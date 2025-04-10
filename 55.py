class Counter:
    def __init__(self, value=0):
        self.__dict__['value'] = max(0, value)

    def inc(self, num=1):
        return Counter(self.value + num)

    def dec(self, num=1):
        return Counter(max(0, self.value - num))
