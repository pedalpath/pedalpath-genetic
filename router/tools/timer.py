import time

class Duration:
    def __init__(self,seconds):
        self.seconds = seconds
    def __repr__(self):
        return '{:0.8f} secs'.format(self.seconds)

class Timer:
    def __init__(self,name):
        self.name = name
        self.start()
    def start(self,name=None):
        self.name = name if name else self.name
        self.start_time = time.perf_counter()
    def finish(self):
        self.stop_time = time.perf_counter()
        self.duration = Duration(self.stop_time - self.start_time)
        print('{}: {}'.format(self.name,self.duration))
