class Stack:
    def __init__(self, value):
        self.top = {
            "val": value,
            "next": None
        }
        self.bottom = self.top
        self.n = 1

    def push(self, value):
        node = {
            "val": value,
            "next": self.top
        }
        self.top = node
        self.n += 1

    def pop(self):
        top = self.top
        self.top = top["next"]
        self.n -= 1
        
        return top

    def is_empty(self):
        return self.n == 0
        