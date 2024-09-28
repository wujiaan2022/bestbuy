import products


class Store:
    def __init__(self, products=None):
        self.products = products if products else []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:

        total_quantity =  0
        for product in self.products:
            total_quantity += product.quantity

        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        """Returns all products in the store that are active."""

        active_products = []
        for product in self.products:
            if product.is_active():  # Using the is_active() method to check activity
                active_products.append(product)  # Append the product object itself
        return active_products

    def order(self, shopping_list) -> float:

        total_price = 0

        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                total_price += product.buy(quantity)

        return total_price












