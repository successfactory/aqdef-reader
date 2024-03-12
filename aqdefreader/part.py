from .characteristic import Characteristic


class Part:
    def __init__(self, part_no):
        self.__part_no = part_no
        self.__data = {}
        self.__characteristic = []

    def get_part_no(self):
        return self.__part_no

    def set_data(self, key, data):
        self.__data[key] = data

    def get_data(self, key):
        return self.__data[key]

    def contains_characteristic(self, index):
        if len(self.__characteristic) >= index:
            return True
        return False

    def _append_characteristic(self, characteristic):
        self.__characteristic.append(characteristic)
        return len(self.__characteristic) - 1

    def get_characteristic_by_index(self, index):
        if not self.contains_characteristic(index):
            self._append_characteristic(Characteristic())
        return self.__characteristic[index - 1]

    def get_characteristics(self):
        return self.__characteristic
