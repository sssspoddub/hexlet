opening_symbols = ['(', '[', '{', '<']
closing_symbols = [')', ']', '}', '>']


def are_symbols_balanced(symbols: str) -> bool:
    stack = []
    for symbol in symbols:
        if symbol in opening_symbols:
            stack.append(symbol)
        elif symbol in closing_symbols:
            if not stack:
                return False
            index = stack.pop()
            if opening_symbols.index(index) != closing_symbols.index(symbol):
                return False
    return len(stack) == 0
