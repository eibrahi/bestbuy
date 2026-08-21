class Product:

    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Product name cannot be empty")

        if price < 0:
            raise ValueError("Product price cannot be negative")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def show(self) -> None:
        print("Name: " + self.name)
        print("Price: " + str(self.price))
        print("Quantity: " + str(self.quantity))

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity cannot be negative")

        if quantity > self.quantity:
            raise ValueError("Quantity cannot be greater than the product's quantity")

        if not self.active:
            raise ValueError("Product is not active")

        self.quantity += quantity
        return quantity * self.price




