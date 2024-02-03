# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
def breadth_first_values(root):
  if not root: return []
  stack = [root]
  my_list = []
  
  while stack:
    curr = stack.pop(0)
    my_list.append(curr.val)
    
    if curr.left: stack.append(curr.left)
    if curr.right: stack.append(curr.right)
  
  return my_list
​