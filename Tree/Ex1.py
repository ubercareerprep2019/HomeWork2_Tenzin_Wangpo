class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data  = data
        self.left  = left
        self.right = right

    def getData(self):
        return self.data


class Tree:
    def __init__(self, root ):
        self.root = root

    # print method override for Tree
    def print(self, order="inorder"):
        """
        defualt traversal order is inorder, user can change the traversal order as they want
        """
        self.printTree(self.root, order)

    # Helper method for print function
    @staticmethod
    def printTree(root, order):
        if order == "inorder":
            #base case
            if root == None:
                return
            Tree.printTree(root.left, "inorder")
            print(root.getData(), end = " ")
            Tree.printTree(root.right, "inorder")

        elif order == "preorder":
            if root == None:
                return
            print(root.getData(), end = " ")
            Tree.printTree(root.left, "preorder")
            Tree.printTree(root.right, "preorder")

        elif order == "postorder":
            if root == None:
                return
            Tree.printTree(root.left, "postorder")
            Tree.printTree(root.right, "postorder")
            print(root.getData(), end = " ")

        else:
            # raise exception will offer a clue about what went wrong
            raise Exception("ERROR:  {} is not a type of Tree Traversals order".format(order))


leftChild = TreeNode(6)
rightChild = TreeNode(3)
left = TreeNode(7)
right = TreeNode(17, leftChild, rightChild)
root = TreeNode(1, left, right)

tree = Tree(root)

print("Tree traversal in inorder: ", end = " ")
tree.print()
print("\n")

print("Tree traversal in preorder: ", end = " ")
tree.print("preorder")
print("\n")

print("Tree traversal in postorder: ", end = " ")
tree.print("postorder")
print("\n")

""" ---------------- RUN --------------------

Tree traversal in inorder:  7 1 6 17 3 

Tree traversal in preorder:  1 7 17 6 3 

Tree traversal in postorder:  7 6 3 17 1 
"""

