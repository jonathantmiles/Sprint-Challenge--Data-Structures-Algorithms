class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # initial setup
    nodes = []
    values = []
    current_node = self
    nodes.append(current_node)
    values.append(current_node.value)
    while len(nodes) > 0:
        # each time there's a left node to explore
        while current_node != None:
            nodes.append(current_node.left)
            if current_node.left:
                values.append(current_node.left.value)
                print(current_node.value)
            current_node = current_node.left
        # when the left side is exhausted, back up by one and check the right
        while current_node == None:
            if nodes[-1] == None:
                nodes.pop(-1)
            if len(nodes) == 0:
                break
            print(len(nodes))
            current_node = nodes[-1]
            print(current_node)
            print(nodes)
            # since we pop each time there's a right fork, we trend towards empty
            nodes.pop(-1)
            nodes.append(current_node.right)
            if current_node.right:
                values.append(current_node.right.value)
                print(current_node.value)
            current_node = current_node.right
    return cb(values.copy())

  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
