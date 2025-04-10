class Truncater:
    OPTIONS = {
        'separator': '...',
        'length': 200,
    }

    def __init__(self, **kwargs):
        self.options = {**Truncater.OPTIONS, **kwargs}

    def truncate(self, text, **kwargs):
        config = {**self.options, **kwargs}
        length = config['length']
        separator = config['separator']

        if len(text) <= length:
            return text

        return text[:length] + separator
