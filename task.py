import random
import string
import time


class Task:

    def __init__(self, x, y):
        self.id = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        self.state = "pending"
        self.required_time = self.analyze_execution_time()
        self.dc = ''
        self.server = ''
        self.x = x
        self.y = y
        self.start_time = 0

    @staticmethod
    def analyze_execution_time():
        return float(random.randint(100, 5000) / 1000)

    def assign_in_server(self, server):
        self.server = server.id
        self.start_time = time.time()
