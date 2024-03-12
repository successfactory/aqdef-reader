from ..file import DfqFile
from .testdata import TEST_3D_LINES, TEST_DFQ_LINES
import unittest


class DfqFileTestCase(unittest.TestCase):
    def setUp(self):
        self.test_3d_file = DfqFile(TEST_3D_LINES)
        self.test_dfq_file = DfqFile(TEST_DFQ_LINES)

    def test_3d_init(self):
        self.assertEqual(self.test_3d_file.part_count(), 1)
        self.assertEqual(len(self.test_3d_file.get_part(0).get_characteristics()), 4)

    def test_3d_file_characteristics1(self):
        self.assertEqual(
            self.test_3d_file.get_part(0).get_characteristic_by_index(1).get_data("K2002"),
            "3D-Position",
        )

    def test_3d_file_characteristics2(self):
        self.assertEqual(
            self.test_3d_file.get_part(0).get_characteristic_by_index(2).get_data("K2004"),
            0,
        )

    def test_3d_file_characteristics3(self):
        self.assertEqual(
            self.test_3d_file.get_part(0).get_characteristic_by_index(3).get_data("K2110"),
            15.8,
        )

    def test_3d_file_characteristics4(self):
        self.assertEqual(
            self.test_3d_file.get_part(0).get_characteristic_by_index(4).get_data("K2111"),
            20.2,
        )

    def test_3d_file_measurements(self):
        for i, ch in enumerate(self.test_3d_file.get_part(0).get_characteristics()):
            self.assertEqual(len(ch.get_measurements()), 1)

            if i == 0:
                self.assertEqual(ch.get_measurements()[0].attribute, 256)
            elif i == 3:
                self.assertEqual(ch.get_measurements()[0].value, 20.006)

    def test_dfq_init_part_count(self):
        self.assertEqual(self.test_dfq_file.part_count(), 1)

    def test_dfq_init_part_name(self):
        self.assertEqual(self.test_dfq_file.get_part(0).get_data("K1001"), "08/15")

    def test_dfq_init_part_characteristic_count(self):
        self.assertEqual(len(self.test_dfq_file.get_part(0).get_characteristics()), 3)

    def test_dfq_file_characteristics_laenge(self):
        self.assertEqual(
            self.test_dfq_file.get_part(0)
            .get_characteristic_by_index(1)
            .get_data("K2002"),
            "Länge",
        )

    def test_dfq_file_characteristics_durchmesser(self):
        self.assertEqual(
            self.test_dfq_file.get_part(0)
            .get_characteristic_by_index(2)
            .get_data("K2002"),
            "Durchmesser",
        )

    def test_dfq_file_characteristics_gewinde(self):
        self.assertEqual(
            self.test_dfq_file.get_part(0)
            .get_characteristic_by_index(3)
            .get_data("K2002"),
            "Gewinde",
        )
