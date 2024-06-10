from enum import Enum

class VehicleType(Enum):
    CAR = "Car"
    BIKE = "Bike"
    TRUCK = "Truck"

class Vehicle:
    def __init__(self, vehicle_number: str, vehicle_type: VehicleType):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_number: str, vehicle_type: VehicleType) -> Vehicle:
        return Vehicle(vehicle_number, vehicle_type)

