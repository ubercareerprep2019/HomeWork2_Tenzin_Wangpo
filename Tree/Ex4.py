class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data  = data
        self.left  = left
        self.right = right

    def getData(self):
        return self.data

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)  #need to chnjlkjh
        else:
            self.insertHelper(key, self.root)

    @staticmethod
    def insertHelper(key, currentRoot):
        if currentRoot is None:
            currentRoot = TreeNode(key)
            return

        elif key >= currentRoot.getData():
            if currentRoot.right is None:
                currentRoot.right = TreeNode(key)
                return
            BinarySearchTree.insertHelper(key, currentRoot.right)

        else:
            if currentRoot.left is None:
                currentRoot.left = TreeNode(key)
                return
            BinarySearchTree.insertHelper(key, currentRoot.left)

    def find(self, key):
        return self.findHelper(key, self.root)

    @staticmethod
    def findHelper(key, currentRoot):
        if currentRoot is None:
            return False

        elif currentRoot.getData() == key:
            return True

        elif key >= currentRoot.getData():
            return BinarySearchTree.findHelper(key, currentRoot.right)

        else:
            return BinarySearchTree.findHelper(key, currentRoot.left)

def testing():
    myBST = BinarySearchTree()
    #when BST is empty
    print(myBST.find(10))
    insertList = [16,10,21,7,29,18,13,99]
    for i in insertList:
        myBST.insert(i)

    print(myBST.root)
    print(myBST.find(21))
    print(myBST.find(99))
    print(myBST.find(1))

if __name__ == "__main__":
    testing()