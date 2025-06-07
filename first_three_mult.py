#Here, I provide a function which prints the first three multiples of the parameter 'num'. It then returns the third multiple of num. 
#To become Interview ready, I've provided some pseudocode!
def first_three_multiples(num):
  temp = num
  for i in range(1, 4):
    print(temp * i)
  return temp * 3
# #FUNCTION first_three_multiples(num):
#     FOR i FROM 1 TO 3:
#         PRINT num * i
#     RETURN num * 3
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
