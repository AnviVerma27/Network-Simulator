# device.py

from data_link_config import DataLinkLayerConfig
from network_layer import NetworkLayer
from transport_layer import TransportLayer
from utils import decode  

class Device:
    def __init__(self, name, device_type, mac_address, ip_address):
        self.name = name
        self.device_type = device_type
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.data_link_layer = DataLinkLayerConfig.get_instance().data_link_layer
        self.network_layer = NetworkLayer()
        self.transport_layer = TransportLayer()

        self.data_link_layer.assign_mac_address(self, mac_address)
        self.network_layer.assign_ip_address(self, ip_address)

    def send_message(self, dst_device, message):
        print(f"[{self.name}] Sending message to [{dst_device.name}]: {message}")
        segment = self.transport_layer.create_segment(message)
        print(f"[{self.name}] Transport Layer: Created segment {segment}")
        packet = self.network_layer.create_packet(self.ip_address, dst_device.ip_address, segment)
        print(f"[{self.name}] Network Layer: Created packet {packet}")
        
        print(self.data_link_layer.arp_table)
        dst_mac = self.data_link_layer.get_mac_from_arp(dst_device.ip_address)
        if dst_mac is None:
            print(f"[{self.name}] ARP Miss: MAC address for IP {dst_device.ip_address} not found.")
            return
        
        frame = self.data_link_layer.create_frame(self.mac_address, dst_mac, packet)
        print(f"[{self.name}] Data Link Layer: Created frame {frame}")
        self.physical_layer_send(dst_device, frame)

    def physical_layer_send(self, dst_device, frame):
        print(f"[{self.name}] Physical Layer: Sending frame {frame}")
        dst_device.receive_message(frame, self)

    def receive_message(self, frame, src_device):
        print(f"[{self.name}] Physical Layer: Received frame {frame}")
        src_mac, dst_mac, payload, frame_type = self.data_link_layer.parse_frame(frame)
        print(f"[{self.name}] Data Link Layer: Parsed frame, payload {payload}")
        if frame_type == 'DATA':
            src_ip, dst_ip, segment = self.network_layer.parse_packet(payload)
            print(f"[{self.name}] Network Layer: Parsed packet, segment {segment}")
            encoded_message = self.transport_layer.parse_segment(segment)
            message = decode(encoded_message)  
            print(f"[{self.name}] Transport Layer: Parsed segment, message '{message}'")
            print(f"[{self.name}] Message received from [{src_device.name}]: {message}")

            ack_frame = self.data_link_layer.create_ack(self.mac_address, src_mac)
            print(f"[{self.name}] Data Link Layer: Created ACK frame {ack_frame}")
            self.physical_layer_send(src_device, ack_frame)

