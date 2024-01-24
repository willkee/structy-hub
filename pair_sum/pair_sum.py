def pair_sum(numbers, target_sum):
  
  nums = {}
  
  for i in range(len(numbers)):
    n = numbers[i]
    
    remainder = target_sum - n
​
    if (remainder in nums):
      return (i, nums[remainder])
    
    nums[n] = i