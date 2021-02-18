class QDasMeasurement:
    def __init__(self, value, attribute, date_time, event, batch_no, nest_no, controller_no, machine_no, process_parameter,
                 control_no):
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
