"""
Implementation of Binary Search Tree
"""


class Node(object):

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Tree(object):

    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if(node==None):
            self.root = Node(value)

        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = Node(value)
                else:
                    self.insert(node.left, value)
            else:
                if(node.right==None):
                    node.right = Node(value)
                else:
                    self.insert(node.right, value)

    def printInOrder(self, node):
        if(node!=None):
            self.printInOrder(node.left)
            print(node.data)
            self.printInOrder(node.right)

    def printPreOrder(self, node):
        if(node!=None):
            print(node.data)
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    def printPostOrder(self, node):
        if(node!=None):
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(node.data)


def main():
    tree = Tree()
    tree.insert(tree.root, 15)
    tree.insert(tree.root, 10)
    tree.insert(tree.root, 25)
    tree.insert(tree.root, 5)
    print('In Order', tree.printInOrder(tree.root))
    print('Pre Order', tree.printPreOrder(tree.root))
    print('Post Order', tree.printPostOrder(tree.root))
    
    
main()
