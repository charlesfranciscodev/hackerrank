""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return check_node(root, -1, 10001)

def check_node(node, min_data, max_data):
    if (node is None):
        return True
    if (node.data <= min_data or node.data >= max_data):
        return False
    return check_node(node.left, min_data, node.data) and check_node(node.right, node.data, max_data)
