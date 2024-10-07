import products
import store
import promotions
from user_input import choice_input
from active_inactive_list import get_active_list, print_active_list
from shopping_list import get_order_list, calc_grand_total
import sys

"""
This script simulates a store's basic operations like listing products, 
checking total quantity, placing an order, and quitting the program. 
It demonstrates the interaction between the `Product`, `Store`, and 
various utility modules to handle store operations.

Modules:
- products: Contains the Product class to manage product details.
- store: Contains the Store class to manage the store's products.
- user_input: Provides functions for user input handling.
- active_inactive_list: Handles displaying active products.
- shopping_list: Handles order creation and calculation.
"""


def start(store_object):
    """
        Starts the store menu and handles the interaction with the user.

        Parameters:
        store_object (Store): An instance of the Store class containing the products.

        The user can choose to:
        1. List all products in the store
        2. Show the total quantity of items in the store
        3. Make an order from the store
        4. Quit the program
        """

    menu = {
        "1": "List all products in store",
        "2": "Show total amount in store",
        "3": "Make an order",
        "4": "Quit"
    }

    title = "Store Menu\n"
    dash_line = "-" * len(title)

    while True:

        print(dash_line)
        print(title)

        for key, value in menu.items():
            print(f"{key}. {value}")

        print(dash_line)

        choice = choice_input(menu)

        if choice == "1":
            print()
            print_active_list(store_object)

        elif choice == "2":
            print()
            total_items = store_object.get_total_quantity()  # Use instance method
            print(f"The total items is {total_items}")

        elif choice == "3":
            print("\nProducts list:")
            print_active_list(store_object)
            print()
            shopping_list = get_order_list(store_object)
            print("Your shoppinglist:")
            print(shopping_list)

            if shopping_list:
                grand_total = calc_grand_total(shopping_list)  # Use instance method

                print("*" * 10)

                print(f"Order made! Total payment: {grand_total}\n")

        if choice == "4":
            print()
            sys.exit("Bye!")


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    print(best_buy)

    start(best_buy)


if __name__ == "__main__":
    main()





