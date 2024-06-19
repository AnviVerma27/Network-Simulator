class NetworkLayer:
    def __init__(self):
        self.ip_addresses = {}
        self.routing_table = {}  

    def assign_ip_address(self, device, ip_address):
        self.ip_addresses[device] = ip_address

    def get_ip_address(self, device):
        return self.ip_addresses.get(device)

    def update_routing_table(self, ip_address, next_hop, metric):
        if ip_address in self.routing_table:
            current_next_hop, current_metric = self.routing_table[ip_address]
            if metric < current_metric:
                self.routing_table[ip_address] = (next_hop, metric)
                print(f"[\n Network Layer] Routing table updated: {ip_address} -> {next_hop}, metric={metric}")
        else:
            self.routing_table[ip_address] = (next_hop, metric)
            # print(f"\n [Network Layer] Routing table entry added: {ip_address} -> {next_hop}, metric={metric}")

    def get_route(self, dst_ip):
        if dst_ip in self.routing_table:
            next_hop, _ = self.routing_table[dst_ip]
            return next_hop
        return None

    def create_packet(self, src_ip, dst_ip, segment):
        print(f"\n [Network Layer] Creating packet with src_ip={src_ip}, dst_ip={dst_ip}, segment={segment}")
        return {
            'src_ip': src_ip,
            'dst_ip': dst_ip,
            'segment': segment
        }

    def parse_packet(self, packet):
        print(f"\n [Network Layer] Parsing packet {packet}")
        src_ip = packet['src_ip']
        dst_ip = packet['dst_ip']
        segment = packet['segment']
        return src_ip, dst_ip, segment

    def broadcast_routing_info(self):
        for ip, (next_hop, metric) in self.routing_table.items():
            self.send_routing_update(ip, next_hop, metric)

    def send_routing_update(self, ip_address, next_hop, metric):
        print(f"\n [Network Layer] Sending routing update: {ip_address} -> {next_hop}, metric={metric}")

    def print_routing_table(self):
        print("***************Routing Table***************")
        for ip_address, (next_hop, metric) in self.routing_table.items():
            print(f"  Destination IP: {ip_address} -> Next Hop: {next_hop}")
