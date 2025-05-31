# Write your function here
def combine_sort(my_list1, my_list2):
  original = my_list1 + my_list2
  combined = sorted(original)
  return combined
  #.sort is mutating. In other words, it overwrites the previous list entirely.
  #.sort returns none
  #sorted(your_list) still creates a new list but maintains the older one. Gets lost in the heap (garbage collector) if not assigned to a variable

# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
