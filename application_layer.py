class ApplicationLayer:

    def create_message(self, message, protocol='MSG'):
        return {
            'protocol': protocol,
            'message': message
        }

    def parse_message(self, protocol,message):
        if protocol == 'PING':
            return self.handle_ping("Connected")
        elif protocol == 'FILE':
            return self.handle_file_transfer("Connection Setup, file sended")
        else:
            return message['message']

    def handle_ping(self, message):
        return f"Ping response: {message}"

    def handle_file_transfer(self, message):
        return f"File received: {message}"
