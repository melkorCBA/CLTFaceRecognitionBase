from time import sleep


class Timer:
    time = 0

    def __init__(self, limit=1000000000000000000000000):
        self.limit = limit
        self.time = 0

    def getCurrentTime(self):
        return self.time

    def resetTimer(self):
        self.limit = 0
        self.time = 0
        self.limit = 100000000000000000000000000
        self.startTimer()

    def startTimer(self):
        while(self.time < self.limit):
            sleep(1)
            time += 1

    def stopTimer(self):
        self.limit = 0
        self.time = 0
        self.limit = 100000000000000000000000000
