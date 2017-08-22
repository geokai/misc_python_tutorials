"""a simple temperature script to explore the @property decorator"""


class Celsius():
    """Celsius temperature class"""

    def __init__(self, temperature=0):
        """initialize a temperature object"""
        self.temperature = temperature

    @property
    def to_fahrenheit(self):
        """convert to fahrenheit"""
        self._scale = 'Fahrenheit'
        print('Scale now: {}'.format(self._scale))
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        """returns temperature"""
        print('Getting {} value:'.format(self._scale))
        self._scale = 'Celsius'
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        """set the temperature value, but not below -273 degrees"""
        if value < -273:
            raise ValueError('Temperature below -273 is not possible')
        self._scale = 'Celsius'
        print('Setting {} value: \n{}'.format(self._scale, value))
        self._temperature = value

    @property
    def default_scale(self):
        """returns default scale"""
        self._scale = 'Celsius'
        return 'Default scale is: ' + self._scale


    # temperature = property(get_temperature, set_temperature)
