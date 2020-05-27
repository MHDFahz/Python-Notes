class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.endhere = False
        self.father = None

    def insert(self, word):
        parent = selfa
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = Node(char)
                parent.children[char].father = parent
            parent = parent.children[char]
            if i == len(word)-1:
                parent.endhere = True

    def search(self, word):
        print(f"Seraching {word} in {self.val}")
        parent = self
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.endhere
    def startWith(self,prefix):
        print(f"Search startwith {prefix} in {self.val}")
        parent = self
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True
    def level(self):
        level = 0
        p = self.father
        while p:
            level += 1
            p = p.father
        return level

    def print(self):
        space = " "*self.level()*3
        print(space+"-->"+self.val)
        for i in self.children.values():
            i.print()


node = Node("MainNode")
node.insert("apple")
node.insert("appy")
node.insert("dog")
node.insert("down")
node.insert("drown")
node.print()
print(node.search("apple"))
print(node.search("appl"))
print(node.startWith("appl"))
print(node.startWith("appr"))


