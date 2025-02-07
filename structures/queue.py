""" 
FIFO
"""
class ListQueue:
  def __init__(self):
    self.items = []

  @property
  def size(self):
    return len(self.items)

  def enqueue(self, data):
    self.items.insert(0, data)

  def dequeue(self):
    data = self.items.pop()
    return data
  
  def traverse(self):
    total_items = self.size

    for item in range(total_items):
      print(self.items[item])