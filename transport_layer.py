class TransportLayer:
    def create_segment(self, message):
        print(f"[Transport Layer] Creating segment with message={message}")
        return {
            'message': message
        }

    def parse_segment(self, segment):
        print(f"[Transport Layer] Parsing segment {segment}")
        return segment['message']

