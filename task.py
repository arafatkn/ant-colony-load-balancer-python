import random
import string


class Task:

    def __init__(self, x, y):
        self.id = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        self.state = "pending"
        self.required_time = self.analyzeExecutionTime()  # in  milliseconds
        self.dc = ''
        self.server = ''
        self.x = x
        self.y = y

    @staticmethod
    def analyzeExecutionTime():
        return random.randint(100, 500)
