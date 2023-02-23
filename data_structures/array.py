class Array:

    def __init__(self):
        self.length = 0
        self.data = {}
        
    def __str__(self):
        return str(self.__dict__)

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    # Implement - insert() and delete()
