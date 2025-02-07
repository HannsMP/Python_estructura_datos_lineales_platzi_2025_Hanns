import random

""" 

ARRAY


"""

class Array:
  def __init__(self, capacity, fill_value=None):
    self.capacity = capacity

    if callable(fill_value):
      self.items = [fill_value(i) for i in range(capacity)]
    else:
      self.items = [fill_value for _ in range(capacity)]

  def __len__(self):
    return len(self.items)
  
  def __repr__(self):
    return f"<Array({self.capacity}) {hex(id(self))}>"

  def __str__(self):
    color = lambda t: f"\u001b[96m{t}\u001b[39m"

    result = f"{color('[')}"
    
    def parse_str(val):
      if isinstance(val, str):
        return f"'{val}'" 
      return val
    
    result = f"{result}{parse_str(self.items[0])}"
    for d in self.items[1:]:
      result = f"{result}, {parse_str(d)}"

    return f"{result}{color(']')}"
  
  def __iter__(self):
    return iter(self.items)
  
  def __getitem__(self, index):
    return self.items[index]
  
  def __setitem__(self, index, new_item):
    self.items[index] = new_item

  def fill_random(self, min, max, function_random=random.randint):
    for i in range(self.capacity):
      self.items[i] = function_random(min, max)

  def fill(self, value=None):
    for i in range(self.capacity):
      self.items[i] = value

  def join(self, separator=' '):
    result = self.items[0]
    
    for item in self.items[1:]:
      result = f"{result}{separator}{item}"

    return result
    
  def sum(self):
    result = 0

    for item in self.items:
      result = result + item

    return result

  def reduce(self, func, init_val=0):
    for index in range(0, self.capacity):
      init_val = func(init_val, self.items[index], index)

    return init_val
  
# menu = Array(4, lambda i: i)
# print(menu)
# print(repr(menu))

""" 

GRID


"""

class Grid():
  def __init__(self, rows, columns, fill_value=None):
    self.height = rows
    self.width = columns

    if callable(fill_value):
      self.data = Array(rows, lambda r: Array(columns, lambda c: fill_value(r, c)))
    else:
      self.data = Array(rows, lambda _: Array(columns, fill_value))

  def __getitem__(self, row, col=None):
    if col:
      return self.data[row][col]
    return self.data[row]
  
  def __setitem__(self, row, col, value):
    self.data[row][col] = value

  def __repr__(self):
    return f"<Grid({self.width}x{self.height}) {hex(id(self))}>" 
  
  def __str__(self):
    color = lambda t: f"\u001b[95m{t}\u001b[39m"

    result = f"{color('[')}"

    result += f"\n  {self.data[0].__str__()}"
    for row in self.data[1:]:
      result += f",\n  {row.__str__()}"

    return f"{result}\n{color(']')}"
  
  def fill_random(self, min, max, function_random=None):
    if function_random:
      for row in self.data:
        row.fill_random(min, max, function_random)
    else:
      for row in self.data:
        row.fill_random(min, max)

  def fill(self, value=None):
    for row in self.data:
      row.fill(value)

# matrix = Grid(4, 4, lambda r, c: f"{r}:{c}")
# print(repr(matrix))
# print(matrix)

""" 

CUBE


"""

class Cube():
  def __init__(self, x, y, z, fill_value=None):
    self.x = x
    self.y = y
    self.z = z

    if callable(fill_value):
      self.space = Array(x, lambda r:Grid(y, z, lambda h, s: fill_value(r, h, s)))
    else:
      self.space = Array(x, lambda _:Grid(y, z, fill_value))

  def __repr__(self):
    return f"<Cube({self.x}x{self.y}x{self.z}) {hex(id(self))}>" 
  
  def __str__(self):
    color1 = lambda t: f"\u001b[93m{t}\u001b[39m"
    color2 = lambda t: f"\u001b[95m{t}\u001b[39m"

    result = f"{color1('[')}"

    def parse_str(grid:Grid):
      res = f"{color2('[')}"

      res += f"{grid[0].__str__()}"
      for arr in grid[1:]:
        res += f", {arr.__str__()}"

      return f"{res}{color2(']')}"

    result += f"\n  {parse_str(self.space[0])}"
    for xs in self.space[1:]:

      result += f",\n  {parse_str(xs)}"

    result = f"{result}\n{color1(']')}"

    return result
  def fill_random(self, min, max, function_random=None):
    if function_random:
      for grid in self.space:
        grid.fill_random(min, max, function_random)
    else:
      for grid in self.space:
        grid.fill_random(min, max)

  def fill(self, value=None):
    for grid in self.space:
      grid.fill(value)
      
# rubik = Cube(3, 3, 3, lambda x, y, z: f"{x}:{y}:{z}")
# print(repr(rubik))
# print(rubik)