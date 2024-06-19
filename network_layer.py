class NetworkLayer:
    def __init__(self):
        self.ip_addresses = {}
        self.routing_table = {}  

    def assign_ip_address(self, device, ip_address):
        self.ip_addresses[device] = ip_address

    def get_ip_address(self, device):
        return self.ip_addresses.get(device)

    def update_routing_table(self, ip_address, next_hop):
        self.routing_table[ip_address] = next_hop
        print(f"[Network Layer] Routing table updated: {ip_address} -> {next_hop}")

    def get_route(self, dst_ip):
        return self.routing_table.get(dst_ip)

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


