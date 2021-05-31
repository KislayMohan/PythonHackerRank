class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


def check_binary_search_tree_(root):
    if root is None:
        return True
    if root.left is not None and root.data <= root.left.data:
        return False
    if root.right is not None and root.data >= root.right.data:
        return False

    leftres = check_binary_search_tree_(root.left)
    rightres = check_binary_search_tree_(root.right)

    return leftres and rightres;

tree = node(5)
leftsub = node(1)
tree.left=leftsub
rightsub=node(3)
tree.right=rightsub

result = check_binary_search_tree_(tree)
print(result)