# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data), 'please check the numbers inputted'

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])
   
#more efficent algorithim using sift down and build heap
  def FastSwap(self):
    for i in range(int(len(self._data)/2),-1,-1):
      self.SiftDown(i)

  def SiftDown(self, i):
    minIndex = i
    l = 2*i + 1
    if(l < len(self._data) and self._data[l] < self._data[minIndex]):
      minIndex = l
    r = 2*i + 2
    if(r < len(self._data) and self._data[r] < self._data[minIndex]):
      minIndex = r
    if(i!=minIndex):
      self._swaps.append((i, minIndex))
      self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
      self.SiftDown(minIndex)
#         size = len(self._data)
#         min_index = i
#         l = 2*i + 1 #leftchild(i)
#         if (l < size and self._data[l]<self._data[min_index]):
#             min_index = l
#         
#         r = 2*i + 2
#         if (r < size and self._data[r]<self._data[min_index]):
#             min_index = r
#         if i != min_index:
#        #swap array[i] and array[minindex]
#            self._swaps.append((i,min_index))
#            self._data[i],self._data[min_index] = self._data[min_index],self.data[i]
#            self.SiftDown(min_index)


          
      

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]
          

  def Solve(self):
    self.ReadData()
    #self.GenerateSwaps()
    self.FastSwap
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
