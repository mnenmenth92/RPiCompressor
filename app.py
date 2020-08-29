from gpio_driver import GPIODriver
from analog_input import AnalogInput
from rpi_compressor import RpiCompressor

gpio_driver = GPIODriver()
analog_input = AnalogInput()
rpi_compressor = RpiCompressor(analog_input, gpio_driver)







if __name__ == '__main__':
    try:
        # ToDo run flask server
        pass
    except AttributeError:
        pass
    finally:
        pump.cleanup_gpio()
