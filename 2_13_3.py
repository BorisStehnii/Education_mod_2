class Product():

    def __init__(self, type_, name, price):
        self.type_ = type_
        self.name = name
        self.price = price
        self.amount_ = 0


class ProductStore():

    def __init__(self, name_market):
        self.name_market = name_market
        self.warehouse = dict()
        self.income = 0

    def add_product(self, new_product, amount):
        if new_product.name in self.warehouse:
            self.warehouse[new_product.name].amount_ += amount
        else:
            new_product.amount_ = amount
            self.warehouse.update({new_product.name: new_product})

    def set_discount(self, identifier, percent):
        discount = 0
        if identifier is self.warehouse:
            discount = self.warehouse[identifier].price * percent / 100
        else:
            for name in self.warehouse:
                if self.warehouse[name].type_ == identifier:
                    discount = self.warehouse[name].price * percent / 100
                    print(discount)
        return discount

    def sell_product(self, name_product_, amount):
        if self.warehouse[name_product_].amount_ < amount:
            raise ValueError("little product")
        else:
            discount = 0
            self.warehouse[name_product_].amount_ -= amount
            disc_ = input("Discount(E/n): ").lower()
            if disc_ == "e":
                identifier = input("Type identifier / name product: ")
                while True:
                    percent = input("Percent(30): ")
                    if percent.isdigit():
                        percent = int(percent)
                        break
                discount = self.set_discount(identifier, percent)
            self.income += (amount * self.warehouse[name_product_].price - amount*discount)

    def get_income(self):
        print(self.income)

    def get_all_products(self):
        for product_name in self.warehouse:
            print(f"{self.warehouse[product_name].type_} - {product_name}, price={self.warehouse[product_name].price},"
                  f" amount={self.warehouse[product_name].amount_}")

    def get_product_info(self, product_name):
        if product_name in self.warehouse:
            product_info = (product_name, self.warehouse[product_name].amount_)
        else:
            product_info = "There is no product"
        return product_info


def int_():
    while True:
        amount_products = input("product")
        if amount_products.isdigit():
            amount_products = int(amount_products)
            break
    return amount_products


if __name__ == '__main__':
    store = ProductStore("ATB")
    print("Add product: a, sell product: s\n get incom: i, all products: p\ninf product: j, exit: e")
    while True:
        command = input("command")
        if command.lower() == "a":
            type_product = input("type product: ")
            name_product = input("name product: ")
            print("price", end=" ")
            price_product = int_()
            print("amount", end=" ")
            amount_product = int_()
            product = Product(type_product, name_product, price_product)
            store.add_product(product, amount_product)
        elif command.lower() == "s":
            name_product = input("name product: ")
            print("amount", end=" ")
            amount_product = int_()
            store.sell_product(name_product, amount_product)
        elif command.lower() == "i":
            store.get_income()
        elif command.lower() == "p":
            store.get_all_products()
        elif command.lower() == "j":
            name_product = input("name product: ")
            print(store.get_product_info(name_product))
        elif command.lower() == "e":
            exit(0)

