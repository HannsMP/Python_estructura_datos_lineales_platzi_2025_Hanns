from structures.node import Node

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  def enqueue(self, data):
    new_node = Node(data)

    if self.head:
      self.tail.set_child(new_node)
      self.tail = new_node
    else:
      self.head = new_node
      self.tail = new_node
      
    self.count += 1

  def dequeue(self):
    if self.count <= 0:
      return None
    
    current = self.head
    if self.count == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.child
      self.head.parent = None

    self.count -= 1
    return current.data