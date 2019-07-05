class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def path_from_root_to_node(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    TODO: complete this method and return a list containing values of each node in the path
    from root to the data node
    """
    pass

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2) 
root.right = BinaryTreeNode(3) 
root.left.left = BinaryTreeNode(4) 
root.left.right = BinaryTreeNode(5) 
print("Diameter of given binary tree is {}".format(diameter_of_binary_tree(root))) 