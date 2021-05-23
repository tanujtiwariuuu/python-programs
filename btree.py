# complete this into complete binary tree
class BTree:
    def __init__(self,*value):
        self.root = None
        self.left = None
        self.right = None
        self.value = value
    def display(self):
        i=0
        while i!=len(self.value):
            self.root = self.value[0]
            i=i+1
        print(self.root)
        print(self.left)
        print(self.right)

p1 = BTree(4,5,6,7,8,9,1)
p1.display()
