from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Muss von jeder Unterklasse implementiert werden."""
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        # Jeder zweite Artikel kostet die Hälfte
        full_price_items = (quantity // 2) + (quantity % 2)
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        # Kauf 3, zahl 2 (Jeder dritte ist gratis)
        chargeable_items = quantity - (quantity // 3)
        return float(chargeable_items * product.price)