def intersection(a, b):
  answer = []
  
  longer_list = None;
  shorter_list = None;
  
  if len(a) > len(b):
    longer_list = set(a)
    shorter_list = b
  else:
    longer_list = set(b)
    shorter_list = a
  
  for num in shorter_list:
    if num in longer_list:
      answer.append(num)
  
  return answer