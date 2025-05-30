#This function checks if a given item appears in the list more than 'n' times.
# It manually counts occurrences using a loop, returning True if the count 
# exceeds 'n', and False otherwise.
def more_than_n(my_list, item, n):
  count = 0
  for i in range(len(my_list)):
    if my_list[i] == item:
      count += 1
  if count > n:
    return True
  return False

# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
