from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, region):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} {self.region}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} {self.region}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model, region):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model, region):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model, region):
        return Car(make, model, region)

    def create_motorcycle(self, make, model, region):
        return Motorcycle(make, model, region)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model, region):
        return Car(make, model, region)

    def create_motorcycle(self, make, model, region):
        return Motorcycle(make, model, region)


us_factory = USVehicleFactory()
vehicle_one = us_factory.create_car("Ford", "Mustang", "(US Spec)")
vehicle_one.start_engine()

vehicle_two = us_factory.create_motorcycle("Harley-Davidson", "Sportster", "(US Spec)")
vehicle_two.start_engine()

eu_factory = EUVehicleFactory()
vehicle_three = eu_factory.create_car("Volkswagen", "Golf", "(EU Spec)")
vehicle_three.start_engine()

vehicle_four = eu_factory.create_motorcycle("Ducati", "Monster", "(EU Spec)")
vehicle_four.start_engine()
