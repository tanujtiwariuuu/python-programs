# program to insert element  at last position in singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next= None
class Linked_list:
    def __init__(self):
        self.root = None
    def create_linked_list(self,element):
        if self.root is None:
            self.root = element
        else:
            temp_node = self.root
            while True:
                if temp_node.next is None:
                    break
                temp_node = temp_node.next
            temp_node.next = element
    def display(self):
        current_node = self.root
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next

    def insert_last(self,ele):
        temp = self.root
        c = 0
        while True:
            if temp.next is None:
                temp.next = ele
                break
            temp = temp.next
            c += 1
n1 = Node(1)
l1 = Linked_list()
l1.create_linked_list(n1)
n2 = Node(2)
l1.create_linked_list(n2)
n3 = Node(3)
l1.create_linked_list(n3)
l1.display()
for i in range(2):
    ele = int(input('enter element : '))
    n6 = Node(ele)
    l1.insert_last(n6)
    l1.display()