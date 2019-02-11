def sum67(nums):
  suma = 0
  dodawaj = True
  
  for x in nums:
    if x != 6 and dodawaj:
      suma += x
    elif not dodawaj and x == 7:
      dodawaj = True
    else:
      dodawaj = False
      
  return suma

