# Given an input string, return the number of times that the string "code" appears anywhere in the string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(s):
    count = 0
    for i in range(len(s)):
        value = s[i : i + 4]
        if value[-1] == "e" and value[0:2] == "co":
            count +=1
    return count
