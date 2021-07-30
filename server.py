import random
import string


class Server:

    def __init__(self, x, y):
        self.id = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
        self.status = False
        self.x = x
        self.y = y
