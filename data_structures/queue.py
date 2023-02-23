# Implemented using a linked list data structure

class Queue:

    def __init__(self):
        self.first = None
        self.last = self.first
        self.size = 0

    def __str__(self):
        return str(self.__dict__)

    def enqueue(self, value):
        node = {"val": value, "next": None}
        
        if self.is_empty():
            self.last = node
            self.first = self.last
        else:
            self.last["next"] = node
            self.last = node
                        
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
            
        first = self.first

        if self.size > 1:
            self.first = first["next"]
        else:
            self.first = None
            self.last = self.first            
            
        self.size -= 1

        return first

    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        else:
            return self.first["val"]

    def is_empty(self):
        return self.size == 0

    # return items in an array
    def listify(self):
        node = self.first
        items = []
        while node:
            items.append(node["val"])
            node = node["next"]

        return items


