class TransportLayer:
    WELL_KNOWN_PORTS = {80: 'HTTP', 443: 'HTTPS', 21: 'FTP'}
    EPHEMERAL_PORT_START = 49152
    EPHEMERAL_PORT_END = 65535

    def __init__(self):
        self.active_connections = {}

    def create_segment(self, message, src_port= 80, dst_port = 80):
        print(f"\n [Transport Layer] Creating segment from port {src_port} to port {dst_port} with message='{message}'")
        if src_port not in self.active_connections:
            self.assign_port(src_port)
        return {
            'src_port': src_port,
            'dst_port': dst_port,
            'message': message
        }

    def parse_segment(self, segment):
        print(f"\n [Transport Layer] Parsing segment from port {segment['src_port']} to port {segment['dst_port']}")
        return segment['src_port'], segment['dst_port'], segment['message']

    def assign_port(self, port):
        if port in self.WELL_KNOWN_PORTS or (self.EPHEMERAL_PORT_START <= port <= self.EPHEMERAL_PORT_END):
            self.active_connections[port] = True
            print(f"\n [Transport Layer] Port {port} assigned.")
        else:
            raise ValueError("Invalid port number. Use a well-known or ephemeral port number.")
