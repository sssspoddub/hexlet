def update_inventory(inventory, name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity


def get_stock(inventory, name):
    return inventory.get(name, 0)
