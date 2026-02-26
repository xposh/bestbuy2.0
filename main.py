from products import Product
from store import Store


# setup initial stock of inventory
def stock_of_inventory():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    return Store(product_list)


def list_products(best_buy):
    products = best_buy.get_all_products()

    print("------")
    number = 1
    for product in products:
        print(f"{number}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
        number += 1
    print("------")

    return products


def start(best_buy):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_input = input("Please choose a number: ").strip()

        if user_input == "1":
            list_products(best_buy)

        elif user_input == "2":
            total = best_buy.get_total_quantity()
            print(f"Total of {total} items in store")

        elif user_input == "3":
            products = list_products(best_buy)
            print("When you want to finish order, enter empty text.")

            shopping_list = []  # list of tuples: (Product, quantity)

            while True:
                product_choice = input("Which product # do you want? ").strip()
                if product_choice == "":
                    break

                if not product_choice.isdigit():
                    print("Error adding product!\n")
                    continue

                product_number = int(product_choice)

                if product_number < 1 or product_number > len(products):
                    print("Error adding product!\n")
                    continue

                chosen_product = products[product_number - 1]

                amount_text = input("What amount do you want? ").strip()

                if not amount_text.isdigit():
                    print("Error adding product!\n")
                    continue

                amount = int(amount_text)

                if amount <= 0:
                    print("Error adding product!\n")
                    continue

                # Prevent ordering more than available when same product is added multiple times
                already_requested = 0
                for product, qty in shopping_list:
                    if product is chosen_product:
                        already_requested += qty

                available_left = chosen_product.get_quantity() - already_requested
                if amount > available_left:
                    print("Error adding product!\n")
                    continue

                shopping_list.append((chosen_product, amount))
                print("Product added to list!\n")

            if shopping_list:
                try:
                    total_price = best_buy.order(shopping_list)
                    print(f"Order cost: {total_price} dollars.")
                except Exception:
                    print("Error adding product!\n")

        elif user_input == "4":
            break

        else:
            continue


if __name__ == "__main__":
    best_buy = stock_of_inventory()
    start(best_buy)