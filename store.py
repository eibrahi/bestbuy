from products import Product

class Store:

    def __init__(self, products: list[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_all_products(self) -> list[Product]:
        result = []
        for product in self.products:
            if product.active:
                result.append(product)
        return result

    def order(self, shopping_list:list[tuple[Product, int]]) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            total += product.quantity

        return total
