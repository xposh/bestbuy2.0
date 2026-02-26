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
        # LOGIK-FIX: Hier wird geprüft, bevor das Objekt im RAM belegt wird
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    # Getter function for quantity.
    # Returns the quantity (int).
    def get_quantity(self):
        return int(self.quantity)

    # Setter function for quantity.
    # If quantity reaches 0, deactivates the product.
    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False
        else:
            self.active = True

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
        # ARCHITEKTUR-HINWEIS: Für f-strings in Tests nutzen wir return oder print
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    # Buys a given quantity of the product.
    # Returns the total price (float) of the purchase.
    # Updates the quantity of the product.
    # In case of a problem, raises an Exception.
    def buy(self, quantity):  # float
        if not self.active:
            raise ValueError("Product is not active")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if quantity > self.quantity:
            # GEÄNDERT: ValueError statt Exception, passend zum pytest.raises im Test
            raise ValueError("Not enough quantity in stock")

        total_price = float(quantity * self.price)
        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return total_price


class NonStockedProduct(Product):
    """
    Subklasse für digitale Produkte ohne Lagerbestand.
    Die Menge ist fest auf 0 fixiert.
    """

    def __init__(self, name, price):
        # Nutzt den Konstruktor der Elternklasse, setzt quantity aber fest auf 0
        super().__init__(name, price, quantity=0)

    def show(self):
        # Überschreibt die Anzeige: Keine Mengenangabe sinnvoll
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited"

    def buy(self, quantity):
        # Logik-Anpassung: Digitale Produkte können immer gekauft werden,
        # solange sie aktiv sind. Die Menge im Lager reduziert sich nicht.
        if not self.active:
            raise ValueError("Product is not active")

        return float(quantity * self.price)


class LimitedProduct(Product):
    """
    Subklasse für Produkte mit einer maximalen Bestellmenge pro Kauf (z.B. Versand).
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        # Zeigt das zusätzliche Limit in der Beschreibung an
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Limited to {self.maximum} per order"

    def buy(self, quantity):
        # ARCHITEKTUR-CHECK: Erst das Limit prüfen, dann die Lagerlogik der Elternklasse
        if quantity > self.maximum:
            raise ValueError(f"Order quantity exceeds maximum limit of {self.maximum}")

        # Nutzt die bestehende Logik von Product.buy() für die Bestandsreduzierung
        return super().buy(quantity)

# ---------- TEST CODE ----------

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    # bose.show() gibt jetzt den String zurück
    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())