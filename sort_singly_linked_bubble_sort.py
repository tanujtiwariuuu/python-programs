class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.root = None
    def insert(self,ele):
        if self.root is None:
            self.root = ele

        else:
            temp = self.root
            while True:
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = ele
    def bubble_sort(self):
        temp = self.root
        c = 0
        while True:
            if temp is None:
                break
            c += 1
            temp = temp.next
        while True:
            

    def display(self):
        temp = self.root
        while True:
            if temp is None:
                break
            print(temp.data)
            temp = temp.next





l1 = Linked_list()
for i in range(5):
    p1 = Node(int(input('enter data ')))
    l1.insert(p1)
l1.display()
print()
l1.bubble_sort()
l1.display()