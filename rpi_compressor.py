from config import initial_pressure_limit, initial_pressure_hysteresis
class RpiCompressor():
    """
    combines analog input and pwm driver for compressor functionality
    """
    def __init__(self, analog_input, gpio_driver):
        self.analog_input = analog_input
        self.gpio_driver = gpio_driver
        self.pressure_limit = initial_pressure_limit
        self.pressure_hysteresis = initial_pressure_hysteresis
        self.state = False

    def manage_pressure(self):
        """
        runs/stops pump when needed.
        when pressure greater than limit than stop pump
        when pressure less than limit - hysteresis than start pump
        :return: current state
        """
        self.analog_input.update()
        ai_value = self.analog_input.current_value
        if ai_value > self.pressure_limit:
            self.gpio_driver.stop_pwm()
            self.state = False
            self.set_led_value(self.state)
        elif ai_value < self.pressure_limit - self.pressure_hysteresis:
            self.gpio_driver.set_pwm()
            self.state = True
            self.set_led_value(self.state)
        return self.state

    # set led digital output
    def set_led_value(self, value):
        self.gpio_driver.set_do_value('tank_full_led', value)



