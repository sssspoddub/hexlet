class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }

    def __init__(self, **kwargs):
        self.options = self.OPTIONS.copy()
        self.options.update(kwargs)

    def validate(self, password):
        data = {}
        if len(password) < self.OPTIONS['min_len']:
            data['min_len'] = 'too small'
        if self.options['contain_numbers'] and not self._has_number(password):
            data['contain_numbers'] = 'should contain at least one number'
        return data

    def _has_number(self, password):
        return any(char.isdigit() for char in password)
