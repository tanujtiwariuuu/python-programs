# insert element at the beggining of linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.root = None
    def create_ll(self,element):
        if self.root is None:
            self.root = element
        else:
            temp = self.root
            while True:
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = element
    def display(self):
        cur = self.root
        while True:
            if cur is None:
                break
            print(cur.data)
            cur = cur.next
    def insert(self,ele):
        newnode = self.root
        self.root = ele
        self.root.next = newnode

n1 = Node(1)
l1 = Linked_list()
l1.create_ll(n1)
n2 = Node(2)
l1.create_ll(n2)
n3 = Node(3)
l1.create_ll(n3)
l1.display()
for i in range(int(input('how many element : '))):
    ele = int(input('enter element : '))
    n6 = Node(ele)
    l1.insert(n6)
    l1.display()
# l1.display()