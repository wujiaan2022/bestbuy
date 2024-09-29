import products
import store
import sys


# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)
#
# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())
#
# bose.show()
# mac.show()
#
# bose.set_quantity(1000)
# bose.show()


# product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
#                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                 products.Product("Google Pixel 7", price=500, quantity=250),
#                ]
#
# store = Store(product_list)
# products = store.get_all_products()
# print(store.get_total_quantity())
# print(store.order([(products[0], 1), (products[1], 2)]))


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = store.Store(product_list)


def get_active_list(store_object):

    active_list = []
    active_products = store_object.get_all_products()  # Always get the latest active products

    for i, product in enumerate(active_products, start=1):
        active_list.append((i, product))
    return active_list


def print_active_list(store_object):

    active_list = get_active_list(store_object)
    for product in active_list:
        print(f"{product[0]}. {product[1]}")


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

    try:
        print("Which product # would you like to purchase? Press enter to quit or end your order.")
        order_number = choice_input(active_list)
        if order_number:
            order_quantity = input("Please enter the amount or press enter to quit or end your order: ")
            if order_quantity:
                return str(order_number), int(order_quantity)
            else:
                return None, None
        else:
            return None, None

    except ValueError as ve:
        print(f"An error occurred in order_input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred in order_input: {e}")


def get_order_list(store_object):
    order_list = []
    while True:
        order_num, order_quan = order_input(store_object)
        # print(order_num, order_quan)

        active_list = get_active_list(store_object)
        if order_num and order_quan:
            for product in active_list:
                # print(product)

                if str(order_num) == str(product[0]):  # Check against the product index
                    order_name = product[1]
                    # print(order_name)

                    order_list.append((order_name, order_quan))
                    print("Product added to your shopping list!\n")
                    break
        else:
            return order_list


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

            if shopping_list:
                total_price = store_object.order(shopping_list)  # Use instance method

                print("*" * 10)

                print(f"Order made! Total payment: {total_price}\n")

        if choice == "4":
            print()
            sys.exit("Bye!")


def main():

    start(best_buy)


if __name__ == "__main__":
    main()





