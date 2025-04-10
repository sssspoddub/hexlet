class Counter:
    value = 0

    def inc(self, delta=1):
        self.value += delta

    def dec(self, delta=1):
        self.value = max(0, self.value - delta)


c = Counter()
c.inc()
c.inc()
c.inc(40)
c.dec(delta=100)
print(c.value)
