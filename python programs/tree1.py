class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print(self):
        space = ' ' * self.level() * 3
        prefic = space + '-->'
        print(prefic+self.data)
        for i in self.children:
            i.print()

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printleaf(self):
        if self.level() == 2:
            print(self.data)
        for i in self.children:
            i.printleaf()


root = Node('ELectronics')
laptop = Node('Laptop')
laptop.addChild(Node('Mac'))
laptop.addChild(Node('Windows'))
laptop.addChild(Node('linux'))
tv = Node('Tv')
tv.addChild(Node('Sumsumg'))
tv.addChild(Node('LG'))
tv.addChild(Node('philips'))
Mobile = Node('Mobile')
Mobile.addChild(Node('LG'))
Mobile.addChild(Node('iphone'))
root.addChild(laptop)
root.addChild(Mobile)
root.addChild(tv)
root.print()

print("--")
root.printleaf()
