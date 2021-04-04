from collections import deque


class EventQueue(deque):
    def __init__(self):
        super().__init__()

    def is_empty(self):
        if len(self) == 0:
            return True
        return False
