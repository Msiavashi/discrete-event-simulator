from Event import Event
from SimulationClock import SimulationClock
from SystemState import SystemState
from StatisticalCounters import StatisticalCounter


class Report:
    def __init__(self):
        self._snapshot_number = 1
        print("*** The floating numbers are due to python floating point truncation ***")

    def print_snapshot(self, event_queue):
        print("==================")
        print("Snapshot: " + str(self._snapshot_number))
        print("Clock: " + str(SimulationClock.instance.get_time()))
        print("Next Arrival Event: " + str(Event.arrival))
        print("Next Departure Event: " + str(Event.departure))
        print()
        print("Statistical Counters:")
        print()
        print("Number Serviced: " + str(StatisticalCounter.number_serviced))
        print("Total Delay: " + str(StatisticalCounter.total_delay))
        print("Area Under Q(t): " + str(StatisticalCounter.area_under_qt))
        print("Area Under B(t): " + str(StatisticalCounter.area_under_bt))
        print()
        print("System State: ")
        print()
        print("Server Status: " + str(SystemState.server_status))
        print("Number in Queue: " + str(SystemState.number_in_queue))
        # print("Times of Arrival: " + str([x.get_arrival_time() for x in event_queue]))
        print("Time of Last Event: " + str(SystemState.time_of_last_event))
        self._snapshot_number += 1
        print("==================")

    def analyze(self):
        print("Analysis")
        StatisticalCounter.WQ = StatisticalCounter.total_delay / StatisticalCounter.total_queued_customers
        StatisticalCounter.W = StatisticalCounter.total_service_times / StatisticalCounter.number_serviced
        StatisticalCounter.LQ = StatisticalCounter.area_under_qt / SimulationClock.instance.get_time()
        StatisticalCounter.P = StatisticalCounter.area_under_bt / SimulationClock.instance.get_time()
        StatisticalCounter.L = StatisticalCounter.P + StatisticalCounter.LQ
        print("WQ: " + str(StatisticalCounter.WQ))
        print("W: " + str(StatisticalCounter.W))
        print("LQ: " + str(StatisticalCounter.LQ))
        print("P or utilization: " + str(StatisticalCounter.P))
        print("L: " + str(StatisticalCounter.L))


