from .menu import AVAILABLE_MENU


def get_item(item_id: int):
    for item in AVAILABLE_MENU:
        if item["id"] == item_id:
            return item


def add_item_to_tab(table_tab: list, item_id: int, amount: int):
    item = get_item(item_id)

    if not item:
        return False

    table_tab.append(dict(**item, amount=amount))
    return True


def calculate_tab(table_tab: list):
    count = 0
    for item in table_tab:
        count += item["price"] * item["amount"]

    return count
