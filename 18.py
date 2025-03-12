dictionary = {
    "foo": "bar",
    "baz": 42,
    "items": {
        1: "apple",
        2: "orange",
        100500: "lemon"
    },
    True: "python"
}

print(dictionary.get("BANG", 'no bang'))
