import products
import store
from user_input import choice_input
from active_inactive_list import get_active_list, print_active_list
from shopping_list import get_order_list, calc_grand_total
import sys


product_list = [ products.Product("MacBook Air M2", price=1000, quantity=50),
                 products.Product("Bose QuietComfort Earbuds", price=200, quantity=100),
                 products.Product("Google Pixel 7", price=100, quantity=200)
               ]

best_buy = store.Store(product_list)


def start(store_object):

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

    start(best_buy)


if __name__ == "__main__":
    main()





