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

    def get_quantity(self) -> int:
        """Getter function for quantity, returns the quantity as a float."""
        return int(self.quantity)

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity

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

    def buy(self, quantity) -> int:
        """Handles purchasing of a product. Decreases quantity and returns total cost."""
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")

        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity  # Calculate total cost of the purchase

        self.set_quantity(self.quantity - quantity)  # Use set_quantity to adjust and potentially deactivate

        return total_price




