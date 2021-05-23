class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.root = None
    def create_list(self,ele):
        if self.root is None:
            self.root = ele
        else:
            temp = self.root
            while True:
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = ele
    def display(self):
        cur= self.root
        while True:
            if cur is None:d
                break
            print(cur.data)
            cur = cur.next
    def insert_specific(self,element):
        pos = int(input('pos : '))
        i = self.root
        c = 0
        while True:
            if c == pos:
                prev.next = element
                element.next = i
                break
            c += 1
            prev=i
            i = i.next
n1 = Node(4)
l1 = Linked_list()
l1.create_list(n1)
n2=Node(5)
l1.create_list(n2)
n5=Node(55)
l1.create_list(n5)
l1.display()
for i in range(int(input('num : '))):
    element = int(input('ele : '))
    n3 = Node(element)
    l1.insert_specific(n3)
    l1.display()