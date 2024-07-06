class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount_Price = 0

    def __str__(self):
        return f'Name: {self.name}\nPrice: {self.price}'

    def show_product(self):
        print(f'##Product Information##')
        print(f'Name: {self.name}')
        print(f'Price: {self.price}\n')

    def discount(self):
        discount = int(input(f'How much discount do you want to give to {self.name}? '))
        self.discount_Price = self.price - (self.price * (discount/100))
        print(f'\nThe price of {self.name} with {discount}% discount is {self.discount_Price}')


shampoo = Product('Shampoo', 10)
shampoo.show_product()
shampoo.discount()

