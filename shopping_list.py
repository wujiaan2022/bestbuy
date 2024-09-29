from user_input import order_input
from active_inactive_list import get_active_list
from products import Product
from store import Store


def get_order_list(store_object):
    order_list = []

    while True:
        order_id, order_quan = order_input(store_object)  # Get the product ID and quantity
        print(f"\nDEBUG---The order_id and order_quan in get_order_list: {order_id}, {order_quan}")
        # If the user presses Enter without input, break the loop and return the order list
        if not order_id or not order_quan:
            return order_list

        active_list = get_active_list(store_object)  # Get the active product list from the store

        # Check if valid order ID and quantity were entered
        for product in active_list:

            print(f"DEBUG---for product in active_list in get_order_list: {product}")

            if str(order_id) == str(product[0]):  # Check if the product ID matches
                order_name = product[1]

                # Check if the product is already in the order list
                product_found = False

                for i, (p, q) in enumerate(order_list):
                    if p == order_name:
                        order_list[i] = (p, q + order_quan)  # Update the quantity
                        product_found = True
                        break  # Exit the loop once the product is found

                # If the product was not found, append it outside the loop
                if not product_found:
                    order_list.append((order_name, order_quan))

                # Reduce stock and update the product's stock status
                order_name.reduce_stock_deactivate(order_quan)
                updated_stock = order_name.get_stock_quan()

                print(f"The updated stock after purchasing is {updated_stock}")
                print("Product added to your shopping list!\n")
                break


def calc_grant_total(shopping_list) -> float:

    grant_total = 0

    for product, quantity in shopping_list:
        grant_total += product.calc_each_total(int(quantity))

    return grant_total

