#This function is designed to remove elements from a list starting from one index to another index while returning the new list. A sophisticated approach, don't you think!
#Thinking of a more efficient example of this...
def remove_middle(my_list, start, end + 1):
  his_list = my_list[start:end +1]
  for i in range(len(his_list)):
    my_list.remove(his_list[i])
  return my_list

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
#Should return [4, 23, 42], but run it yourselves in codespaces or VSCode!

#Update, this can only work for non-duplicate values! Clearly need a new solution...
