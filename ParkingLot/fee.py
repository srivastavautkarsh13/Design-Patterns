from abc import ABC, abstractmethod
from datetime import datetime

class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, entry_time: datetime, exit_time: datetime) -> float:
        pass

class HourlyFeeStrategy(FeeStrategy):
    def __init__(self, hourly_rate: float):
        self.hourly_rate = hourly_rate

    def calculate_fee(self, entry_time: datetime, exit_time: datetime) -> float:
        duration = exit_time - entry_time
        hours = duration.total_seconds() / 3600
        return hours * self.hourly_rate

