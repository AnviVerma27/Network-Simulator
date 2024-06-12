# network_layer.py

class NetworkLayer:
    def __init__(self):
        self.ip_addresses = {}

    def assign_ip_address(self, device, ip_address):
        self.ip_addresses[device] = ip_address

    def get_ip_address(self, device):
        return self.ip_addresses.get(device)

    def create_packet(self, src_ip, dst_ip, segment):
        print(f"[Network Layer] Creating packet with src_ip={src_ip}, dst_ip={dst_ip}, segment={segment}")
        return {
            'src_ip': src_ip,
            'dst_ip': dst_ip,
            'segment': segment
        }

    def parse_packet(self, packet):
        print(f"[Network Layer] Parsing packet {packet}")
        src_ip = packet['src_ip']
        dst_ip = packet['dst_ip']
        segment = packet['segment']
        return src_ip, dst_ip, segment