from ..file import DfqFile
import unittest


class DfqFileTestCase(unittest.TestCase):
    def setUp(self):
        test_3d_lines = [
            "K0100 4",
            "K1002 Teil",
            "K2002/1 3D-Position",
            "K2004/1 0",
            "K2008/1 10",
            "K2002/2 X-Achse",
            "K2004/2 0",
            "K2110/2 9,8",
            "K2111/2 10,2",
            "K2002/3 Y-Achse",
            "K2004/3 0",
            "K2110/3 15,8",
            "K2111/3 16,2",
            "K2002/4 Z-Achse",
            "K2004/4 0",
            "K2110/4 19,8",
            "K2111/4 20,2",
            "K5111/1 1",
            "K5112/2 1",
            "K5103/1 2",
            "K5102/2 2",
            "K5102/2 3",
            "K5102/2 4",
            "K0001/1 0",
            "K0002/1 256",
            "K0001/2 10,023",
            "K0001/3 15,986",
            "K0001/4 20,006"]
        self.test_3d_file = DfqFile(test_3d_lines)

        test_dfq_lines = [
            "K0100 3",
            "K1001 08/15",
            "K1002 Teil 1",
            "K2001/1 1.1",
            "K2002/1 Länge",
            "K2311/1 Drehen",
            "K2402/1 Meßschieber",
            "K2002/2 Durchmesser",
            "K2022/2 3",
            "K2402/2 Meßschieber",
            "K2002/3 Gewinde",
            "K2004/3 1",
            "K2011/3 200",
            "K2311/3 Schneiden",
            "K2402/3 Lehre",
            "9.94012.08.1999/15:23:450#1230.96601000001",
            "9.95012.08.1999/15:23:580#1231.09101000002",
            "9.98012.08.1999/15:24:120#1230.99301000003",
            "10.01012.08.1999/15:24:380#1230.96401000001",
            "10.02012.08.1999/15:25:020#1230.91501000001",
            "10.06012.08.1999/15:25:370#1231.01101000002",
            "9.94012.08.1999/15:25:590#1231.00901000001",
            "9.99012.08.1999/15:26:170#1231.01101000002",
            "10.00012.08.1999/15:26:500#1231.06201000002",
            "10.03012.08.1999/15:27:230#1231.01101000001",
            "10.17012.08.1999/15:27:563#1231.00901000001"]
        self.test_dfq_file = DfqFile(test_dfq_lines)

    def test_3d_init(self):
        self.assertEqual(len(self.test_3d_file.parts), 1)
        self.assertEqual(len(self.test_3d_file.parts[0].get_characteristics()), 4)

    def test_3d_file_characteristics(self):
        self.assertEqual(self.test_3d_file.parts[0].get_characteristic_by_index(1).get_data("K2002"), "3D-Position")
        self.assertEqual(self.test_3d_file.parts[0].get_characteristic_by_index(2).get_data("K2004"), 0)
        self.assertEqual(self.test_3d_file.parts[0].get_characteristic_by_index(3).get_data("K2110"), 15.8)
        self.assertEqual(self.test_3d_file.parts[0].get_characteristic_by_index(4).get_data("K2111"), 20.2)

    def test_3d_file_measurements(self):
        for i, ch in enumerate(self.test_3d_file.parts[0].get_characteristics()):
            self.assertEqual(len(ch.get_measurements()), 1)

            if i == 0:
                self.assertEqual(ch.get_measurements()[0].attribute, 256)
            elif i == 3:
                self.assertEqual(ch.get_measurements()[0].value, 20.006)

    def test_dfq_init(self):
        self.assertEqual(len(self.test_dfq_file.parts), 1)
        # test name
        self.assertEqual(self.test_dfq_file.parts[0].get_data("K1001"), "08/15")
        self.assertEqual(len(self.test_dfq_file.parts[0].get_characteristics()), 3)

    def test_dfq_file_characteristics(self):
        self.assertEqual(self.test_dfq_file.parts[0].get_characteristic_by_index(1).get_data("K2002"), "Länge")
        self.assertEqual(self.test_dfq_file.parts[0].get_characteristic_by_index(2).get_data("K2002"), "Durchmesser")
        self.assertEqual(self.test_dfq_file.parts[0].get_characteristic_by_index(3).get_data("K2002"), "Gewinde")
