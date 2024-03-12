class Characteristic:
    def __init__(self):
        self.__data = {}
        self.__measurements = []

    def set_data(self, key, data):
        self.__data[key] = data

    def get_data(self, key):
        if key in self.__data.keys():
            return self.__data[key]

    def get_data_keys(self):
        return list(self.__data.keys())

    def _append_measurement(self, measurement):
        self.__measurements.append(measurement)

    def get_measurements(self):
        return self.__measurements

    def get_last_measurement(self):
        return self.__measurements[-1]
