from ..operations import create_column_dataframe, read_dfq_file
import numpy as np
import pandas as pd
import unittest


class DfqFileIntegrationTestCase(unittest.TestCase):
    __FILENAME = "aqdefreader/tests/testmeasures.dfq"

    def test_file_read(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        self.assertEqual(parsed_file.part_count(), 1)

    def test_file_read_characteristics(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        self.assertEqual(len(parsed_file.get_part(0).get_characteristics()), 2)

    def test_file_read_part_name(self):
        parsed_file = read_dfq_file(self.__FILENAME)
        self.assertEqual(parsed_file.get_part(0).get_data("K1001"), "Teil 123.456.789")

    def test_file_df_count(self):
        data = {
            "Diameter": [249.895, 249.905, 249.780, np.nan],
            "Diameter before drill": [249.485, 249.515, np.nan, 249.340],
        }

        test_df = pd.DataFrame(
            data,
            index=[
                pd.to_datetime("2002-05-17 05:54:58"),
                pd.to_datetime("2002-05-17 15:38:08"),
                pd.to_datetime("2002-05-18 18:14:43"),
                pd.to_datetime("2002-05-18 18:14:57"),
            ],
        )

        parsed_file = read_dfq_file(self.__FILENAME)
        df = create_column_dataframe(parsed_file)

        self.assertDictEqual(test_df.fillna(0).to_dict(), df.fillna(0).to_dict())
