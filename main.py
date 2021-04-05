__version__ = "1.0.0"
__author__ = "Mohammad Siavashi"
__title__ = "Discrete event simulation"

from Report import Report
from Event import Event
from SimulationClock import SimulationClock
from SystemState import SystemState
from StatisticalCounters import StatisticalCounter


class Simulate:
    def __init__(self):
        self._event = Event(7, 0, 2, 1, 2)
        self._clock = SimulationClock.instance
        self._reporter = Report()

    def run(self):
        try:
            while StatisticalCounter.number_serviced < self._event.get_finish_event_id():
                next_event_type = self.get_next_event_type()
                queue_len = SystemState.number_in_queue
                prev_time = self._clock.get_time()
                if Event.departure < float('inf'):
                    StatisticalCounter.area_under_bt += min(Event.arrival, Event.departure) - self._clock.get_time()
                if next_event_type == "arrival":
                    self.handle_arrival_event()
                elif next_event_type == "departure":
                    self.handle_departure_event()
                if queue_len:
                    StatisticalCounter.area_under_qt += queue_len * (
                            self._clock.get_time() - prev_time)
                self._reporter.print_snapshot(self._event.event_queue)
        except:
            print()

    def handle_arrival_event(self):
        customer = self._event.get_next()
        if SystemState.server_status == 1:
            self._event.event_queue.appendleft(customer)
            SystemState.number_in_queue += 1
        else:
            SystemState.server_status = 1
            StatisticalCounter.number_serviced += 1
            Event.departure = self._clock.get_time() + customer.get_service_time()
            SystemState.current_process = customer
        SystemState.time_of_last_event = self._clock.get_time()

    def handle_departure_event(self):
        SystemState.server_status = 0
        self._clock.set_time(Event.departure)
        SystemState.time_of_last_event = self._clock.get_time()
        Event.departure = float('inf')
        SystemState.current_process = None
        if not self._event.event_queue.is_empty():
            self.handle_arrival_event()

    @staticmethod
    def get_next_event_type():
        if Event.departure is not None and Event.arrival >= Event.departure:
            return "departure"
        return "arrival"


if __name__ == '__main__':
    simulate = Simulate()
    simulate.run()
