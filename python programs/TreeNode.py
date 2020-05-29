class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        self.end = True

    def add_child(self, child):
        child.parent = self
        self.end = False
        self.children.append(child)

    def level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print(self):
        d = self.level()
        space = " " * d * 3
        print(space+str(d)+"--|"+self.data)
        for i in self.children:
            i.print()

    def leaf(self):
        if self.end:
            print(self.data)
        for i in self.children:
            i.leaf()

    def search(self, dat,q):
        if dat == self.data:
            q.append(self.level())
            return q
        else:
            for i in self.children:
                i.search(data,q)
        if q:
            return q[0]


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    Samsung = TreeNode("Samsung")
    tv.add_child(Samsung)
    Samsung.add_child(TreeNode("Samsung2"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    root.print()
    return root


if __name__ == '__main__':
    root = build_product_tree()
    data = "LG"
    find = root.search(data,[])
    if find:
        print(f"found in {find} level")
    else:
        print("not find")
