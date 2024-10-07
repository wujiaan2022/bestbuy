from user_input import order_input
from active_inactive_list import get_active_list
from products import Product
from store import Store


# Function: Retrieves the order list from the user input and updates the product quantities
def get_order_list(store_object):
    """
    Retrieves the order list from the user by accepting product IDs and quantities.
    Updates the product stock and status in the store.

    Parameters:
    store_object (Store): An instance of the Store class containing the products.

    Returns:
    list: A list of tuples where each tuple contains a product and the quantity ordered.
    """
    order_list = []

    while True:
        # Get the product ID and quantity from user input
        order_id, order_quan = order_input(store_object)

        # If the user presses Enter without input, break the loop and return the order list
        if not order_id or not order_quan:
            return order_list

        # Get the active product list from the store
        active_list = get_active_list(store_object)

        # Check if valid order ID and quantity were entered
        for product in active_list:
            if str(order_id) == str(product[0]):  # Check if the product ID matches
                order_name = product[1]

                # Check if the product is already in the order list
                product_found = False

                for i, (p, q) in enumerate(order_list):
                    if p == order_name:
                        order_list[i] = (p, q + order_quan)  # Update the quantity
                        product_found = True
                        break  # Exit the loop once the product is found

                # If the product was not found, append it to the list
                if not product_found:
                    order_list.append((order_name, order_quan))

                # Reduce stock and update the product's stock status
                order_name.reduce_stock_deactivate(order_quan)
                updated_stock = order_name.get_stock_quan()

                print(f"The updated stock after purchasing is {updated_stock}")
                print("Product added to your shopping list!\n")
                break


# Function: Calculates the grand total of the products in the shopping list
def calc_grand_total(shopping_list, percent_off_promotion=None) -> float:
    """
    Calculates the grand total price of the products in the shopping list.
    Optionally applies a PercentOff promotion to the grand total.

    Parameters:
    shopping_list (list): A list of tuples where each tuple contains a product and the quantity ordered.
    percent_off_promotion (PercentOff, optional): An optional PercentOff promotion to apply to the grand total.

    Returns:
    float: The grand total price after applying the promotion (if any).
    """
    grand_total = 0

    # Sum up the total price for each product in the shopping list
    for product, quantity in shopping_list:
        grand_total += product.calc_each_total(int(quantity))

    return grand_total

