# data_link_layer.py

class DataLinkLayer:
    def __init__(self):
        self.mac_addresses = {}

    def assign_mac_address(self, device, mac_address):
        self.mac_addresses[device] = mac_address

    def get_mac_address(self, device):
        return self.mac_addresses.get(device)

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
