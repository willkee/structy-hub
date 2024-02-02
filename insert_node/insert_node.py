class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
​
def insert_node(head, value, index):
  if index == 0:
    new_node = Node(value)
    new_node.next = head
    return new_node
  
  current_index = 0
  prev = None
  current = head
  
  while current is not None:
    if current_index == index:
      print(index, current.val, prev.val)
      new_node = Node(value)
      prev.next = new_node
      new_node.next = current    
      return head
    else:
      prev = current
      current = current.next
    current_index += 1
  
  prev.next = Node(value)
  return head
​