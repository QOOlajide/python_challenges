#import the math library to use built-in functions to ocontrol for rounding up or down
import math
def round_sum(a, b, c):
    my_list = []
    my_list.extend([a, b, c])
    # for item in my_list:
    #     new_num = str(item)[-1]
    #     if new_num == "5":
    #         item = math.floor(item/10) * 10
    #     item = round(item, -1)
    # return sum(my_list)
    #Above doesn't actually chnage the values of the list. Item is just a COPY, not a reference!
    #Solution: Use indexing to access values directly
    # Check the rightmost digit of num
    for i in range(len(my_list)):
        remainder = my_list[i] % 10
        if remainder >= 5:
        # Round up to the next multiple of 10
            my_list[i] += (10 - remainder)
        else:
        # Round down to the previous multiple of 10
            my_list[i] -= remainder
  
    # Round each number and return the sum
    return sum(my_list)
