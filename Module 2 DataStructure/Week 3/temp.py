class TreeOrders():
     
 def inOrder(self):
    self.result = []
    #starts from root
    self.inOrderTraversal(0)     
    return self.result

 def inOrderTraversal(self,index):
    #Left,Key,Right
    
    if self.left[index] != -1:
        self.inOrderTraversal(self.left[index])
    self.result.append(self.key[index])
    
    if self.left[index] != -1:
        self.inOrderTraversal(self.right[index])
def main():
  """Binary tree traversals.
    Builds and outputs in-order, pre-order and post-order traversals of
    a rooted binary tree.
    Samples:
    >>> tree = TreeOrders()
    >>> tree.key = [4, 2, 5, 1, 3]
    >>> tree.left = [1, 3, -1, -1, -1]
    >>> tree.right = [2, 4, -1, -1, -1]
    >>> [x for x in tree.inOrder()]
    [1, 2, 3, 4, 5]
    >>> # Explanation:
    >>> #
    >>> #       root
    >>> #         4
    >>> #        / \
    >>> #       2   5
    >>> #      / \
    >>> #     1   3
  """  
  tree = TreeOrders()
  tree.key = [4, 2, 5, 1, 3]
  tree.left = [1, 3, -1, -1, -1]
  tree.right = [2, 4, -1, -1, -1]
  print(" ".join(str(x) for x in tree.inOrder()))