import time
import os, psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)
s=time.time()
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.root = None
        # self.tail = None
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
    # def rev_ll(self):
    #     temp = self.root
    #     # s = temp.next
    #     prev = None
    #     while True:
    #         if temp is None:
    #
    #             break
    #         # self.root = temp
    #
    #         s=temp.next
    #         print(self.root.data)

    def reverse(self):
        prev = None
        current = self.root
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.root= prev
    def display(self):
        c = self.root
        while True:
            if c is None:
                break
            print(c.data)
            c = c.next
p2 = Linked_list()
for i in range(1000):
    p1 = Node(3+i)
    p2.insert(p1)
p2.reverse()

p2.display()
e = time.time()
print(e-s)
process = psutil.Process(os.getpid())
print(process.memory_info().rss)