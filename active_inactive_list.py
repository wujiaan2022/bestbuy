def get_active_list(store_object):

    active_list = []
    active_products = store_object.get_active_products()  # Always get the latest active products

    for i, product in enumerate(active_products, start=1):
        active_list.append((i, product))
    return active_list


def print_active_list(store_object):

    active_list = get_active_list(store_object)
    for product in active_list:
        print(f"{product[0]}. {product[1]}")


def get_inactive_list(store_object):

    inactive_list = []
    inactive_products = store_object.get_inactive_products()  # Always get the latest inactive products

    for i, product in enumerate(inactive_products, start=1):
        inactive_list.append((i, product))
    return inactive_list


def print_inactive_list(store_object):

    inactive_list = get_inactive_list(store_object)
    for product in inactive_list:
        print(f"{product[0]}. {product[1]}")


