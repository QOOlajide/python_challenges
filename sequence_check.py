def checkSubsequence(s, t):
    #Task: We'd like to check to see whether or not you can derive the substring s from t. For this, we actually care about the sequence. In other words, it isn't sufficine to just check whether certain numbers are inside the larger subsequence
    #Edge Cases: If t is less than s, if both are falsy, if s is one value, which eases the process of us searching by manually checking. We could create an entire array an iterate through each value inside the larger array. If it is inside of the smaller array, then we add it to a new string array, then at the end we check to compare the two arrays and see if they're equal. Now, this can work, but this increases space complexity, and we don't want that!

    #Let's think through it logically. We have one letter, say a. We surely have to go through the larger array. I'm thinking of creating a dictionary. This is undoubtedly a two-pointer problem, as we're simply traversing two things and checking the order of them, without changing anything. 
    #Initialize two pointers
    #Create a while loop, whereby we'll conitune to move both pointers so long as the first pointer for the first string is less than its length. If it isn't, then we know that the correct subsequence doesn't exist and can return false outside of the while loop!
    #otherwise, within the while loop, create a conditional. If the array[pointer1] == array[pointer2], then we iterate pointer 1 and pointer 2, else, we simply iterate pointer2. Seems like we have to add another conditional, and that is if pointer2 is less than the length of the bigger substring. Once one of these are false, then we exit the loop. Anyway, in our else, we just only iterate pointer 2. Since we have two consditionals, we're going to need to perform a check outside the while loop to verify if we have a substring. In terms of the length, we can try by seeing of the pointer value of s is equal to the length of s. We can put this inside a return statement, as the result will tell us whether we have a substring or not.
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(s) and pointer2 < len(t):
        if s[pointer1] == t[pointer2]:
            pointer1 += 1
        pointer2 += 1 #will always iterate pointer2 in both instances
    return pointer1 == len(s)
