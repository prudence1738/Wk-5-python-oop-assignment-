# Parent class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # encapsulated private attribute

    def show_info(self):
        print(f"{self.brand} {self.model}, Battery: {self.__battery}%")

    def charge(self, amount):
        self.__battery += amount
        if self.__battery > 100:
            self.__battery = 100
        print(f"Charging... Battery is now {self.__battery}%")

# Child class: Smartwatch inherits from Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery, heart_rate):
        super().__init__(brand, model, battery)
        self.heart_rate = heart_rate

    # Overriding method (polymorphism)
    def show_info(self):
        print(f"{self.brand} {self.model}, Battery: {self._Smartphone__battery}%, Heart Rate: {self.heart_rate} bpm")

# Testing
phone = Smartphone("Samsung", "A25", 80)
phone.show_info()
phone.charge(15)

watch = Smartwatch("Samsung", "Galaxy Watch", 60, 72)
watch.show_info()
