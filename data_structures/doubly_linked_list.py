class DoublyLinkedList:
    def __init__(self, value):
        self.head = {
            "val": value,
            "next": None,
            "prev": None
        }
        
        self.tail = self.head;
        self.n = 1

    def __str__(self):
        return str(self.__dict__)

        
    def dictify(self):
        return self.__dict__
        

    def append(self, value):
        node = {
            "val": value,
            "next": None,
            "prev": self.tail
        }
        self.tail["next"] = node
        self.tail = node
        self.n += 1

    def prepend(self, value):
        tmp = self.head
        self.head = {
            "val": value,
            "next": tmp,
            "prev": None
        }
        tmp["prev"] = self.head
        self.n += 1

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return self.listify()
        elif index > self.n:
            self.append(value)
            return self.listify()

        i = 0
        node = self.head
        while i != index-1:
            node = node["next"]
            i += 1

        tmp = node["next"]
        node["next"] = {
            "val": value,
            "next": tmp,
            "prev": node
        }
        self.n += 1
        return self.listify()

    def remove(self, index):
        if index >= self.n:
            print("Index out of range")
            return
        elif index == 0:
            self.head = self.head["next"]
            self.head["prev"] = None
            self.n -= 1
            return
        
        i = 0
        node = self.head
        while i != index - 1:
            node = node["next"]
            i += 1

        tmp = node["next"]["next"]
        del node["next"]
        node["next"] = tmp

        if tmp:
            tmp["prev"] = node
                
        self.n -= 1
            
        
    # return items in an array
    def listify(self):
        node = self.head
        items = []
        while node:
            items.append(node["val"])
            node = node["next"]

        return items
        