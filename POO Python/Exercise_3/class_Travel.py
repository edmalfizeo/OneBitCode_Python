class Travel:
    def __init__(self, destination=None, price=None, duration=None, transport=None):
        self.destination = destination
        self.price = price
        self.duration = duration
        self.transport = transport

    def __str__(self):
        return f"Destination: {self.destination}\nPrice: {self.price}\nDuration: {self.duration}\nTransport: {self.transport}"

    @staticmethod
    def get_places():
        return ["Paris", "London", "Madrid", "Berlin", "Rome", "Amsterdam", "Prague", "Vienna", "Budapest", "Lisbon"]

    @staticmethod
    def get_transports():
        return ["Plane", "Train", "Car", "Bus"]

    @staticmethod
    def get_prices():
        price_bus = [3400, 3100, 2000, 2500, 4500, 1600, 700, 2800, 1900, 4000]
        price_car = [5000, 4500, 3000, 3500, 5500, 2500, 1200, 4000, 3000, 5000]
        price_plane = [7000, 6500, 5000, 5500, 7500, 4500, 3200, 6000, 5000, 7000]
        price_train = [6000, 5500, 4000, 4500, 6500, 3500, 2200, 5000, 4000, 6000]
        return price_bus, price_car, price_plane, price_train

    def buy_ticket(self, destination, duration, transport):
        places = self.get_places()
        transports = self.get_transports()
        prices = self.get_prices()

        if destination not in places:
            raise ValueError("Invalid destination")
        if transport not in transports:
            raise ValueError("Invalid transport")

        choosen_destination = places.index(destination)

        self.destination = destination
        self.duration = duration
        self.transport = transport

        if transport == "Bus":
            self.price = prices[0][choosen_destination]
        elif transport == "Car":
            self.price = prices[1][choosen_destination]
        elif transport == "Plane":
            self.price = prices[2][choosen_destination]
        elif transport == "Train":
            self.price = prices[3][choosen_destination]








