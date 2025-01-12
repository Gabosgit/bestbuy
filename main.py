"""
"""
import products
import store

def start(store):
    print(f"\tStore Menu\n"
          f"\t----------")
    print(f"1. List all products in store\n"
          f"2. Show total amount in store\n"
          f"3. Make an order\n"
          f"4. Quit")

def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)

    start(store)


if __name__ == '__main__':
    main()
