import random
import string
import time


class Server:

    def __init__(self, x, y, dc_name):
        self.id = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
        self.status = False
        self.x = x
        self.y = y
        self.dc_name = dc_name
        self.tasks = list()
        self.free_after = 0

    def assign_task(self, task):

        if self.free_after > time.time():
            tt = self.free_after
        else:
            tt = time.time()
            task.state = "running"

        task.start_time = tt
        task.dc = self.dc_name
        task.server = self.id
        self.free_after = tt + task.required_time
        self.tasks.append(task)
        self.status = True

        print('Task ' + str(task.id) + ' Assigned in Server ' + self.id
              + ' of ' + self.dc_name + '. State: ' + task.state)
