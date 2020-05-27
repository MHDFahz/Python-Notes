class Node:
    def __init__(self,data):
        self.data = data
        self.left = left
        self.right = right
    def add(self,data):
        if self.data==data:
            return
        if self.data<data:
            if self.left:
                self.left.add(data)
            else:
                self.left=Node(data)
        else:
