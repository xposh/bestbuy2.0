
from products import Product

#Specification
#The Store class will contain one variable - a list of products that exist in the store.
class Store:


    def __init__(self, products):
        #products: list[Product]
        self.products = products
# It will expose the following methods:
#add_product(self, product)
#Example:
#bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
#mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    def add_product(self, product):
        self.products.append(product)

    def get_total_quantity(self):# -> int
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total
    # Returns how many items are in the store in total.

    def get_all_products(self):  # -> List[Product]
        active_products = []
        for product in self.products:
            if product.is_active():
                (active_products.append(product))
        return active_products
    # Returns all products in the store that are active.

    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
    #Gets a list of tuples, where each tupl has 2 items:


# instance of a store

# --------- TEST CODE ---------

if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))