def update_inventory(inventory, goods, quantity):
    if goods in inventory:
        inventory[goods] += quantity
    else:
        inventory[goods] = quantity


def get_stock(inventory, goods):
    return inventory.get(goods, 0)
