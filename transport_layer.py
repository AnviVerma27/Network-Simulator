# # transport_layer.py

# class TransportLayer:
#     def create_segment(self, src_port, dst_port, payload):
#         return {
#             'src_port': src_port,
#             'dst_port': dst_port,
#             'payload': payload,
#             'protocol': 'TCP',
#             'type': 'DATA'
#         }

#     def create_ack_segment(self, src_port, dst_port):
#         return {
#             'src_port': src_port,
#             'dst_port': dst_port,
#             'protocol': 'TCP',
#             'type': 'ACK'
#         }

#     def parse_segment(self, segment):
#         return segment['src_port'], segment['dst_port'], segment['payload'], segment['protocol'], segment['type']

class TransportLayer:
    def create_segment(self, message):
        print(f"[Transport Layer] Creating segment with message={message}")
        return {
            'message': message
        }

    def parse_segment(self, segment):
        print(f"[Transport Layer] Parsing segment {segment}")
        return segment['message']

