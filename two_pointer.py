def isVowel(c):
    check_list = ["a", "e", "i", "o", "u"]
    if c.lower() in check_list:
        return True 
    
def how_many_vowels(s):
    count = 0
    for char in s:
        if char == "a" or char == "i" or char == "e" or char == "u" or char == "o":
            count += 1
    return count

def reverse_vowels(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    if how_many_vowels(s) < 2:
        print("Cannot swap anything because there are either no vowels or not enough" \
        "to actually perform at least one vowel swap. Returning an empty string")
        return ""
    elif not s:
        return "Invaid input"
    else: 
        ready_to_swap = False
        while left < right:
            if isVowel(s[left]) == True:
                ready_to_swap = True
            else:
                left += 1
            if isVowel(s[right]) == True and ready_to_swap == True:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -=1
                ready_to_swap = False
            elif isVowel(s[right]) == True and ready_to_swap == False:
                ready_to_swap == True
            else:
                right -=1
    return "".join(s) 

               
s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)
