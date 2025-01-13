"""
    This module manages the list of products in the store.
"""
import products

class Store:
    """ Creates a store by starting it with a list of products """
    def __init__(self, products_list):
        self.products_list = products_list


    def add_product(self, product):
        """ Allows to add a product to the product list """
        self.products_list.append(product)


    def remove_product(self, product):
        """ Allows to remove a product from the product list """
        self.products_list.remove(product)


    def get_total_quantity(self):
        """ Prints the total of products in the store """
        total_quantity = 0
        for product in self.products_list:
            total_quantity += product.quantity
        print(f"\nTotal of {total_quantity} items in store\n")


    def get_all_products(self):
        """
            Check if the product is active.
            If it is not active it removes it from the products list to not show it and not count it as a purchase option.
            Prints a numbered list of products
        """
        print()
        for product in self.products_list:
            if not product.is_active():
                self.remove_product(product)

        for index, product in enumerate(self.products_list):
            if not product.is_active():
                self.remove_product(product)
            elif product.is_active():
                print(f"{index+1}. {product.show()}")
        print()


    def order(self, shopping_list):
        """ Gets a list of tuples from the user. Each tuple contains the product index and the quantity of this product to order.
            Returns the total price for the entire purchase
        """
        total_order = 0
        for product, quantity in shopping_list:
            total_product_price = product.buy(quantity) # Product price * quantity
            total_order = total_order + total_product_price # Result of all products purchased
        return total_order


def main():
    pass


if __name__ == '__main__':
    main()
