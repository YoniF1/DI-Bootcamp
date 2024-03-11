class Phone():
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.messages = []

    def call(self, other_phone):
        history = f"{self.phone_number} called {other_phone.phone_number}"
        self.call_history.append(history)
        print(history)

    def show_call_history(self):
        for call in self.call_history:
            print(call)
    
    def send_message(self, to, content):
        if type(to) is not Phone:
            print("You need to pass in a Phone object")
            return

        message_dict = { 'to': to.phone_number, 'from': self.phone_number, 'content': content }
        self.messages.append(message_dict)
        to.messages.append(message_dict)

    def show_outgoing_messages(self):
        for message in self.messages:
            if message['from'] == self.phone_number:
                print(f"Outgoing message: {message}")
    
    def show_incoming_messages(self):
        for message in self.messages:
            if message['to'] == self.phone_number:
                print(f"Incoming message: {message}")

    def show_messages_from(self):
        for message in self.messages:
            print(f"{message['from']}")

phone = Phone('05222222222')
phone2 = Phone('053333333')
phone.call_history = []
phone2.call_history = []

phone.call(phone2)
phone2.call(phone)
phone.show_call_history()
phone2.show_call_history()

phone.send_message(phone2, "Hello does this work")
phone.send_message(phone2, "Testing testing 123")
phone.show_outgoing_messages()

phone2.show_incoming_messages()
phone2.show_messages_from()

