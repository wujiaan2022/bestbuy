import pytest
from products import Product


# Test that creating a normal product works
def test_create_normal_product():
    product = Product(name="Laptop", price=1000, quantity=10)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 10
    assert product.active is True  # This remains since 'active' defaults to True


# Test that creating a product with invalid details (empty name, negative price) invokes an exception
def test_create_product_invalid_details():
    with pytest.raises(ValueError):
        Product(name="", price=1000, quantity=10)

    with pytest.raises(ValueError):
        Product(name="Phone", price=-500, quantity=5)


# Test that when a product reaches 0 quantity, it becomes inactive
def test_product_becomes_inactive_reduce():
    product = Product(name="Tablet", price=500, quantity=10)  # Start with a quantity greater than 0
    product.reduce_stock_deactivate(10)  # Reduce stock to 0
    assert product.active is False  # Product should now be inactive


# Test that when a product quantity is initialized as 0, it becomes inactive
def test_product_becomes_inactive_initialize():
    product = Product(name="Tablet", price=500, quantity=0)  # Start with a quantity greater than 0
    assert product.active is False  # Product should now be inactive


# Test that product purchase modifies the quantity and returns the correct output
def test_purchase_modifies_quantity():
    product = Product(name="Headphones", price=100, quantity=10)
    product.reduce_stock_deactivate(3)
    assert product.quantity == 7


# Test that buying a larger quantity than exists invokes an exception
def test_buy_larger_quantity_than_exists():
    product = Product(name="TV", price=1500, quantity=5)

    with pytest.raises(ValueError):
        product.reduce_stock_deactivate(10)


