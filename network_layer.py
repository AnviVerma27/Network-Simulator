class NetworkLayer:
    def __init__(self):
        self.ip_addresses = {}
        self.routing_table = {}  # Routing table for devices

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

    def update_routing_table(self, ip_address, next_hop):
        if ip_address in self.routing_table:
            print(f"[Network Layer] Routing table update skipped: {ip_address} already mapped to {self.routing_table[ip_address]}")
        else:
            self.routing_table[ip_address] = next_hop
            print(f"[Network Layer] Routing table updated: {ip_address} -> {next_hop}")

    def get_route(self, ip_address):
        next_hop = self.routing_table.get(ip_address)
        if next_hop:
            print(f"[Network Layer] Found route to {ip_address} via {next_hop}")
        else:
            print(f"[Network Layer] No route to {ip_address} found")
        return next_hop
