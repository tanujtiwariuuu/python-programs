class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class complete_binary_tree:
    def __init__(self):
        self.root = None
    def insert(self,ele):
        if self.root is None:
            self.root = ele
        else:
            temp = self.root
    def left_insert(self,element):
        

