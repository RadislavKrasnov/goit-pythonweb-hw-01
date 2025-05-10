from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str) -> None:
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.region}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.region}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "(US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "(US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "(EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "(EU Spec)")


us_factory = USVehicleFactory()
vehicle_one = us_factory.create_car("Ford", "Mustang")
vehicle_one.start_engine()

vehicle_two = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle_two.start_engine()

eu_factory = EUVehicleFactory()
vehicle_three = eu_factory.create_car("Volkswagen", "Golf")
vehicle_three.start_engine()

vehicle_four = eu_factory.create_motorcycle("Ducati", "Monster")
vehicle_four.start_engine()
