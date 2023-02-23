# Implemented using a linked list data structure

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        return str(self.__dict__)

    def push(self, value):
        if self.is_empty():
            next = None
        else:
            next = self.top

        node = {"val": value, "next": next}
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
            
        top = self.top
        self.top = top["next"]
        self.size -= 1

        return top

    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        else:
            return self.top["val"]

    def is_empty(self):
        return self.size == 0

    # return items in an array
    def listify(self):
        node = self.top
        items = []
        while node:
            items.append(node["val"])
            node = node["next"]

        return items

