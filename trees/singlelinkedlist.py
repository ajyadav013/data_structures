"""
Single Linked List
"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nxt = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, node, value):
        if(node==None):
            self.head = Node(value)
        else:
            self.head = node.nxt
        
    def printLinkedList(self, node):
        if(node!=None):
            print(node.value)
            self.printLinkedList(node.nxt)


        

def main():
    linkedList = LinkedList()
    linkedList.insert(linkedList.head, 10)
    linkedList.insert(linkedList.head, 20)
    linkedList.insert(linkedList.head, 30)
    linkedList.printLinkedList(linkedList.head)

main()
