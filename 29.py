def create_print():
    name = input('name: ')

    def print_name():
        print(name)

    return print_name


my_print = create_print()
my_print()
