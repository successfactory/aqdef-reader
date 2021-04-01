from ..measurement import Measurement
from datetime import datetime
import unittest


class MeasurementTestCase(unittest.TestCase):
    def test_init(self):
        d = datetime.now()
        m = Measurement(123, 4711, d, "whatever", 123, 456, 789, "machno", "no-param", "ok")
        self.assertTrue(m.value == 123)
        self.assertTrue(m.attribute == 4711)
        self.assertTrue(m.datetime == d)
        self.assertTrue(m.event == "whatever")
        self.assertTrue(m.batch_no == 123)
        self.assertTrue(m.nest_no == 456)
        self.assertTrue(m.controller_no == 789)
        self.assertTrue(m.machine_no == "machno")
        self.assertTrue(m.process_parameter == "no-param")
        self.assertTrue(m.control_no == "ok")

    def test_dict(self):
        d = datetime.now()
        m = Measurement(123, 4711, d, "whatever", 123, 456, 789, "machno", "no-param", "ok")
        self.assertDictEqual(m.as_dict(), {"datetime": d, "value": 123})
