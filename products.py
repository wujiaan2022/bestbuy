from promotions import Promotion, SecondHalfPrice, ThirdOneFree, PercentDiscount


class Product:
    """
        The Product class represents a product with a name, price, and a promotion (optional).
        """
    def __init__(self, name, price, quantity, **kwargs):
        """
        Initializes a Product object with a name, price, quantity, active status, and promotion.

        Parameters:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.

        Raises:
        ValueError: If the name is empty, or price/quantity is negative.
        """
        try:
            if kwargs:
                raise TypeError

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

            # Promotion is initially None (no promotion applied)
            self.promotion = None

        except TypeError:
            print(f"Failed to add product {name} due to invalid arguments.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            print("Can not change name to an empty name.")
        else:
            self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        try:
            if float(new_price) < 0:
                raise ValueError
            self._price = float(new_price)
        except ValueError:
            print("Price cannot be negative.")

    # Define __str__ for a human-readable string representation
    def __str__(self):
        """
        String representation of the product, showing the name, price, and promotion (if any).

        Returns:
        str: String representation of the product.
        """
        promotion_name = f" with {self.promotion}" if self.promotion else " (No promotion)"
        return f"Product: {self.name}, Price: {self.price}{promotion_name}"

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

        # Getter for the promotion
    def get_promotion(self):
        """
        Get the current promotion applied to the product.

        Returns:
        Promotion: The promotion object applied to the product, or None if no promotion is applied.
        """
        return self.promotion

    def set_promotion(self, promotion):
        """
        Set or update the promotion for the product.

        Parameters:
        promotion (Promotion): A Promotion object to apply to the product.
        """
        self.promotion = promotion

    # def show(self) -> str:
    #     """
    #     Calls the __str__ method to provide the same output.
    #     """
    #     return str(self)  # Calls __str__ internally

    def calc_each_total(self, order_quan):
        """
        Calculate the total price of the product, applying any active promotion.

        Parameters:
        quantity (int): The quantity of the product being purchased.

        Returns:
        float: The total price after applying the promotion (if any).
        """
        total_price = float(self.price) * int(order_quan)  # Calculate total cost for each product

        if self.promotion:
            total_price = self.promotion.apply(total_price, order_quan)

        return total_price

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented


class NonStockedProduct(Product):
    def __init__(self, name, price):
        # call the parent constructor with quantity set to 0.
        super().__init__(name, price, quantity=10000)

        # overwrite the status setting to make sure it is always active
        self.active = True

    # ignore any attempts to change quantity
    def set_quantity(self, quantity):
        pass

    def __str__(self):
        """
        String representation of the product, showing the name, price, and promotion (if any).

        Returns:
        str: String representation of the product.
        """
        promotion_name = f" with {self.promotion}" if self.promotion else " (No promotion)"
        return f"Non-Stocked Product: {self.name}, Price: {self.price}{promotion_name}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self):
        return f"Limited Product: {self.name}, Price: {self.price}"


