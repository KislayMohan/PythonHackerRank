class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

INT_MIN = -4294967296
INT_MAX = 4294967296

def check_binary_search_tree_(root):
    return check_btree(root, INT_MIN, INT_MAX)

def check_btree(node, min, max):
    if node is None:
        return True
    if node.data < min or node.data > max:
        return False
    
    return check_btree(node.left,min, node.data - 1) and check_btree(node.right, node.data + 1, max)

tree = node(5)
leftsub = node(1)
tree.left = leftsub
rightsub = node(7)
tree.right = rightsub

leftrightsub = node(6)
leftsub.right = leftrightsub

result = check_binary_search_tree_(tree)
print(result)