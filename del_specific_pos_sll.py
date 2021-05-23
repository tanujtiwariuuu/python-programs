import os, psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.root = None
    def create(self,element):
        if self.root is None:
            self.root = element
            # global temp

        else:
            temp = self.root
            while True:
                if temp.next is None:
                    break

                temp = temp.next
            temp.next = element
    def display(self):
        s = self.root
        while True:
            if s is None:
                break
            print(s.data)
            s = s.next
    def delete_node(self):
        pos = int(input('entr pos : '))
        count=0
        c = self.root
        prev = c
        while True:
            if pos==1:
                self.root = c.next
                break

            elif count+1 == pos:
                prev.next = c.next
                break
            count += 1
            prev = c
            c = c.next
p1 = Node(4)

p2 = Linked_list()
p2.create(p1)
p1 = Node(45)
p2.create(p1)
p1 = Node(435)
p2.create(p1)
p1 = Node(4333333333335)
p2.create(p1)
p2.display()
p2.delete_node()
p2.display()
p1 = Node(433335)
p2.create(p1)
p1 = Node(9995)
p2.create(p1)
p2.display()
process = psutil.Process(os.getpid())
print(process.memory_info().rss)