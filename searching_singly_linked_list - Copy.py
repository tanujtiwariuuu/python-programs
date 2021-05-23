class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None
class Linked_list:
    def __init__(self):
        self.root = None
    def insert(self,dataa):
        if self.root is None:
            self.root = dataa
        else:
            temp = self.root
            while True:
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = dataa
    def search(self,ele=4):
        c=0
        if self.root.data == ele:
            c+=1
            print(1,' st Node')
        else:

                c+=1
                temp = self.root

                while True:
                    try:
                        if temp.data is ele:
                            print(c,'th Node')
                            break
                        temp = temp.next
                        c+=1
                    except :
                        print('not found ')
                        break

p1 = Linked_list()
for i in range(7):
    p2 = Node(i+1)
    p1.insert(p2)
p1.search()