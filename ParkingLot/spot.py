class Observer(ABC):
    @abstractmethod
    def update(self, parking_spot: ParkingSpot):
        pass

class ParkingSpotObserver(Observer):
    def update(self, parking_spot: ParkingSpot):
        status = "Occupied" if parking_spot.is_occupied else "Empty"
        print(f"Parking spot {parking_spot.spot_id} is now {status}.")

class ParkingSpotSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, parking_spot: ParkingSpot):
        for observer in self._observers:
            observer.update(parking_spot)

