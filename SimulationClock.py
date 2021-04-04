import threading


class SimulationClockSingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._instance = None
        cls._locker = threading.Lock()

    @property
    def instance(self, *args, **kwargs):
        if self._instance is None:
            with self._locker:
                if self._instance is None:
                    self._instance = self(*args, **kwargs)
        return self._instance


class SimulationClock(metaclass=SimulationClockSingletonMeta):
    """
    Clock with nano second resolution
    """

    def __init__(self):
        self._time = 0

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def increase(self, ns):
        self._time += ns

    def to_seconds(self):
        return self._time * 1000000000
