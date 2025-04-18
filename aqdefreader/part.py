import numpy as np
from .characteristic import Characteristic


class Part:
    def __init__(self, part_no):
        self.__part_no = part_no
        self.__data = {}
        self.__characteristics = {}

    def get_part_no(self):
        return self.__part_no

    def set_data(self, key, data):
        self.__data[key] = data

    def get_data(self, key):
        return self.__data[key]

    def contains_characteristic(self, index):
        if self.__characteristics.get(index) is not None:
            return True
        return False

    def _append_characteristic(self, characteristic, index=None):
        max_index = 0
        keys = list(self.__characteristics.keys())
        if index is None and len(keys) > 0:
            max_index = keys[np.argmax(np.asarray(keys))]
        this_index = max_index + 1 if index is None else index
        self.__characteristics[this_index] = characteristic
        return this_index

    def get_characteristic_by_index(self, index):
        if not self.contains_characteristic(index):
            self._append_characteristic(Characteristic(), index)
        return self.__characteristics[index]

    def get_characteristics(self):
        all_characteristics = {k: v for k, v in self.__characteristics.items() if k != 0}
        return list(all_characteristics.values())
