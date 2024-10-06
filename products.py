class Product:
    def __init__(self, name, price, quantity):
        """
        Initializes a Product object with a name, price, quantity, and active status.

        Parameters:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.

        Raises:
        ValueError: If the name is empty, or price/quantity is negative.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        self.name = name

        if float(price) < 0:
            raise ValueError("Price cannot be negative.")
        self.price = float(price)

        if int(quantity) < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = int(quantity)

        # Update active status based on quantity
        self.active = self.quantity > 0

    # Define __str__ for a human-readable string representation
    def __str__(self):
        """
        Returns a human-readable string representation of the product.
        """
        return f"name={self.name}, price={self.price}, quantity={self.quantity}"

    # Define __repr__ for an unambiguous representation (typically used for debugging)
    def __repr__(self):
        """
        Returns an unambiguous string representation of the product, useful for debugging.
        """
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"

    def get_stock_quan(self) -> int:
        """
        Getter function for the quantity of the product.

        Returns:
        int: The current stock quantity of the product.
        """
        return int(self.quantity)

    def reduce_stock_deactivate(self, order_quan):
        """
        Reduces the stock by the specified order quantity and
        deactivates the product if the stock falls below or equals zero.

        Parameters:
        order_quan (int): The quantity to be subtracted from the product's stock.

        Raises:
        ValueError: If the order quantity is greater than available stock.
        """
        if order_quan > self.quantity:
            raise ValueError("Cannot order more than available quantity.")

        self.quantity -= order_quan

        if self.quantity <= 0:
            self.active = False

    def is_active(self) -> bool:
        """
        Checks if the product is active.

        Returns:
        bool: True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product by setting its active status to True.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product by setting its active status to False.
        """
        self.active = False

    def show(self) -> str:
        """
        Returns a formatted string displaying the product's details (name, price, quantity).

        Returns:
        str: The string containing the product's details.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def calc_each_total(self, order_quan):
        """
        Calculates the total price based on the order quantity for the product.

        Parameters:
        order_quan (int): The quantity of the product being ordered.

        Returns:
        float: The total price for the ordered quantity.
        """
        total_price = float(self.price) * int(order_quan)  # Calculate total cost for each product
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        # call the parent constructor with quantity set to 0.
        super().__init__(name, price, 0)

        # overwrite the status setting to make sure it is always active
        self.active = True

    # ignore any attempts to change quantity
    def set_quantity(self, quantity):
        pass

    def show(self):
        return f"Non-Stocked Product: {self.name}, Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return f"Limited Product: {self.name}, Price: {self.price}"


