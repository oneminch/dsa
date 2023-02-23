# n - total number of items

class HashTable:

    def __init__(self, size):
        self.data = {}
        self.size = size
        self.n = 0

    def __str__(self):
        return str(self.__dict__)

    def hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size

        return hash

    def set(self, key, value):
        address = self.hash(key)
        if address not in self.data:
            self.data[address] = []

        self.data[address].append([key, value])
        self.n += 1

    def get(self, key):
        address = self.hash(key)
        if address in self.data:
            bucket = self.data[address]

            for item in bucket:
                if item[0] == key:
                    return item[1]

        return None

    # put all key-value pairs into a single list
    def flatten(self):
        all_items = []

        for hash in self.data:
            all_items.extend(self.data[hash])

        return all_items

    def keys(self):
        key_list = []

        for item in self.flatten():
            key_list.append(item[0])

        return key_list
