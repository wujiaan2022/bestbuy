class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty.")
        self.name = name

        if float(price) < 0:
            raise ValueError("Price cannot be negative.")
        self.price = float(price)

        if float(quantity) < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = float(quantity)

        self.active = True

    def get_quantity(self) -> float:
        """Getter function for quantity, returns the quantity as a float."""
        return float(self.quantity)

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """Getter function for active. Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """Handles purchasing of a product. Decreases quantity and returns total cost."""

        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity  # Calculate total cost of the purchase

        self.set_quantity(quantity)  # Reduce the quantity after calculating total price

        return total_price




