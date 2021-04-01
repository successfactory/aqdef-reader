class Measurement:
    def __init__(
        self,
        value,  # K0001
        attribute=None,  # K0002
        date_time=None,  # K0004
        event=None,  # K0005
        batch_no=None,  # K0006
        nest_no=None,  # K0007
        controller_no=None,  # K0008
        machine_no=None,  # K0010
        process_parameter=None,  # K0011
        control_no=None,
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

    def as_dict(self):
        return {"datetime": self.datetime, "value": self.value}
