import random
from Customer import Customer
from SimulationClock import SimulationClock
from EventQueue import EventQueue
from SystemState import SystemState
from StatisticalCounters import StatisticalCounter


class Event:
    arrival = 0
    departure = float('inf')

    def __init__(self, finish_event_id, at_a, at_b, st_a, st_b):
        self._at_a = at_a
        self._at_b = at_b
        self._st_a = st_a
        self._st_b = st_b
        self._clock = SimulationClock.instance
        self._finish_event_id = finish_event_id
        self.i = 0
        self._c_id = 0
        self.event_queue = EventQueue()
        self.predict_next_arrival_time()

    def get_finish_event_id(self):
        return self._finish_event_id

    def predict_next_arrival_time(self):
        if Event.arrival >= Event.departure:
            return
        Event.arrival += [0.4, 1.2, 0.5, 1.7, 0.2, 1.6, 0.2, 1.4, 1.9][self.i]
        # Event.arrival = round(random.uniform(self._at_a, self._at_b), 1)

    def get_next(self):
        if not self.event_queue.is_empty() and SystemState.server_status == 0:
            customer = self.event_queue.pop()
            SystemState.number_in_queue -= 1
            StatisticalCounter.total_delay += self._clock.get_time() - customer.get_arrival_time()
            return customer
        # service_time = round(random.uniform(self._st_a, self._st_b), 1)
        service_time = [2.0, 0.7, 0.2, 1.1, 3.7, 0.6, 1, 1, 1][self.i]
        customer = Customer(Event.arrival, service_time, self._c_id)
        self._c_id += 1
        self.i += 1
        self._clock.set_time(Event.arrival)
        self.predict_next_arrival_time()
        if self.i <= self._finish_event_id:
            StatisticalCounter.total_service_times += customer.get_service_time()
        return customer

    def get_last_generated_id(self):
        return self._c_id

    def has_next(self):
        if self._c_id == self._finish_event_id - 1:
            return False
        return True
