import products
import store


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


def start(store_object):

    menu = {
        "1": "List all products in store",
        "2": "Show total amount in store",
        "3": "Make an order",
        "4": "Quit"
    }

    title = "Store Menu"
    dash_line = "-" * len(title)
    print(title)
    print(dash_line)

    for key, value in menu.items():
        print(f"{key}. {value}")