# data_link_layer.py

class DataLinkLayer:
    def __init__(self):
        self.mac_addresses = {}
        self.arp_table = {}

    def assign_mac_address(self, device, mac_address):
        self.mac_addresses[device] = mac_address

    def get_mac_address(self, device):
        return self.mac_addresses.get(device)

    def update_arp_table(self, ip_address, mac_address):
        if ip_address in self.arp_table:
            print(f"[Data Link Layer] ARP entry update skipped: {ip_address} already mapped to {self.arp_table[ip_address]}")
        else:
            self.arp_table[ip_address] = mac_address
            print(f"[Data Link Layer] ARP entry added: {ip_address} -> {mac_address}")

    def get_mac_from_arp(self, ip_address):
        return self.arp_table.get(ip_address)

    def create_frame(self, src_mac, dst_mac, payload):
        print(f"[Data Link Layer] Creating frame with src_mac={src_mac}, dst_mac={dst_mac}, payload={payload}")
        return {
            'src_mac': src_mac,
            'dst_mac': dst_mac,
            'payload': payload,
            'type': 'DATA'
        }

    def create_ack(self, src_mac, dst_mac):
        print(f"[Data Link Layer] Creating ACK frame with src_mac={src_mac}, dst_mac={dst_mac}")
        return {
            'src_mac': src_mac,
            'dst_mac': dst_mac,
            'type': 'ACK'
        }

    def parse_frame(self, frame):
        print(f"[Data Link Layer] Parsing frame {frame}")
        src_mac = frame['src_mac']
        dst_mac = frame['dst_mac']
        frame_type = frame.get('type')
        payload = frame.get('payload')
        return src_mac, dst_mac, payload, frame_type
