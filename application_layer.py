# application_layer.py

class ApplicationLayer:
    def create_message(self, message):
        return {
            'protocol': 'MSG',
            'message': message
        }

    def parse_message(self, message):
        return message['message']
