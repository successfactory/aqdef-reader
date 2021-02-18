from ..attribute import QDasAttribute
import unittest

class AttributeTestCase(unittest.TestCase):
    def setUp(self):
        self.attribute = QDasAttribute()

    def test_init(self):
        self.assertTrue(len(self.attribute.get_data_keys()) == 0)
        self.assertTrue(len(self.attribute.get_measurements()) == 0)

    def test_data(self):
        self.attribute.set_data(1, 1)
        self.attribute.set_data("abc12345", 1)
        self.attribute.set_data(2, "abc12345")
        self.assertListEqual(self.attribute.get_data_keys(), [1, "abc12345", 2])
        self.assertEqual(self.attribute.get_data(1), 1)
        self.assertEqual(self.attribute.get_data(2), "abc12345")

    def test_data_get(self):
        self.attribute.set_data(key="key", data=4711)
        self.assertEqual(self.attribute.get_data("key"), 4711)

    def test_get_measurement(self):
        self.attribute.append_measurement(4711)
        self.attribute.append_measurement(4711)
        self.attribute.append_measurement(4711)
        self.assertEqual(len(self.attribute.get_measurements()), 3)
        print(type(self.attribute.get_measurements()))
        self.assertIsInstance(self.attribute.get_measurements(), list)
