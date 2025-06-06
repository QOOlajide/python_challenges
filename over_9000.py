#returns the largest sum of the given list that just exceeds 9000
def over_nine_thousand(lst):
  my_sum = 0
  for i in range(len(lst)):
    my_sum += lst[i]
    if my_sum >= 9000:
      break
  return my_sum
    
