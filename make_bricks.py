#!/usr/bin/python3.6

'''
  We want to make a row of bricks that is goal inches long.
  We have a number of small bricks (1 inch each) and big bricks (5 inches each).
  Return True if it is possible to make the goal by choosing from the given bricks.
  This is a little harder than it looks and can be done without any loops.
'''

def make_bricks(small, big, goal):
  big_len = big * 5
  if small + big_len < goal:
    return False
  elif small + big_len == goal or small == goal or big_len == goal:
    return True
  else:
    if big_len < goal:
      return big_len + small >= goal
    else:
      return goal % 5 <= small
      
# sample tests

print(make_bricks(3, 1, 8))	# True
print(make_bricks(3, 1, 9))	# False
print(make_bricks(3, 2, 10))	# True
print(make_bricks(3, 3, 12))	# True
print(make_bricks(3, 3, 14))	# False
