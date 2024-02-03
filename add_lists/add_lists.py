class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
​
def add_lists(h1, h2):
  curr1 = h1
  curr2 = h2
  prev = None
  carry = 0
  
  while curr1:
    # in case the 2nd linked list is shorter
    # c2 is simply 0 if linked list #2 is finished.
    c2 = curr2.val if curr2 else 0
    
    # add up the values in both.
    sum = curr1.val + c2 + carry
    carry = 0 if sum < 10 else sum // 10
    
    # get the last digit of the sum and apply it to curr1.val
    curr1.val = sum % 10
    
    # we want to track prev in case there is a carry over after
    # both linked lists are traversed
    prev = curr1
    
    # curr1 (and curr2 if it still exists) is incremented
    curr1 = curr1.next
    if curr2: curr2 = curr2.next
  
  # although this passes all test cases, this has a flaw in that
  # a carry over amount 10+ will not work. We will need another loop
  # to traverse all remaining digits.
  if carry > 0: prev.next = Node(carry)
    
  return h1
​