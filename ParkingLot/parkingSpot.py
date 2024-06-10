class ParkingSpotType(Enum):
    CAR = "Car"
    BIKE = "Bike"
    TRUCK = "Truck"

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: ParkingSpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = False
        self.vehicle = None

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if self.is_occupied or self.spot_type.value != vehicle.vehicle_type.value:
            return False
        self.vehicle = vehicle
        self.is_occupied = True
        return True

    def remove_vehicle(self) -> Vehicle:
        if not self.is_occupied:
            return None
        vehicle = self.vehicle
        self.vehicle = None
        self.is_occupied = False
        return vehicle

class ParkingSpotFactory:
    @staticmethod
    def create_parking_spot(spot_id: int, spot_type: ParkingSpotType) -> ParkingSpot:
        return ParkingSpot(spot_id, spot_type)

