class Process:
    def __init__(self, id, delay,size,time,time_left,state):
        self.id = id
        self.delay = delay
        self.size = size
        self.time = time
        self.time_left = time_left
        self.state = state #  "waiting" "in_process" "finished"
    def __str__(self):
        return f"Process {self.id}: delay={self.delay}, size={self.size}, time_left={self.time_left}, state={self.state}"


class Segment:
    def __init__(self, start, size, state):
        self.start = start
        self.size = size
        self.state = state  # "free" или "P(x)"
    def __str__(self):
        return f"[start={self.start}, size={self.size}, state={self.state}]"
    