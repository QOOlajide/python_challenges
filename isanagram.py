# Determine if two provided words are anagrams of each other.
# An anagram is defined as a word obtained by rearranging the letters of another word, using all the original letters exactly once.
# For this verification, input consists of two strings: 's' representing the first word, and 't' for the second word.
# The goal is to return true if 't' is an anagram of 's', otherwise, return false.
 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
 
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
 
# Constraints:
# - The length of both strings 's' and 't' will be in the range of 1 to 50,000.
# - Both strings will contain only lowercase English letters.

def is_anagram(s, t):
    #Input: Two Strings. Potential Edge cases: If strings are null or if we have minimum values, like only one character. Another case is if they are equal to each other
    #We only need to check if each of the letters in one string are present within the others
    #In other words, arrangement doesn't matter, however, we want to make sure certain values (characters appear the exact same number of times)

    #Plan. First, i'D need a way to store these into a data structure which can track whether or not values have been repeated. If values have bees
    if not s or not t:
        return 
    if s == t:
        return True
    #A common theme: Check if length for something may be crucial
    if len(s) != len(t):
        return False
    my_dict = {}
    for char in s:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1  
    for char in t:
        #For each character, if the character count matches the charater count of the other 
        #string, then we have an anagram. However, this will be too tediuous to track, so what we do is the opposite. we check each character and use the negation, in other words, if that char occurs more than the amount of times in the previous string, we will return false. Outside of this, we will return true.
        if char not in my_dict or my_dict[char] == 0:
            return False #for the second condition, this means that decrementing further will have an uneven amount of letters that don't match in terms of quantity
        my_dict[char] -= 1 #Start decrementing to see if all of the values can get to zero
    return True
