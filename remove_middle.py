def remove_middle(my_list, start, end):
  his_list = my_list[start:end +1]
  for i in range(len(his_list)):
    my_list.remove(his_list[i])
  return my_list

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
