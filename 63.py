class HourClock:
    def __init__(self):
        self.position = 0

    @property
    def hours(self):
        return self.position

    @hours.setter
    def hours(self, value=0):
        self.position = value % 12
