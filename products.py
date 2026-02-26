"""Step 1 - Product Class
The Product class represents a specific type of product available in the store (For example, MacBook Air M2).
It encapsulates information about the product, including its name and price.
Additionally, the Product class includes an attribute to keep track of the total quantity of items of that product
currently available in the store. When someone will purchase it, the amount will be modified accordingly.
"""


class Product:
    """Initiator (constructor) method.
    Creates the instance variables (active is set to True).
    If something is invalid (empty name / negative price or quantity), raises an exception.
    ❓ Don’t remember how to raise an exception? Search online or go back to Exceptions lesson in previous Units.
    """

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    # Getter function for quantity.
    # Returns the quantity (int).
    def get_quantity(self):
        return self.quantity

    # Setter function for quantity.
    # If quantity reaches 0, deactivates the product.
    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity == 0:
            self.active = False

    # Getter function for active.
    # Returns True if the product is active, otherwise False.
    def is_active(self):
        return self.active

    # Activates the product.
    def activate(self):
        self.active = True

    # Deactivates the product.
    def deactivate(self):
        self.active = False

    # Prints a string that represents the product.
    # Example:
    # "MacBook Air M2, Price: 1450, Quantity: 100"
    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    # Buys a given quantity of the product.
    # Returns the total price (float) of the purchase.
    # Updates the quantity of the product.
    # In case of a problem, raises an Exception.
    def buy(self, quantity):  # float
        if not self.active:
            raise Exception("Product is not active")

        if quantity <= 0:
            raise Exception("Quantity must be greater than zero")

        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock")

        total_price = quantity * self.price
        self.quantity = self.quantity - quantity

        if self.quantity == 0:
            self.active = False

        return total_price


# ---------- TEST CODE ----------

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
