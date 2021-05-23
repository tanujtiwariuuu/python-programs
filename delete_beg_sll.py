# singly linked list :
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
class Linked_list:
    def __init__(self):
        # self.next = None
        self.root = None
    def insert(self, dataa):
        if self.root is None:
            self.root = dataa
        else:
            temp = self.root
            while True:
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = dataa
    def pr(self):
        c = self.root
        while True:
            if c is None:
                break
            print(c.data)
            c = c.next
    def delete(self):
        # q=self.root
        self.root = 

c1 = Node(9)
ll1 = Linked_list()
ll1.insert(c1)
c2 = Node(7)
ll1.insert(c2)
c3 = Node(8)
ll1.insert(c3)
ll1.delete()
# ll1.pr()
ll1.delete()
ll1.pr()
