class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild= None
root = BST(50)
print(root)
print(root.lchild)
print(root.rchild)
print("%%%%%%%%%%%%%%%%")
rootlchild = BST(25)
print(root)
print(root.lchild)
print(root.rchild)
print("%%%%%%%%%%%%%%%%")
print(rootlchild)
print(rootlchild.lchild)
print(rootlchild.rchild)


# insertion of a node
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key ==data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else :
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    def search(self,data):
        if self.key == data:
            print("Node is found!")
            return
        if self.key >data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not found in a tree  --)")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not found in a tree  --)")
    def Preorder(self):
        print(self.key,end = "\t")
        if self.lchild:
            self.lchild.Preorder()
        if self.rchild:
            self.rchild.Preorder()
    def Postorder(self):
        if self.lchild:
            self.lchild.Postorder()
        if self.rchild:
            self.rchild.Postorder()
        print(self.key,end = "\t")
    def Inorder(self):
        if self.lchild:
           self.lchild.Inorder()
        print(self.key,end = "\t")
        if self.rchild:
            self.rchild.Inorder()
    def Delete(self,data):
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.Delete(data)
            else:
                print("Node is not present in left sub Tree")
        elif data >self.key:
            if self.rchild:
                self.rchild = self.rchild.Delete(data)
            else:
                print("Node is not present in right sub tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp1 = self.rchild
                self = None
                return temp1
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.Delete(node.key)
            return self


root = BST(50)
#root.insert(20)

list = [20,4,30,55,60,67,13]
for i in list:
    root.insert(i)
print("%%%%%%%%%%%")
root.search(13)
print("Preorder:")
root.Preorder()
print("\n")
print()
"""print("Postorder:")
root.Postorder()
print("\n")
print("Inorder:")
root.Inorder()"""
root.Delete(10)
print("after deleting the node:")
root.Preorder()


