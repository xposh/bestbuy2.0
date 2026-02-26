import pytest
from products import Product


# 1. Test: Normales Produkt erstellen (ERFÜLLT)
def test_creating_product():
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    assert prod.name == "MacBook Air M2"
    assert prod.price == 1450
    assert prod.quantity == 100
    assert prod.is_active() is True


# 2. Test: Ungültige Details (Name leer, Preis negativ)
def test_creating_product_invalid_details():
    # Testet leeren Namen
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)

    # Testet negativen Preis
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


# 3. Test: Wenn Menge 0 erreicht wird, wird es inaktiv
def test_product_reaches_zero_quantity():
    prod = Product("MacBook Air M2", price=1450, quantity=1)
    prod.buy(1)  # Menge auf 0 setzen
    assert prod.quantity == 0
    assert prod.is_active() is False


# 4. Test: Kauf modifiziert Menge und gibt richtigen Output (Gesamtpreis)
def test_product_purchase_modifies_quantity():
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = prod.buy(10)
    assert prod.quantity == 90
    assert total_price == 14500  # 10 * 1450


# 5. Test: Kauf von mehr als vorhanden ist (Exception)
def test_buy_larger_quantity_than_exists():
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        prod.buy(200)  # 200 ist > 100 im Lager