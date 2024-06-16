# physical_layer.py

class PhysicalLayer:
    def __init__(self):
        self.connections = {}

    def remove_device(self, device_name):
        if device_name in self.connections:
            del self.connections[device_name]

    def add_connection(self, device1, device2):
        if device1 not in self.connections:
            self.connections[device1] = []
        if device2 not in self.connections:
            self.connections[device2] = []
        self.connections[device1].append(device2)
        self.connections[device2].append(device1)

    def get_connections(self, device):
        return self.connections.get(device, [])
