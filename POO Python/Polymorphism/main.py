class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price

    def __str__(self):
        return f"{self._brand} {self._model_name} with price: {self._price}"

    @staticmethod
    def make_call(phone_number):
        print(f"Making a call for {phone_number}")

    def discount_price(self):
        return self._price * 0.10
class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera

    def discount_price(self):
        return self._price * 0.20


