# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
def depth_first_values(root):
  if not root: return []
  
  my_list = []
  stack = [root]
  current = root
  
  while len(stack):
    curr = stack.pop()
    
    my_list.append(curr.val)
    
    if curr.right: stack.append(curr.right)
    if curr.left: stack.append(curr.left)
  
  return my_list