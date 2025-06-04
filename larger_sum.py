#This Python function returns the larger of the sums of the two lists passed into the parameter. If they are equal, must return the 1st list
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for st1 in lst1:
    sum1 += st1
  for st2 in lst2:
    sum2 += st2
  if sum1 >= sum2:
    return lst1
  return lst2
