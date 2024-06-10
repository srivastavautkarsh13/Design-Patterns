class ParkingLot:
    _instance = None

    def __new__(cls, total_spots: int):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls._instance._init(total_spots)
        return cls._instance

    def _init(self, total_spots: int):
        self.parking_spots = []
        for i in range(total_spots):
            if i % 3 == 0:
                self.parking_spots.append(ParkingSpotFactory.create_parking_spot(i, ParkingSpotType.TRUCK))
            elif i % 2 == 0:
                self.parking_spots.append(ParkingSpotFactory.create_parking_spot(i, ParkingSpotType.BIKE))
            else:
                self.parking_spots.append(ParkingSpotFactory.create_parking_spot(i, ParkingSpotType.CAR))

    def find_parking_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        for spot in self.parking_spots:
            if not spot.is_occupied and spot.spot_type.value == vehicle.vehicle_type.value:
                return spot
        return None

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        spot = self.find_parking_spot(vehicle)
        if spot and spot.park_vehicle(vehicle):
            print(f"Vehicle {vehicle.vehicle_number} parked at spot {spot.spot_id}.")
            return True
        print(f"No available spot for vehicle {vehicle.vehicle_number}.")
        return False

    def remove_vehicle(self, vehicle_number: str) -> bool:
        for spot in self.parking_spots:
            if spot.is_occupied and spot.vehicle.vehicle_number == vehicle_number:
                removed_vehicle = spot.remove_vehicle()
                print(f"Vehicle {removed_vehicle.vehicle_number} removed from spot {spot.spot_id}.")
                return True
        print(f"Vehicle {vehicle_number} not found.")
        return False

    def display_status(self):
        for spot in self.parking_spots:
            status = "Occupied" if spot.is_occupied else "Empty"
            vehicle_info = f" ({spot.vehicle.vehicle_number})" if spot.is_occupied else ""
            print(f"Spot {spot.spot_id} ({spot.spot_type.name}): {status}{vehicle_info}")

