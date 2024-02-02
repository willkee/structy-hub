class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
​
def add_lists(h1, h2):
  curr1 = h1
  curr2 = h2
  
  prev = None
  
  carry_over = 0
  
  while curr1:
    
    c2 = None
    if curr2: c2 = curr2.val
    else: c2 = 0
  
    if carry_over > 0:
      curr_sum = curr1.val + c2 + carry_over
      if curr_sum < 10:
        carry_over = 0
      else:
        carry_over = curr_sum // 10
    else:
      curr_sum = curr1.val + c2
      
    carry_over = curr_sum // 10
    last_digit = int(str(curr_sum)[-1])
    curr1.val = last_digit
    
    prev = curr1
    curr1 = curr1.next
    if curr2: curr2 = curr2.next
  
  if carry_over > 0: prev.next = Node(carry_over)
    
  return h1
​
    curr2 = curr2.next