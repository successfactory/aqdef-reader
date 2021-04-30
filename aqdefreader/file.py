from .part import Part
from .characteristic import Characteristic
from .measurement import Measurement

from datetime import datetime
import re  # regular expression library to parse numbers


class DfqFile:
    def __init__(self, lines):
        self.parts = []

        self.__part_index = -1

        self.__characteristic = 0
        self.__datetime = datetime.now()
        self.__event = ""
        self.__batch_no = ""
        self.__nest_no = 0
        self.__controller_no = 0
        self.__machine_no = 0
        self.__process_parameter = ""
        self.__control_no = 0

        self.__get_lines(lines)

    def __get_lines(self, lines):
        for line in lines:
            if line[0:1] == "K":
                self.__parse_coded_line(line)
            else:
                self.__parse_uncoded_measurements(line)

    def __parse_coded_line(self, line):
        code = line.split(" ", 1)[0]
        value = self.__parse_numeric_value(line.split(" ", 1)[1])

        index = 1
        has_id = False
        if len(code) > 5:
            code, index = code.split("/")
            index = int(index)
            has_id = True

        # header - number of characteristics in file
        if code[0:5] == "K0100":
            print(f"Count of characteristics in DFQ file: {value}")
        # part information
        elif code[0:2] == "K1":
            # create a new part if the index increased
            if self.__part_index + 1 < index:
                self.__part_index += 1
                self.parts.append(Part(value))

            self.parts[self.__part_index].set_data(code, value)
        # characteristic information
        elif code[0:2] in ("K2", "K3", "K8"):
            if not self.parts[self.__part_index].contains_characteristic(index):
                new_index = self.parts[self.__part_index].append_characteristic(
                    Characteristic()
                )
                if new_index + 1 != index:
                    print(
                        f"Warning: Given characteristic index {index} not equal to current index {new_index + 1}"
                    )
            attr = self.parts[self.__part_index].get_characteristic_by_index(index)
            attr.set_data(code, value)
        # measurements
        elif has_id:
            self.__parse_coded_measurement(code, index, value)

    def __parse_coded_measurement(self, code, index, value):
        if code[0:5] in ("K0001"):
            measure = Measurement(value)
            self.parts[self.__part_index].get_characteristic_by_index(
                index
            ).append_measurement(measure)
        elif code[0:5] in ("K0002"):
            self.parts[self.__part_index].get_characteristic_by_index(
                index
            ).get_last_measurement().attribute = value
        elif code[0:5] in ("K0004"):
            self.parts[self.__part_index].get_characteristic_by_index(
                index
            ).get_last_measurement().datetime = datetime.strptime(
                value, "%d.%m.%Y/%H:%M:%S"
            )

    def __parse_uncoded_measurements(self, line):
        for i, data in enumerate(line.split("\x0f")):
            # documentation page 46 - scope of measurement info
            self.__characteristic = 0
            self.__event = ""
            self.__process_parameter = ""

            elements = data.split("\x14")
            value = float(elements[0])
            if len(elements) >= 2:
                self.__characteristic = int(elements[1])

            if self.__characteristic not in (255, 256):
                self.__extract_measurement_info(elements)
                measure = Measurement(
                    value,
                    self.__characteristic,
                    self.__datetime,
                    self.__event,
                    self.__batch_no,
                    self.__nest_no,
                    self.__controller_no,
                    self.__machine_no,
                    self.__process_parameter,
                    self.__control_no,
                )
                self.parts[self.__part_index].get_characteristic_by_index(
                    i + 1
                ).append_measurement(measure)

    def __extract_measurement_info(self, elements):
        if len(elements) >= 2:
            self.__characteristic = int(elements[1])
        if len(elements) >= 3:
            self.__datetime = datetime.strptime(elements[2], "%d.%m.%Y/%H:%M:%S")
        if len(elements) >= 4:
            self.__event = elements[3]
        if len(elements) >= 5:
            self.__batch_no = elements[4]
        if len(elements) >= 6:
            self.__nest_no = int(elements[5])
        if len(elements) >= 7:
            self.__controller_no = int(elements[6])
        if len(elements) >= 8:
            self.__machine_no = int(elements[7])
        if len(elements) >= 9:
            self.__process_parameter = elements[8]
        if len(elements) >= 10:
            self.__control_no = int(elements[9])

    def __parse_numeric_value(self, value):
        intnumber = re.compile(r"^\d+$")
        decnumber = re.compile(r"^\d+(?:,\d*)?$")

        if intnumber.match(value):
            return int(value)
        elif decnumber.match(value):
            return float(value.replace(",", "."))

        return value