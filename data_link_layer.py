class DataLinkLayer:
    def __init__(self):
        self.mac_addresses = {}
        self.arp_table = {}

    def assign_mac_address(self, device, mac_address):
        self.mac_addresses[device] = mac_address

    def get_mac_address(self, device):
        return self.mac_addresses.get(device)

    def update_arp_table(self, ip_address, mac_address):
        if ip_address not in self.arp_table:
            # print(f"\n [Data Link Layer] ARP entry update skipped: {ip_address} already mapped to {self.arp_table[ip_address]}")
        # else:
            self.arp_table[ip_address] = mac_address
            # print(f"\n [Data Link Layer] ARP entry added: {ip_address} -> {mac_address}")

    def get_mac_from_arp(self, ip_address):
        return self.arp_table.get(ip_address)

    def create_frame(self, src_mac, dst_mac, payload):
        parity_bit = self.calculate_parity(payload)
        print(f"\n [Data Link Layer] Creating frame with src_mac={src_mac}, dst_mac={dst_mac}, payload={payload}, parity={parity_bit}")
        return {
            'src_mac': src_mac,
            'dst_mac': dst_mac,
            'payload': payload,
            'parity': parity_bit,
            'type': 'DATA'
        }

    def create_ack(self, src_mac, dst_mac):
        print(f"\n [Data Link Layer] Creating ACK frame with src_mac={src_mac}, dst_mac={dst_mac}")
        return {
            'src_mac': src_mac,
            'dst_mac': dst_mac,
            'type': 'ACK'
        }

    def parse_frame(self, frame):
        print(f"\n [Data Link Layer] Parsing frame {frame}")
        src_mac = frame['src_mac']
        dst_mac = frame['dst_mac']
        frame_type = frame.get('type')
        payload = frame.get('payload')
        parity = frame.get('parity')

        if frame_type != 'ACK' and not self.validate_parity(payload, parity):
            print("\n [Data Link Layer] Parity check failed.")
            return None

        return src_mac, dst_mac, payload, frame_type

    def calculate_parity(self, payload):
        if payload is None:
            raise ValueError("ACK")
        message = payload.get('segment', {}).get("message")
        encoded = message['message']
        return sum(int(bit) for bit in encoded.replace(' ', '')) % 2

    def validate_parity(self, payload, parity):
        return self.calculate_parity(payload) == parity
    

    def print_arp_table(self):
        print("***************ARP Table***************")
        for ip_address, mac_address in self.arp_table.items():
            print(f"IP Address: {ip_address} -> MAC Address: {mac_address}")

