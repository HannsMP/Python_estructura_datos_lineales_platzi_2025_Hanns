class Node:
  def __init__(self, data, child=None, parent=None):
    self.data = data
    self.child:Node = child
    self.parent:Node = parent

  def set_child(self, node):
    self.child = node
    node.parent = self

  def set_parent(self, node):
    self.parent = node
    node.child = self

  def __repr__(self):
    if isinstance(self.child, Node):
      return f"<Node({self.data}) {hex(id(self))}> -> Node({self.child.data})"
    else:
      return f"<Node({self.data}) {hex(id(self))}> -> {self.child}"
    
  def __str__(self):
    if isinstance(self.child, Node):
      return f"Node({self.data}) -> {self.child.__str__()}"
    else:
      return f"Node({self.data}) -> {self.child}"
""" 

SinglyLinkedList
  el primer agregado es el tail
  el ultimo agregado es el head

"""
class SinglyLinkedList:
  def __init__(self):
    self.head:Node = None
    self.tail:Node = None
    self.size = 0

  def __repr__(self):
    return f"<SinglyLinkedList({self.size}) {hex(id(self))}>"
  
  def __str__(self):
    if self.head:
      return self.head.__str__()
    else:
      return "None"

  def empty(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def iter(self):
    probe = self.head

    while probe:
      yield probe
      probe = probe.child

  def has(self, data):
    for current_node in self.iter():
      if current_node.data == data:
        return True
    return False

  def append_head(self, data):
    new_node = Node(data)

    if self.head:
      new_node.set_child(self.head)
    else:
      self.tail = new_node

    self.head = new_node
    self.size += 1

  def append_tail(self, data):
    new_node = Node(data)

    if self.tail:
      new_node.set_parent(self.tail)
    else:
      self.head = new_node

    self.tail = new_node
    self.size += 1

  def append_index(self, index, data):
    if index == 0:
      return self.append_head(data)
    if index == self.size:
      return self.append_tail(data)
    if index > self.size:
      return

    new_node = Node(data)
    i = 0
    for node in self.iter():
      if i == index:
        node.parent.set_child(new_node)
        new_node.set_child(node)
      i+=1

    self.size += 1

  def replace(self, find_data, new_data):
    for current_node in self.iter():
      if current_node.data == find_data:
        current_node.data = new_data
        return True
    return False

  def delete(self, data):
    state = False
    for node in self.iter():
      if node.data == data:
        state = True

        if self.size == 1:
          self.empty()
          break
        if node.parent == None:
          self.head = self.tail = node.child 
          break
        if node.child == None:
          self.head = self.tail = node.parent
          break

        node.parent.set_child(node.child)

    return state
  
  def remove_index(self, index):
    if index == 0:
      return self.remove_head()
    if index == self.size:
      return self.remove_tail()
    if index > self.size:
      return

    i = 0
    for node in self.iter():
      if i == index:
        node.parent.set_child(node.child)
      i+=1

    self.size -= 1
  
  def remove_head(self):    
    if self.head == None:
      return True, None
    
    remove_item = self.head
    self.head = remove_item.child
    
    self.size -= 1
    return True, remove_item
  
  def remove_tail(self):
    remove_item = self.tail
    self.tail = remove_item.parent
 
    self.size -= 1
    return remove_item
""" 

DoubleLinkedList

"""
class DoubleLinkedList(SinglyLinkedList):
  def __init__(self):
    super().__init__()

  def __repr__(self):
    return f"<DoubleLinkedList({self.size}) {hex(id(self))}>"
  
  def iter_tail(self):
    probe = self.tail

    while probe:
      yield probe
      probe = probe.parent
""" 

CircularLinked

"""
class CircularLinked:
  def __init__(self):
    self.head = None
    self.size = 0

  def __repr__(self):
    return f"<CircularLinked({self.size}) {hex(id(self))}>"
  
  def __str__(self):
    if self.head:
      iter_child = self.iter_child()
      result = f"┌┬▸({next(iter_child).data})\n"
      for node in iter_child:
        result += f"│├▸({node.data})\n"
      result += "└┘"
      return result
    else:
      return 'None'

  def iter_child(self):
    head = self.head
    yield head

    probe = head.child
    while probe != head:
      yield probe
      probe = probe.child

  def iter_parent(self):
    tail = self.head.parent
    yield tail

    probe = tail.parent
    while probe != tail:
      yield probe
      probe = probe.parent

  def apend(self, data):
    new_node = Node(data)

    if self.head:
      new_node.set_parent(self.head.parent)
      new_node.set_child(self.head)
    else:
      new_node.set_child(new_node)

    self.head = new_node
    self.size += 1