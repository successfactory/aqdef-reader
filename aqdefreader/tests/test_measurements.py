from ..measurement import Measurement
from datetime import datetime
import unittest


class MeasurementTestCase(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now()
        self.measurement = Measurement(
            123, 4711, self.now, "whatever", 123, 456, 789, "machno", "no-param", "ok"
        )

    def test_measurement_init_value(self):
        self.assertTrue(self.measurement.value == 123)

    def test_measurement_init_attribute(self):
        self.assertTrue(self.measurement.attribute == 4711)

    def test_measurement_init_datetime(self):
        self.assertTrue(self.measurement.datetime == self.now)

    def test_measurement_init_event(self):
        self.assertTrue(self.measurement.event == "whatever")

    def test_measurement_init_bacth_no(self):
        self.assertTrue(self.measurement.batch_no == 123)

    def test_measurement_init_nest_no(self):
        self.assertTrue(self.measurement.nest_no == 456)

    def test_measurement_init_controller_no(self):
        self.assertTrue(self.measurement.controller_no == 789)

    def test_measurement_init_machine_no(self):
        self.assertTrue(self.measurement.machine_no == "machno")

    def test_measurement_init_process_parameter(self):
        self.assertTrue(self.measurement.process_parameter == "no-param")

    def test_measurement_init_control_no(self):
        self.assertTrue(self.measurement.control_no == "ok")

    def test_value_dictionary(self):
        d = datetime.now()
        m = Measurement(
            123, 4711, d, "whatever", 123, 456, 789, "machno", "no-param", "ok"
        )
        self.assertDictEqual(m.as_value_dictionary(), {"datetime": d, "value": 123})

    def test_subgroup_dictionary(self):
        m = Measurement(subgroup_size=1000, error_count=1)
        self.assertDictEqual(
            m.as_dictionary(),
            {
                "datetime": None,
                "value": None,
                "attribute": None,
                "event": None,
                "batch_no": None,
                "nest_no": None,
                "controller_no": None,
                "machine_no": None,
                "process_parameter": None,
                "control_no": None,
                "subgroup_size": 1000,
                "error_count": 1
            },
        )

    def test_full_dictionary(self):
        d = datetime.now()
        m = Measurement(
            123, 4711, d, "whatever", 123, 456, 789, "machno", "no-param", "ok"
        )
        self.assertDictEqual(
            m.as_dictionary(),
            {
                "datetime": d,
                "value": 123,
                "attribute": 4711,
                "event": "whatever",
                "batch_no": 123,
                "nest_no": 456,
                "controller_no": 789,
                "machine_no": "machno",
                "process_parameter": "no-param",
                "control_no": "ok",
                "subgroup_size": None,
                "error_count": None
            },
        )

    def test_full_dictionary_with_empty_data(self):
        d = datetime.now()
        m = Measurement(123, 4711, d)
        self.assertDictEqual(
            m.as_dictionary(),
            {
                "datetime": d,
                "value": 123,
                "attribute": 4711,
                "event": None,
                "batch_no": None,
                "nest_no": None,
                "controller_no": None,
                "machine_no": None,
                "process_parameter": None,
                "control_no": None,
                "subgroup_size": None,
                "error_count": None
            },
        )
