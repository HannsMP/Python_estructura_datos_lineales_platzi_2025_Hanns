from structures.node import Node
""" 
FOFI
"""
class Stack:
  def __init__(self):
    self.top:Node = None
    self.bottom:Node = None
    self.size = 0

  def __repr__(self):
    return f"<Stack({self.size})>"
  
  def __str__(self):
    return str(self.top)
  
  def iter(self):
    probe = self.top

    while probe:
      yield probe
      probe = probe.child

  def push(self, data):
    new_node = Node(data)

    if self.top:
      new_node.set_child(self.top)
    else:
      self.bottom = new_node

    self.top = new_node
    self.size += 1

  def pop(self):
    if self.top:
      data = self.top.data

      if self.top.child:
        self.top = self.top.child
      else:
        self.top = None
        self.bottom = None

      self.size -= 1
      return data
    else:
      return None
    
  def peek(self):
    if self.top:
      return self.top.data
    else:
      return None
  def clear(self):
    self.top = None
    self.bottom = None