import products


# The Store class manages a collection of products, allowing for adding, removing, and querying product information.
class Store:
    def __init__(self, products_lis=None):
        """
        Initializes the Store with a list of products.

        Parameters:
        products (list): A list of Product objects. If not provided, an empty list is initialized.
        """
        self.products_lis = products_lis if products_lis else []

    # Function: Adds a product to the store's product list
    def add_product(self, product):
        """
        Adds a product to the store's list of products.

        Parameters:
        product (Product): An instance of the Product class to be added to the store.
        """
        self.products_lis.append(product)

    # Function: Removes a product from the store's product list
    def remove_product(self, product):
        """
        Removes a product from the store's list of products.

        Parameters:
        product (Product): An instance of the Product class to be removed from the store.
        """
        self.products_lis.remove(product)

    # Function: Returns the total quantity of all products in the store
    def get_total_quantity(self) -> int:
        """
        Calculates and returns the total quantity of all products in the store.

        Returns:
        int: The total quantity of all products combined.
        """
        total_quantity = 0
        for product in self.products_lis:
            total_quantity += product.quantity

        return total_quantity

    # Function: Returns a list of all active products in the store
    def get_active_products(self):
        """
        Returns all active products in the store.

        Returns:
        list: A list of Product objects that are currently active.
        """
        active_products = [product for product in self.products_lis if product.is_active()]
        return active_products

    # Function: Returns a list of all inactive products in the store
    def get_inactive_products(self):
        """
        Returns all inactive products in the store.

        Returns:
        list: A list of Product objects that are currently inactive.
        """
        inactive_products = [product for product in self.products_lis if not product.is_active()]
        return inactive_products




