import products

class Store:
    def __init__(self, products_list):
        self.products_list = products_list

    def add_product(self, product):
        self.products_list.append(product)

    def remove_product(self, product):
        self.products_list.remove(product)

    def get_total_quantity(self):
        return len(self.products_list)

    def get_all_products(self):
        for product in self.products_list:
            if product.is_active():
                print(product.show())

    def order(self, shopping_list):
        self.products_list = shopping_list
        total_order = 0

        for product, quantity in shopping_list:
            total_product_price = product.buy(quantity) # Product price * quantity
            total_order = total_order + total_product_price # Result of all products purchased

        return total_order


def main():
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    store = Store([bose, mac])
    print(store.products_list)

    print()

    pixel = products.Product("Google Pixel 7", price=500, quantity=250)
    store.add_product(pixel)

    print()
    print(store.products_list)

    print()

    store.remove_product(bose)
    print(store.products_list)

    print(store.get_total_quantity())

    #mac.deactivate()
    store.add_product(bose)

    print()
    store.get_all_products()
    print()

    price = store.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")




if __name__ == '__main__':
    main()
