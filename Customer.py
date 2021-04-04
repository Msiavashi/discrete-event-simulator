class Customer:
    def __init__(self, arrival_time, service_time, c_id):
        self._arrival_time = arrival_time
        self._service_time = service_time
        self._id = c_id

    def get_id(self):
        return self._id

    def get_service_time(self):
        return self._service_time

    def get_arrival_time(self):
        return self._arrival_time
