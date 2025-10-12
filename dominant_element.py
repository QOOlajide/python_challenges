def majorityElement(nums):
#Input: Given a list, return an integer
#We only care about the integer that appears more than half of the time, so we know that can only be one integer, unless...
#Edge cases: Can we assume that this list won't be empty? That it won't have falsy values? That it'll have a length of at least three? If so, we can proceed. But hod on, lets go back a bit.. Can we even be sure that our inputs wi always represent an actual integer and not a nummber that is a string? Yes, we can, as the problem states we're given a lsit of numbers and that the element exists in the list. But, if the list has a length of 1, we return that value. if the list is a length of two and the values are different, we return 0. Otherwise, we return the single value that occurs in the array. We'd likely have to traverse the array and find a way to remember the frequency of the values in the array. We traverse the array and increment the key value pairs each time we see the same value. Finally, we'd have to reutrn the value that occurred the most. Might occur by extracting the values andchecking which one is greater than half the lenght of the array.
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        if nums[0] != nums[1]:
            return 0
        else:
            return nums[0]

    seen = {}
    for x in nums:
        if x in seen:
            seen[x] += 1
        else:
            seen[x] = 1
    
    #for x in seen.values():
    #    if x > len(nums) // 2:
    #        return x #but, what are you returning? You're returning the actual
    for x in seen:
        if seen[x] > len(nums) // 2:
            return x
            
