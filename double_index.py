#Doubles the desired value at a certain index and returns the new list without modifying its original values. Uses the method count, though
#could use list slicing.
#Write your function here
def double_index(my_list, index):
  if index < 0 or index >= len(my_list):
    return my_list
  new_list = my_list.copy()
  new_list[index] = new_list[index] * 2
  return new_list
  #Nice, but modifies the original input of the list. Instead, can perform the following


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
