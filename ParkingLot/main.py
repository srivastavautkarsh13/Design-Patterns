from parkingLot import ParkingLot
from spot import ParkingSpotSubject, ParkingSpotObserver
from vehicle import Vehicle, VehicleFactory, VehicleType
from gates import EntranceGate, ExitGate
from fee import HourlyFeeStrategy


class ParkingLotWithObserver(ParkingLot, ParkingSpotSubject):
    def __init__(self, total_spots: int):
        ParkingLot.__init__(self, total_spots)
        ParkingSpotSubject.__init__(self)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        spot = self.find_parking_spot(vehicle)
        if spot and spot.park_vehicle(vehicle):
            self.notify(spot)
            print(f"Vehicle {vehicle.vehicle_number} parked at spot {spot.spot_id}.")
            return True
        print(f"No available spot for vehicle {vehicle.vehicle_number}.")
        return False

    def remove_vehicle(self, vehicle_number: str) -> bool:
        for spot in self.parking_spots:
            if spot.is_occupied and spot.vehicle.vehicle_number == vehicle_number:
                removed_vehicle = spot.remove_vehicle()
                self.notify(spot)
                print(f"Vehicle {removed_vehicle.vehicle_number} removed from spot {spot.spot_id}.")
                return True
        print(f"Vehicle {vehicle_number} not found.")
        return False

# Example usage:
if __name__ == "__main__":
    parking_lot = ParkingLotWithObserver(10)
    observer = ParkingSpotObserver()
    parking_lot.attach(observer)
    
    vehicle1 = VehicleFactory.create_vehicle("KA-01-HH-1234", VehicleType.CAR)
    vehicle2 = VehicleFactory.create_vehicle("KA-01-HH-5678", VehicleType.BIKE)
    vehicle3 = VehicleFactory.create_vehicle("KA-01-HH-9101", VehicleType.TRUCK)
    
    entrance_gate = EntranceGate(1)
    ticket1 = entrance_gate.issue_ticket(vehicle1)
    ticket2 = entrance_gate.issue_ticket(vehicle2)
    ticket3 = entrance_gate.issue_ticket(vehicle3)
    
    parking_lot.park_vehicle(vehicle1)
    parking_lot.park_vehicle(vehicle2)
    parking_lot.park_vehicle(vehicle3)
    
    parking_lot.display_status()
    
    exit_gate = ExitGate(1)
    hourly_fee_strategy = HourlyFeeStrategy(10)
    
    parking_lot.remove_vehicle(vehicle1.vehicle_number)
    ticket1.mark_exit()
    fee1 = exit_gate.process_ticket(ticket1, hourly_fee_strategy)
    print(f"Fee for vehicle {vehicle1.vehicle_number}: {fee1}")
    
    parking_lot.display_status()

