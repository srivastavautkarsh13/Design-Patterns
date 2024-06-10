from vehicle import Vehicle
from ticket import Ticket

class EntranceGate:
    def __init__(self, gate_id: int):
        self.gate_id = gate_id

    def issue_ticket(self, vehicle: Vehicle) -> Ticket:
        return Ticket(vehicle)

class ExitGate:
    def __init__(self, gate_id: int):
        self.gate_id = gate_id

    def process_ticket(self, ticket: Ticket, fee_strategy):
        ticket.mark_exit()
        ticket.calculate_fee(fee_strategy)
        return ticket.fee

