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


class LimitedCounter(Counter):
    def __init__(self, limit=None):
        super().__init__()
        self.limit = limit

    def inc(self, amount=1):
        new_value = self.value + amount
        if self.limit is not None:
            new_value = min(new_value, self.limit)
        self.value = max(new_value, 0)
