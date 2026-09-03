cart = {}


def add_product(name, price):

    cart[name] = price
    print("Product added")


def remove_product(name):

    if name in cart:
        del cart[name]
        print("Product removed")

    else:
        print("Product not found")


def calculate_total():

    return sum(cart.values())


def display_cart():

    if len(cart) == 0:

        print("Cart is empty")

    else:

        print("\n===== YOUR CART =====")

        for name, price in cart.items():
            print(name, ":", price)

        print("Total:", calculate_total())