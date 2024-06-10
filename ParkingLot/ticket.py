import uuid
from datetime import datetime
from vehicle import Vehicle

class Ticket:
    def __init__(self, vehicle: Vehicle):
        self.ticket_id = uuid.uuid4()
        self.vehicle = vehicle
        self.entry_time = datetime.now()
        self.exit_time = None
        self.fee = 0

    def mark_exit(self):
        self.exit_time = datetime.now()

    def calculate_fee(self, fee_strategy):
        self.fee = fee_strategy.calculate_fee(self.entry_time, self.exit_time)

