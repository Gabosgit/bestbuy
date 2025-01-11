class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if name == "":
            raise Exception("The name of the product is empty")

        if price < 0:
            raise Exception("The price can't be negative")

        if quantity < 0:
            raise Exception("The quantity can't be negative")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, buy_quantity):
        if buy_quantity > self.quantity:
            raise Exception("Not enough Quantity in stock")

        if buy_quantity < 1:
            raise Exception("Quantity must be a positive number and at least 1")

        total_price = self.price * buy_quantity
        self.quantity = self.quantity - buy_quantity

        return total_price
