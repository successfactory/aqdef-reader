from ..part import Part
import unittest


class PartTestCase(unittest.TestCase):
    def setUp(self):
        self.part = Part("a testpart")

        self.part.set_data(1, 1)
        self.part.set_data("abc12345", 1)
        self.part.set_data(2, "abc12345")

        self.part.append_characteristic(4711)
        self.part.append_characteristic(4711)
        self.part.append_characteristic(4711)

    def test_init(self):
        self.assertTrue(self.part.get_part_no() == "a testpart")
        self.assertTrue(len(self.part.get_characteristics()) == 3)

    def test_new_data(self):
        self.assertEqual(self.part.get_data(1), 1)
        self.assertEqual(self.part.get_data(2), "abc12345")

    def test_data_get(self):
        self.part.set_data(key="key", data=4711)
        self.assertEqual(self.part.get_data("key"), 4711)

    def test_if_not_initial_characteristics(self):
        self.assertFalse(self.part.contains_characteristic(123))

    def test_contains_characteristics(self):
        self.assertFalse(self.part.contains_characteristic(4711))
        self.assertFalse(self.part.contains_characteristic(4))
        self.assertTrue(self.part.contains_characteristic(3))

    def test_new_characteristics(self):
        self.assertEqual(len(self.part.get_characteristics()), 3)
        self.assertIsInstance(self.part.get_characteristics(), list)

    def test_characteristics_index(self):
        self.assertEqual(self.part.get_characteristic_by_index(1), 4711)
