class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


# BEGIN (write your solution here)
class LimitedCounter(Counter):
    def __init__(self, limit=0):
        super().__init__()
        self.limit = limit

    def inc(self, amount=1):
        self.value = min(self.limit, self.value + amount)

    def dec(self, amount=1):
        self.value = max(0, self.value - amount)
