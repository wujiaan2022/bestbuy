from abc import ABC, abstractmethod


# Abstract base class for all promotions
class Promotion(ABC):
    """
    The Promotion abstract class serves as a blueprint for different types of promotions.
    Subclasses must implement the `apply` method to handle how the promotion is applied.

    Attributes:
        name (str): The name of the promotion.
    """

    def __init__(self, name):
        """
        Initialize the promotion with a name.

        Parameters:
        name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply(self, total_price, order_quan):
        """
        Abstract method to apply the promotion. This must be overridden in subclasses.

        Parameters:
        total_price (float): The total price of the product(s).
        order_quan (int): The quantity of the product(s) in the order.

        Returns:
        float: The modified total price after the promotion is applied.
        """
        pass

    def __str__(self):
        """
        Return a string representation of the promotion.

        Returns:
        str: The name of the promotion.
        """
        return f"Promotion: {self.name}"


# Subclass for "Second Half Price" promotion
class SecondHalfPrice(Promotion):
    """
    A promotion where the second product is half-price if the quantity is 2 or more.
    """

    def apply(self, total_price, order_quan):
        """
        Apply the "Second Half Price" promotion.

        If the order contains two or more items, the second item will be half-priced.

        Parameters:
        total_price (float): The total price of the products.
        order_quan (int): The quantity of the product(s) in the order.

        Returns:
        float: The new total price after applying the promotion.
        """
        if order_quan >= 2:
            discount = total_price / order_quan / 2  # Half-price for the second item
            total_price -= discount
        return total_price


# Subclass for "Third One Free" promotion
class ThirdOneFree(Promotion):
    """
    A promotion where the third item is free if the quantity is 3 or more.
    """

    def apply(self, total_price, order_quan):
        """
        Apply the "Third One Free" promotion.

        If the order contains three or more items, the third one will be free.

        Parameters:
        total_price (float): The total price of the products.
        order_quan (int): The quantity of the product(s) in the order.

        Returns:
        float: The new total price after applying the promotion.
        """
        if order_quan >= 3:
            discount = total_price / order_quan  # Full discount for the third item
            total_price -= discount
        return total_price


# Subclass for percentage discount promotion
class PercentDiscount(Promotion):
    """
    A promotion where a percentage discount is applied to the grand total if a certain threshold is exceeded.
    """

    def __init__(self, name, percent):
        """
        Initialize the PercentOff promotion with a name, discount percentage, and an exceed limit.

        Parameters:
        name (str): The name of the promotion.
        percent (float): The percentage discount to apply.
        exceed_limit (float): The threshold above which the promotion is applied.
        """
        super().__init__(name)
        self.percent = percent

    def apply(self, total_price, order_quan):
        """
        Apply the percentage discount promotion if the grand total exceeds the set limit.

        Parameters:
        grand_total (float): The total price of all products in the order.
        order_quan (int): The quantity of the product(s) in the order (unused here but needed for signature consistency).

        Returns:
        float: The new grand total after applying the percentage discount, if applicable.
        """

        discount = total_price * self.percent / 100  # Calculate the percentage discount
        total_price -= discount
        return total_price

