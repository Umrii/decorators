#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

#Return the merged string.

word1="abcdef"
word2="xyz"
arr=[]
def append_array(word1,word2):
    x=len(word1)
    y=len(word2)
    for i in range(min(x,y)):
        arr.append(word1[i])
        arr.append(word2[i])
    if x > y:
        arr.append(word1[y:])
        # say x=5 and y=3, so the above piece of code will slice the word1 after index 2 and appendthe rest to the array
    else:
        arr.append(word2[:x])
         # say x=2 and y=4, so the above piece of code will slice the word2 after index 1 and appendthe rest to the array
    return ''.join(arr)
print(append_array(word1,word2))
#Example 1:

#Input: word1 = "abc", word2 = "pqr"
#output: "apbqcr"
#Explanation: The merged string will be merged as so:
#word1:  a   b   c
#word2:    p   q   r
#merged: a p b q c r