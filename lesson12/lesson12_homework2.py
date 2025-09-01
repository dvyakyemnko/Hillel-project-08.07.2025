class Item:
    name: str
    price: float
    description: str
    dimensions: str

    def __init__(self, name: str, price: float, description: str, dimensions: str) -> None:
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}"


class User:
    name: str
    surname: str
    numberphone: str

    def __init__(self, name: str, surname: str, numberphone: str) -> None:
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class Purchase:
    products: dict[Item, int]
    user: User

    def __init__(self, user: User) -> None:
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item: Item, cnt: int) -> None:
        self.products[item] = cnt

    def __str__(self) -> str:
        items = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
        return f"User: {self.user}\nItems:\n{items}"

    def get_total(self) -> float:
        return sum(item.price * cnt for item, cnt in self.products.items())


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
assert cart.get_total() == 40