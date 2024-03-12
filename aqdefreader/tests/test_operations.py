from ..operations import read_dfq_file, create_characteristic_dataframe
from .testdata import TEST_DFQ_LINES
import unittest
import os


class IntegrationTestCase(unittest.TestCase):
    __FILENAME = "testfile.dfq"

    def setUp(self):
        with open(self.__FILENAME, "w") as f:
            f.writelines(line + "\n" for line in TEST_DFQ_LINES)

    def tearDown(self):
        if os.path.exists(self.__FILENAME):
            os.remove(self.__FILENAME)

    def test_file_read(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        self.assertEqual(parsed_file.part_count(), 1)

    def test_file_read_characteristics(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        self.assertEqual(len(parsed_file.get_part(0).get_characteristics()), 3)

    def test_file_read_part_name(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        self.assertEqual(parsed_file.get_part(0).get_data("K1001"), "08/15")

    def test_characteristic_df(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        df = create_characteristic_dataframe(
            parsed_file.get_part(0).get_characteristics()[0]
        )
        self.assertEqual(len(df), 11)
        self.assertEqual(df.value[0], 9.94)
        self.assertEqual(df.value[len(df) - 1], 10.17)

    def test_characteristic_nogroup_df_values(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        df = create_characteristic_dataframe(
            parsed_file.get_part(0).get_characteristics()[0]
        )
        # These two entries have the same datetime index, so access via datetime
        # will fail as not unique. Therefore access via index.
        self.assertEqual(df.value[4], 10.02)
        self.assertEqual(df.value[5], 10.06)

    def test_characteristic_nogroup_df_date_values(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        df = create_characteristic_dataframe(
            parsed_file.get_part(0).get_characteristics()[0]
        )
        self.assertEqual(df.datetime[4], df.datetime[5])

    def test_characteristic_group_df(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        df = create_characteristic_dataframe(
            parsed_file.get_part(0).get_characteristics()[0], True
        )
        self.assertEqual(len(df), 10)

    def test_characteristic_group_df_values(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        df = create_characteristic_dataframe(
            parsed_file.get_part(0).get_characteristics()[0], True
        )
        self.assertEqual(df.value["1999-08-12 15:25:02"], 10.04)
