class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty.")
        self.name = name

        if float(price) < 0:
            raise ValueError("Price cannot be negative.")
        self.price = float(price)

        if int(quantity) < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = int(quantity)

        self.active = True

    # Define __str__ for a human-readable string representation
    def __str__(self):
        return f"name={self.name}, price={self.price}, quantity={self.quantity}"

    # Define __repr__ for an unambiguous representation (typically used for debugging)
    def __repr__(self):
        return f"name={self.name}, price={self.price}, quantity={self.quantity}"

    def get_stock_quan(self) -> int:
        """Getter function for quantity, returns the quantity as a float."""
        return int(self.quantity)

    def reduce_stock_deactivate(self, order_quan):

        self.quantity -= order_quan

        if self.quantity <= 0:
            self.active = False

    def is_active(self) -> bool:
        """Getter function for active. Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        """Returns a string representing the product details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def calc_each_total(self, order_quan):

        total_price = float(self.price) * int(order_quan)  # Calculate total cost for each product

        return total_price






