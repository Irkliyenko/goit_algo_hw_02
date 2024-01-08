from queue import Queue
import random
import string
import time
import signal


class Client:
    def __init__(self):
        # creats ID with 8 randon letters and digits
        self.id = ''.join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(8))


class CallCenter:
    def __init__(self):
        self.clients = Queue()
        self.active = True  # for while loop
        # setting up signal handlers
        # user-initiated stop. Setting interpratation of keybord to stop the program (CTRL+C)
        signal.signal(signal.SIGINT, self.signal_handler)
        # signal.signal(signal.SIGTERM, self.signal_handler) # system-intiated stop.

    # function that is handling termination signal and changes self.active to False
    def signal_handler(self, signum):
        print(f"Received signal: {signum}. Shutting down.")
        self.active = False

    def generate_request(self):
        new_client = Client()  # create Client class instance to use generated id
        self.clients.put(new_client.id)
        print(f'Request generated for client ID: {new_client.id}')

    def process_request(self):
        if not self.clients.empty():
            current_id = self.clients.get()
            print(f'{current_id} is being processed')

    def run(self):
        while self.active:
            self.generate_request()
            self.process_request()

            time.sleep(3)  # adds wait time before adding new request


call_center = CallCenter()
call_center.run()
print(f'Run is finished')
