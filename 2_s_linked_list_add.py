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
        # l111=[]
        while True:
            if c is None:
                break
            print(c.data)
            c = c.next
    def addition(self,l,e):
        # print('f',self.root.data)
        total = 0
        l = self.root
        e = self.root
        # c = self.root
        while True:
            if e is None:
                break
            total = l.data+e.data
            l = l.next
            e= e.next
            print('sum of elements', total)
p1 = Node(4)
p2 = Linked_list()
p2.insert(p1)
p3 = Node(3)
p2.insert(p3)
p4 = Node(5)
p2.insert(p4)
c1 = Node(9)
ll1 = Linked_list()
ll1.insert(c1)
c2 = Node(7)
ll1.insert(c2)
c3 = Node(8)
ll1.insert(c3)
ll1.pr()
p2.pr()
l2 = Linked_list()
l2.addition(ll1,p2)