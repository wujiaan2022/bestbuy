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
    def get_active_list(self):

        active_list = []
        active_products = [product for product in self.products_lis if product.is_active()]
        for i, product in enumerate(active_products, start=1):
            active_list.append((i, product))
        return active_list

    def print_active_list(self):
        active_list = self.get_active_list()
        if not active_list:
            print("No active product available.")
        else:
            for i, product in active_list:  # Unpack the tuple (i, product)
                print(f"{i}. {product}")  # Now this will call product.__str__()

    # Function: Returns a list of all inactive products in the store
    def get_inactive_list(self):

        inactive_list = []
        inactive_products = [product for product in self.products_lis if not product.is_active()]
        for i, product in enumerate(inactive_products, start=1):
            inactive_list.append((i, product))
        return inactive_list




