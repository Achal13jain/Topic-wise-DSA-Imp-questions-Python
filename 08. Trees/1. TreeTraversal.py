#Traverse a binary tree in different orders.
# Depth-First Search (DFS) can be classified into three main types 
# based on the order in which the nodes are visited
# Orders
# Inorder: Left → Root → Right
# Preorder: Root → Left → Right
# Postorder: Left → Right → Root

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val] 

# Time Complexity: O(n) 
# Space Complexity: O(n) (recursion stack)