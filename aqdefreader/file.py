from .part import Part
from .measurement import Measurement

from datetime import datetime
import dateutil.parser
import re  # regular expression library to parse numbers


class DfqFile:
    def __init__(self, lines):
        self.__parts = []
        self.__part_index = -1

        self.__value = 0
        self.__characteristic = 0
        self.__datetime = datetime.now()
        self.__event = ""
        self.__batch_no = ""
        self.__nest_no = 0
        self.__controller_no = 0
        self.__machine_no = 0
        self.__process_parameter = ""
        self.__control_no = 0
        self.__subgroup_size = 0
        self.__error_count = 0

        self.__get_lines(lines)

    def get_part(self, index):
        return self.__parts[index]

    def get_parts(self):
        return self.__parts

    def part_count(self):
        return len(self.__parts)

    def __parse_datatime(self, value):
        try:
            return dateutil.parser.parse(value)
        except ValueError:
            print(f"Warning: {value} cannot be parsed as datetime")
            return None

    def __get_lines(self, lines):
        for line in lines:
            if line:
                if line[0:1] == "K":
                    self.__parse_coded_line(line)
                else:
                    self.__parse_uncoded_measurements(line)

    def __parse_coded_line(self, line):
        line_elements = line.split(" ", 1)
        code = line_elements[0]
        value = DfqFile.__parse_numeric_value(line.split(" ", 1)[1]) if len(line_elements) > 1 else None

        index = 1
        has_id = False
        if len(code) > 5:
            code, index = code.split("/")
            index = int(index)
            has_id = True

        # characterictics for all characteristics
        if value is None:
            print(f"Warning: code {code} for index {index} has no value")
        # header - number of characteristics in file
        elif code[0:5] == "K0100":
            print(f"Count of characteristics in DFQ file: {value}")
        # part information
        elif code[0:2] == "K1":
            # create a new part if the index increased
            if self.__part_index + 1 < index:
                self.__part_index += 1
                self.__parts.append(Part(value))

            self.__parts[self.__part_index].set_data(code, value)
        # characteristic information
        elif code[0:2] in ("K2", "K3", "K8"):
            attr = self.__parts[self.__part_index].get_characteristic_by_index(index)
            attr.set_data(code, value)
        # measurements
        elif has_id:
            self.__parse_coded_measurement(code, index, value)

    def __parse_coded_measurement(self, code, index, value):
        if code[0:5] in ("K0001"):
            measure = Measurement(value)
            self.__parts[self.__part_index].get_characteristic_by_index(
                index
            )._append_measurement(measure)
        elif code[0:5] in ("K0002"):
            self.__parts[self.__part_index].get_characteristic_by_index(
                index
            ).get_last_measurement().attribute = value
        elif code[0:5] in ("K0004"):
            self.__parts[self.__part_index].get_characteristic_by_index(
                index
            ).get_last_measurement().datetime = self.__parse_datatime(
                value
            )

    def __parse_uncoded_measurements(self, line):
        for i, data in enumerate(line.split("\x0f")):
            # documentation page 46 - scope of measurement info
            self.__characteristic = 0
            self.__event = ""
            self.__process_parameter = ""

            # Get the information if the characteristic is variable or
            # attributed. If attributed, subgroup size is part of the
            # data and needs to be extracted.
            attributed = 0
            if (
                self.__parts[self.__part_index].contains_characteristic(i + 1)
                and "K2004"
                in self.__parts[self.__part_index]
                .get_characteristic_by_index(i + 1)
                .get_data_keys()
            ):
                attributed = (
                    self.__parts[self.__part_index]
                    .get_characteristic_by_index(i + 1)
                    .get_data("K2004")
                )

            elements = data.split("\x14")
            self.__characteristic = 0
            if len(elements) >= 2 and str(elements[1]).strip():
                self.__characteristic = int(elements[1])
            if attributed == 1 and len(elements) >= 4:
                self.__characteristic = int(elements[3])

            if self.__characteristic not in (255, 256):
                self.__extract_measurement_info(attributed, elements)
                measure = Measurement(
                    self.__value,
                    self.__characteristic,
                    self.__datetime,
                    self.__event,
                    self.__batch_no,
                    self.__nest_no,
                    self.__controller_no,
                    self.__machine_no,
                    self.__process_parameter,
                    self.__control_no,
                    self.__subgroup_size,
                    self.__error_count,
                )
                self.__parts[self.__part_index].get_characteristic_by_index(
                    i + 1
                )._append_measurement(measure)

    def __extract_measurement_info(self, attributed, elements):
        offset = 0
        if attributed == 1:
            offset = 2
            self.__subgroup_size = int(elements[0])
            self.__error_count = int(elements[1])

        if len(elements) >= 1 + offset:
            self.__value = float(elements[0 + offset])
        if len(elements) >= 2 + offset and str(elements[1 + offset]).strip():
            self.__characteristic = int(elements[1 + offset])
        if len(elements) >= 3 + offset and str(elements[2 + offset]).strip():
            datetimeValue = self.__parse_datatime(elements[2 + offset])
            self.__datetime = datetimeValue if datetimeValue else self.__datetime
        if len(elements) >= 4 + offset:
            self.__event = elements[3 + offset]
        if len(elements) >= 5 + offset:
            self.__batch_no = elements[4 + offset]
        if len(elements) >= 6 + offset:
            self.__nest_no = int(elements[5 + offset])
        if len(elements) >= 7 + offset:
            self.__controller_no = int(elements[6 + offset])
        if len(elements) >= 8 + offset:
            self.__machine_no = int(elements[7 + offset])
        if len(elements) >= 9 + offset:
            self.__process_parameter = elements[8 + offset]
        if len(elements) >= 10 + offset:
            self.__control_no = int(elements[9 + offset])

    @staticmethod
    def __parse_numeric_value(value):
        intnumber = re.compile(r"^\d+$")
        decnumber = re.compile(r"^\d+(?:,\d*)?$")

        if intnumber.match(value):
            return int(value)
        elif decnumber.match(value):
            return float(value.replace(",", "."))

        return value
