from products import Product
from store import Store
from active_inactive_list import get_active_list, get_inactive_list, print_active_list, print_inactive_list


# Function: Takes user input to choose a number corresponding to an option in an iterable.
def choice_input(iterable):
    """
    Handles user input for choosing a number within a given range based on the length of an iterable.

    Parameters:
    iterable (iterable): An iterable object (e.g., list) that defines the range of available options.

    Returns:
    str: The user's choice as a string if valid, or None if the user chooses to exit by pressing Enter.

    Raises:
    ValueError: If the input is not a valid number within the specified range.
    """
    while True:
        try:
            choice = input(f"Please choose a number between 1 - {len(iterable)}: ")

            if choice:
                if int(choice) not in range(1, len(iterable) + 1):
                    raise ValueError(f"You must enter a number between 1 - {len(iterable)}.")
                return str(choice)
            else:
                return None

        except ValueError as ve:
            print(f"An error occurred in choice_input: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred in choice_input: {e}")


# Function: Takes user input for selecting a product and its order quantity.
def order_input(store_object):
    """
    Handles the input for ordering a product by allowing the user to select a product and specify the quantity.

    Parameters:
    store_object (Store): An instance of the Store class that contains the active products.

    Returns:
    tuple: A tuple containing the order number (str) and the order quantity (int), or (None, None) if the user quits.

    Raises:
    ValueError: If the user inputs an invalid quantity exceeding stock.
    """
    active_list = get_active_list(store_object)

    try:
        while True:
            print("Which product # would you like to purchase? Press enter to quit or end your order.")
            order_number = choice_input(active_list)

            if not order_number:  # User pressed Enter to quit
                return None, None

            while True:
                order_quantity = input("Please enter the amount or press enter to quit or end your order: ")

                if not order_quantity:  # User pressed Enter to quit
                    return None, None

                for product in active_list:
                    if str(order_number) == str(product[0]):  # Check against the product index
                        order_name = product[1]
                        current_stock = Product.get_stock_quan(order_name)
                        print(f"The current stock for '{order_name}' is {current_stock}")

                        if int(order_quantity) > int(current_stock):
                            print(f"Your order exceeds the current stock {current_stock}, please try again.")
                        else:
                            return str(order_number), int(order_quantity)

    except ValueError as ve:
        print(f"An error occurred in order_input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred in order_input: {e}")