

class AnalogInput():
    """
    gets data from ADC module
    """

    def __init__(self, input_number):
        self.input_number = input_number
        self.current_value = 0

    def update(self):
        self.current_value = 0  # todo update current value
