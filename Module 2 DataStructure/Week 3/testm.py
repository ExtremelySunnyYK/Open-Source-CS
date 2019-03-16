class TreeOrders:
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
    >>> [x for x in tree.preOrder()]
    [4, 2, 1, 3, 5]
    >>> # Explanation:
    >>> #
    >>> #       root
    >>> #         4
    >>> #        / \
    >>> #       2   5
    >>> #      / \
    >>> #     1   3
  """  
  
  def read(self):
    self.n = int(input())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    #creates 3 list(key,left,right) that stores the input value of key,left,right
    for i in range(self.n):
      [a, b, c] = map(int, input().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

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
    
    if self.right[index] != -1:
        self.inOrderTraversal(self.right[index])
        
  def preOrder(self):
    self.result = []
    self.preOrderTraversal(0)           
    return self.result

  def preOrderTraversal(self,index):
      if self.key != -1:
          self.result.append(self.key[index])
      if self.left[index] != -1:    
          self.preOrderTraversal(self.left[index])
      if self.right[index] != -1:
          self.preOrderTraversal(self.right[index])
           
          
  def postOrder(self):
    self.result = []
    self.postOrderTraversale(0)            
    return self.result 

  def postOrderTraversal(self,index):
        if (self.left[index] != -1):
          self.postOrderTraversal(self.left[index])
        if (self.right[index] != -1):
          self.postOrderTraversal(self.right[index])
        self.result.append(self.key[index])
    
def main():
  
  tree = TreeOrders()
  tree.read()
  print(" ".join(str(x) for x in tree.inOrder()))
  print(" ".join(str(x) for x in tree.preOrder()))
  print(" ".join(str(x) for x in tree.postOrder()))


if __name__ == '__main__':
  import doctest
  doctest.testmod()