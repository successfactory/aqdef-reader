class QDasPart:
    def __init__(self, part_no):
        self.__part_no = part_no
        self.__data = {}
        self.__attributes = []

    def get_part_no(self):
        return self.__part_no

    def set_data(self, key, data):
        self.__data[key] = data

    def get_data(self, key):
        return self.__data[key]

    def contains_attribute(self, index):
        if len(self.__attributes) >= index:
            return True
        return False

    def append_attribute(self, attribute):
        self.__attributes.append(attribute)
        return len(self.__attributes)-1

    def get_attribute_by_index(self, index):
        return self.__attributes[index-1]

    def get_attributes(self):
        return self.__attributes
