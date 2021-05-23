class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class Linked_list:
    def __init__(self):
        self.root = None
        self.tail = None
    def insert(self,ele):
        if self.root is None:
            self.root = ele
        else:
            pre = None
            temp = self.root
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
    def search(self):
        ele = int(input('enter : '))
        temp = self.root
        c=1
        while True:
            if temp.data == ele:
                print(c,'th Noode')
                break
            c+=1
            print(temp.data)
            temp = temp.next
p2 = Linked_list()
for i in range(8):
    p1 = Node(i + 3)
    p2.insert(p1)
p2.search()