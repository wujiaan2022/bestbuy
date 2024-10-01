# This module provides functions to get and print lists of active and inactive products from a store.
# Functions include getting the active/inactive products and printing them in a user-friendly format.

# Function: Retrieves a list of active products in the store
def get_active_list(store_object):
    """
    Retrieves a list of active products from the store.

    Parameters:
    store_object (Store): An instance of the Store class containing the products.

    Returns:
    list: A list of tuples, where each tuple contains the index and the product object.
    """
    active_list = []
    active_products = store_object.get_active_products()  # Always get the latest active products

    for i, product in enumerate(active_products, start=1):
        active_list.append((i, product))
    return active_list


# Function: Prints the list of active products in the store
def print_active_list(store_object):
    """
    Prints a list of active products from the store.

    Parameters:
    store_object (Store): An instance of the Store class containing the products.
    """
    active_list = get_active_list(store_object)
    for product in active_list:
        print(f"{product[0]}. {product[1]}")


# Function: Retrieves a list of inactive products in the store
def get_inactive_list(store_object):
    """
    Retrieves a list of inactive products from the store.

    Parameters:
    store_object (Store): An instance of the Store class containing the products.

    Returns:
    list: A list of tuples, where each tuple contains the index and the product object.
    """
    inactive_list = []
    inactive_products = store_object.get_inactive_products()  # Always get the latest inactive products

    for i, product in enumerate(inactive_products, start=1):
        inactive_list.append((i, product))
    return inactive_list


# Function: Prints the list of inactive products in the store
def print_inactive_list(store_object):
    """
    Prints a list of inactive products from the store.

    Parameters:
    store_object (Store): An instance of the Store class containing the products.
    """
    inactive_list = get_inactive_list(store_object)
    for product in inactive_list:
        print(f"{product[0]}. {product[1]}")
