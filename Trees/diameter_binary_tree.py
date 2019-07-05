class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def height(node): 
      
    # Base Case : Tree is empty 
    if node is None: 
        return 0 
      
    # If tree is not empty then height = 1 + max of left  
    # height and right heights  
    return 1 + max(height(node.left) ,height(node.right)) 


def diameter_of_binary_tree(root):
    """
    :param: root - Root of binary tree
    TODO: Complete this method and return diameter (int) of binary tree
    """
    # Base Case when tree is empty  
    if root is None: 
        return 0 
  
    # Get the height of left and right sub-trees 
    lheight = height(root.left) 
    rheight = height(root.right) 
  
    # Get the diameter of left and irgh sub-trees 
    ldiameter = diameter_of_binary_tree(root.left) 
    rdiameter = diameter_of_binary_tree(root.right) 
  
    # Return max of the following tree: 
    # 1) Diameter of left subtree 
    # 2) Diameter of right subtree 
    # 3) Height of left subtree + height of right subtree +1  
    return max(lheight + rheight + 1, max(ldiameter, rdiameter)) 

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2) 
root.right = BinaryTreeNode(3) 
root.left.left = BinaryTreeNode(4) 
root.left.right = BinaryTreeNode(5) 
print("Diameter of given binary tree is {}".format(diameter_of_binary_tree(root))) 