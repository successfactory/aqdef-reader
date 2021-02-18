from .part import QDasPart
from .attribute import QDasAttribute
from .measurement import QDasMeasurement
from datetime import datetime


class QDasFile:
    def __init__(self, lines):
        self.parts = []

        self.__part_index = -1

        self.__attribute = 0
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
                self.__parse_data(line)
            else:
                self.__parse_measurements(line)

    def __parse_data(self, line):
        code = line.split(" ", 1)[0]
        value = line.split(" ", 1)[1]

        index = 1
        if len(code) > 5:
            code, index = code.split("/")
            index = int(index)

        # header - number of attributes in file
        if code[0:5] == "K0100":
            print("Count of attributes in QDAS file: {}".format(value))
        # part number
        elif code[0:5] == "K0101":
            self.__part_index += 1
            self.parts.append(QDasPart(value))
        # part information
        elif code[0:2] == "K1":
            if self.__part_index + 1 != index:
                print(f"Warning: Given part index {index} not equal to current index {self.__part_index + 1}.")
            self.parts[self.__part_index].set_data(code, value)
        # attribute information
        elif code[0:2] in ("K2", "K3", "K8"):
            if not self.parts[self.__part_index].contains_attribute(index):
                new_index = self.parts[self.__part_index].append_attribute(QDasAttribute())
                if new_index + 1 != index:
                    print(f"Warning: Given attribute index {index} not equal to current index {new_index + 1}.")
            attr = self.parts[self.__part_index].get_attribute_by_index(index)
            attr.set_data(code, value)

    def __parse_measurements(self, line):
        for i, data in enumerate(line.split("\x0f")):
            # documentation page 46 - scope of measurement info
            self.__attribute = 0
            self.__event = ""
            self.__process_parameter = ""

            elements = data.split("\x14")
            value = float(elements[0])
            if len(elements) >= 2:
                self.__attribute = int(elements[1])

            if self.__attribute not in (255, 256):
                self.__extract_measurement_info(elements)
                measure = QDasMeasurement(value, self.__attribute, self.__datetime, self.__event, self.__batch_no,
                                          self.__nest_no,
                                          self.__controller_no, self.__machine_no, self.__process_parameter,
                                          self.__control_no)
                self.parts[self.__part_index].get_attribute_by_index(i + 1).append_measurement(measure)

    def __extract_measurement_info(self, elements):
        if len(elements) >= 2:
            self.__attribute = int(elements[1])
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
