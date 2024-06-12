# main.py

import tkinter as tk
from tkinter import Canvas
from device import Device
from physical_layer import PhysicalLayer

class NetworkSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Simulator")
        self.canvas = Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.devices = {}
        self.physical_layer = PhysicalLayer()
        self.device_positions = {}
        self.selected_devices = []

        self.device_type = None
        self.create_widgets()

    def create_widgets(self):
        add_router_button = tk.Button(self.root, text="Add Router", command=lambda: self.set_device_type("Router"), font=("Arial", 12))
        add_router_button.pack(side=tk.LEFT)

        add_switch_button = tk.Button(self.root, text="Add Switch", command=lambda: self.set_device_type("Switch"), font=("Arial", 12))
        add_switch_button.pack(side=tk.LEFT)

        add_pc_button = tk.Button(self.root, text="Add PC", command=lambda: self.set_device_type("PC"), font=("Arial", 12))
        add_pc_button.pack(side=tk.LEFT)

        send_button = tk.Button(self.root, text="Send Message", command=self.send_message, font=("Arial", 12))
        send_button.pack(side=tk.LEFT)

        self.canvas.bind("<Button-1>", self.add_or_select_device)

    def set_device_type(self, device_type):
        self.device_type = device_type

    def add_or_select_device(self, event):
        if self.device_type:
            device_name = f"{self.device_type}_{len(self.devices)}"
            mac_address = f"00:00:00:00:00:{len(self.devices):02x}"
            ip_address = f"192.168.0.{len(self.devices) + 1}"
            device = Device(device_name, self.device_type, mac_address, ip_address)
            self.devices[device_name] = device
            self.device_positions[device_name] = (event.x, event.y)
            self.canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill="blue")
            self.canvas.create_text(event.x, event.y, text=device_name, font=("Arial", 12), fill="black")
            self.device_type = None
        else:
            clicked_device = self.find_device_at_position(event.x, event.y)
            if clicked_device:
                self.selected_devices.append(clicked_device)
                if len(self.selected_devices) == 2:
                    self.connect_devices(self.selected_devices[0], self.selected_devices[1])
                    self.selected_devices = []

    def find_device_at_position(self, x, y):
        for device_name, position in self.device_positions.items():
            dx, dy = position
            if (dx - 10) <= x <= (dx + 10) and (dy - 10) <= y <= (dy + 10):
                return device_name
        return None

    def connect_devices(self, device1_name, device2_name):
        if device1_name in self.devices and device2_name in self.devices:
            self.physical_layer.add_connection(device1_name, device2_name)
            x1, y1 = self.device_positions[device1_name]
            x2, y2 = self.device_positions[device2_name]
            self.canvas.create_line(x1, y1, x2, y2,fill="black")
            print(f"Connected {device1_name} and {device2_name}")

    def send_message(self):
        src_device_name = input("Enter source device name: ")
        dst_device_name = input("Enter destination device name: ")
        message = input("Enter message: ")
        if src_device_name in self.devices and dst_device_name in self.devices:
            src_device = self.devices[src_device_name]
            dst_device = self.devices[dst_device_name]
            src_device.send_message(dst_device, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSimulatorApp(root)
    root.mainloop()
