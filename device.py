from data_link_config import DataLinkLayerConfig
from network_layer import NetworkLayer
from network_layer_config import NetworkLayerConfig
from transport_layer import TransportLayer
from application_layer import ApplicationLayer
from utils import decode

class Device:
    def __init__(self, name, device_type, mac_address, ip_address):
        self.name = name
        self.device_type = device_type
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.data_link_layer = DataLinkLayerConfig.get_instance().data_link_layer
        self.network_layer = NetworkLayerConfig.get_instance().network_layer
        self.transport_layer = TransportLayer()
        self.application_layer = ApplicationLayer()
        self.data_link_layer.assign_mac_address(self, mac_address)
        self.network_layer.assign_ip_address(self, ip_address)
        self.network_layer.broadcast_routing_info()  

    def send_message(self, dst_device, message, protocol='MSG'):
        print(f"\n [{self.name}] Sending message to [{dst_device.name}]: {message}")
        app_message = self.application_layer.create_message(message, protocol)
        
        segment = self.transport_layer.create_segment(app_message)
        print(f"\n [{self.name}] Transport Layer: Created segment {segment}")
        self.network_layer.print_routing_table()
        next_hop_ip = self.network_layer.get_route(dst_device.ip_address)
        if not next_hop_ip:
            print(f"\n [{self.name}] Routing Error: No route to host {dst_device.ip_address}")
            return
        print(f"\n [{self.name}] Next hop IP address for destination {dst_device.ip_address} is {next_hop_ip}")
        if protocol == "PING" or protocol == "FILE":
            test = self.application_layer.parse_message(protocol, app_message)
            print("#########",test)
        else:
            packet = self.network_layer.create_packet(self.ip_address, next_hop_ip, segment)
            print(f"\n [{self.name}] Network Layer: Created packet {packet}")
            self.data_link_layer.print_arp_table()
            dst_mac = self.data_link_layer.get_mac_from_arp(next_hop_ip)
            if dst_mac is None:
                print(f"\n [{self.name}] ARP Miss: MAC address for IP {next_hop_ip} not found.")
                return
            
            frame = self.data_link_layer.create_frame(self.mac_address, dst_mac, packet)
            print(f"\n [{self.name}] Data Link Layer: Created frame {frame}")
            self.physical_layer_send(dst_device, frame)

    def physical_layer_send(self, dst_device, frame):
        print(f"\n [{self.name}] Physical Layer: Sending frame to {dst_device.name}")
        dst_device.receive_message(frame, self)

    def receive_message(self, frame, src_device):
        print(f"\n [{self.name}] Physical Layer: Received frame {frame}")
        src_mac, dst_mac, payload, frame_type = self.data_link_layer.parse_frame(frame)
        if src_mac is None:
            print(f"\n [{self.name}] Data Link Layer: Frame corrupted, requesting retransmission")
            nack_frame = self.data_link_layer.create_nack(self.mac_address, src_mac)
            self.physical_layer_send(src_device, nack_frame)
            return

        print(f"\n [{self.name}] Data Link Layer: Parsed frame, payload {payload}")
        if frame_type == 'DATA':
            src_ip, dst_ip, segment = self.network_layer.parse_packet(payload)
            print(f"\n [{self.name}] Network Layer: Parsed packet, segment {segment}")
            encoded_message = self.transport_layer.parse_segment(segment)
            message = decode((encoded_message[2]).get('message'))
            print(f"\n [{self.name}] Transport Layer: Parsed segment, message '{message}'")
            print(f"\n [{self.name}] Message received from [{src_device.name}]: {message}")

            ack_frame = self.data_link_layer.create_ack(self.mac_address, src_mac)
            print(f"\n [{self.name}] Data Link Layer: Created ACK frame {ack_frame}")
            self.physical_layer_send(src_device, ack_frame)
        global medium
        medium = "idle"
        print("medium:", medium)
