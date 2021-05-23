class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Linked_list:
    def __init__(self):
        self.root = None
        self.tail = None

    def insert(self, ele):
        if self.root is None:
            self.root = ele
            self.tail = ele
        else:
            pre = None
            temp = self.root
            # global s
            s = None
            while True:
                if temp.next is None:
                    break

                s = temp

                temp = temp.next
                pre = temp
            temp.next = ele
            p = temp.next
            temp.prev = s
            self.tail = temp.next
            self.tail.prev = pre

    def reverse(self):
        temp = self.tail
        while True:
            if temp is None:
                break
            print(temp.data)
            temp = temp.prev
p2 = Linked_list()
for i in range(8):
    p1 = Node(i + 3)
    p2.insert(p1)
p2.reverse()