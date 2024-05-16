# Python program to implement Singly Linked List with operations for prepending nodes, appending 
# nodes and traversing nodes



class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Singlylinkedlist:
    def __init__(self):
        self.head=None

    def traverse(self):
        current=self.head
        while current:
            print(current.data , end=" ->")
            current=current.next
        print("None")

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current =self.head
        while current.next:
            current = current.next
        current.next=new_node


    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node



# dirve code
linked_list=Singlylinkedlist()

linked_list.append(10)
linked_list.append(20)
linked_list.prepend(9)
linked_list.prepend(8)
linked_list.prepend(7)


print("mylinked list after appending and prepending")
mylist=linked_list.traverse()