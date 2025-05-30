# This function compares two lists and returns the last element of the longer list.
# If both lists are the same length, it returns the last element of the first list.def larger_list(my_list1, my_list2):
  if len(my_list1) > len(my_list2):
    return my_list1[-1]
  elif len(my_list2) > len(my_list1):
    return my_list2[-1]
  return my_list1[-1]

# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
