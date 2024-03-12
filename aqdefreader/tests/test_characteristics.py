from ..characteristic import Characteristic
import unittest


class CharacteristicTestCase(unittest.TestCase):
    def setUp(self):
        self.characteristic = Characteristic()

    def test_init(self):
        self.assertTrue(len(self.characteristic.get_data_keys()) == 0)
        self.assertTrue(len(self.characteristic.get_measurements()) == 0)

    def test_data(self):
        self.characteristic.set_data(1, 1)
        self.characteristic.set_data("abc12345", 1)
        self.characteristic.set_data(2, "abc12345")
        self.assertListEqual(self.characteristic.get_data_keys(), [1, "abc12345", 2])
        self.assertEqual(self.characteristic.get_data(1), 1)
        self.assertEqual(self.characteristic.get_data(2), "abc12345")

    def test_data_get(self):
        self.characteristic.set_data(key="key", data=4711)
        self.assertEqual(self.characteristic.get_data("key"), 4711)

    def test_get_measurement(self):
        self.characteristic._append_measurement(4711)
        self.characteristic._append_measurement(4711)
        self.characteristic._append_measurement(4711)
        self.assertEqual(len(self.characteristic.get_measurements()), 3)
        self.assertIsInstance(self.characteristic.get_measurements(), list)
