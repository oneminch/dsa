class BST:
    def __init__(self):
        self.root = None
        
    def __str__(self):
        return str(self.__dict__)

    def insert(self, value):
        node = {
            "value": value,
            "left": None,
            "right": None
        }

        if self.root == None:
            self.root = node
            return

        currNode = self.root

        while True:
            if value < currNode["value"]:
                # Go left
                if currNode["left"] == None:
                    currNode["left"] = node
                    return
                currNode = currNode["left"]
            else:
                # elif value > currNode["value"]:
                # Go right
                if currNode["right"] == None:
                    currNode["right"] = node
                    return
                currNode = currNode["right"]

    # Breadth-first search
    def bfs(self):
        curr_node = root
        queue = []
        list = []
        queue.append(curr_node)