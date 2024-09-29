from products import Product
from store import Store
from active_inactive_list import get_active_list, get_inactive_list, print_active_list, print_inactive_list


def choice_input(iterable):

    while True:

        try:
            choice = input(f"Please choose a number between 1 - {len(iterable)}: ")

            if choice:

                if int(choice) not in range(1, len(iterable)+1):
                    raise ValueError(f"You must enter a number between 1 - {len(iterable)}.")

                return str(choice)

            else:
                return None

        except ValueError as ve:
            print(f"An error occurred in choice_menu: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred in choice_menu: {e}")


def order_input(store_object):
    active_list = get_active_list(store_object)
    # print(f"DEBUG---The active list in order_input: \n{active_list}")

    try:
        while True:
            print("Which product # would you like to purchase? Press enter to quit or end your order.")
            order_number = choice_input(active_list)

            if not order_number:  # User pressed enter to quit
                return None, None

            while True:
                order_quantity = input("Please enter the amount or press enter to quit or end your order: ")

                if not order_quantity:  # User pressed enter to quit
                    return None, None

                for product in active_list:

                    # print(f"DEBUG---for product in active_list in order_input: {product}")

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
