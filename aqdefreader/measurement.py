class Measurement:
    def __init__(
        self,
        value=None,  # K0001
        attribute=None,  # K0002
        date_time=None,  # K0004
        event=None,  # K0005
        batch_no=None,  # K0006
        nest_no=None,  # K0007
        controller_no=None,  # K0008
        machine_no=None,  # K0010
        process_parameter=None,  # K0011
        control_no=None,
        subgroup_size=None,
        error_count=None,
    ):
        self.value = value
        self.attribute = attribute
        self.datetime = date_time
        self.event = event
        self.batch_no = batch_no
        self.nest_no = nest_no
        self.controller_no = controller_no
        self.machine_no = machine_no
        self.process_parameter = process_parameter
        self.control_no = control_no
        self.subgroup_size = subgroup_size
        self.error_count = error_count

    def as_value_dictionary(self):
        "Returns the measurement as dictionary. The entry is limited to the datetime and the value."
        return {"datetime": self.datetime, "value": self.value}

    def as_dictionary(self):
        "Returns the measurement as dictionary."
        return {
            "datetime": self.datetime,
            "value": self.value,
            "attribute": self.attribute,
            "event": self.event,
            "batch_no": self.batch_no,
            "nest_no": self.nest_no,
            "controller_no": self.controller_no,
            "machine_no": self.machine_no,
            "process_parameter": self.process_parameter,
            "control_no": self.control_no,
            "subgroup_size": self.subgroup_size,
            "error_count": self.error_count,
        }
