# def sum78(nums):
#     #plan: find the location of the end, then use list slicing 
#     my_sum = 0
#     if 7 not in nums and 8 not in nums:
#         return sum(nums)
#     for i in range(len(nums)):
#         # while num != 7
#         if nums[i] == 7 or nums[i] == 8
#             continue
#         my_sum += nums[i]
#     return my_sum
def sum78(nums):
    # Initialize sum to 0 and a flag to monitor if we are in a 7-8 section
    total_sum = 0
    in_section = False
    for num in nums:
        if num == 7:
            # If we find a 7, set the flag to True to start ignoring numbers
            in_section = True
        elif num == 8 and in_section:
            # If we find an 8 and we are in a section, end the section
            in_section = False
        elif not in_section:
            # If we are not in a section, add the number to the sum
            total_sum += num

    return total_sum
