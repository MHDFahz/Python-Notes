class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print(self):
        space = " " * self.level() * 3
        prefix = space + "-->"
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print()


def product():
    root = Node("Electronics")
    laptop = Node("laptop")
    laptop.addChild(Node("mac"))
    laptop.addChild(Node("win"))
    laptop.addChild(Node("ubuntu"))
    root.addChild(laptop)
    print(laptop.level())
    return root


if __name__ == '__main__':
    root = product()
    root.print()
    pass
