#For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
#(i.e., t is concatenated with itself one or more times).

#Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
class Solution:
    def gcdOfStrings(str1: str, str2: str) -> str:
        x=len(str1)
        y=len(str2)
        count=0
        for i in range(min(x,y)):
            if(str1[i]==str2[i]):
                count=count+1
        print(count+1)
        print("not okay")
word1="ABCABCABC"
word2="ABC"
obj=Solution
# obj.gcdOfStrings(word1,word2)
#Check if one string can be constructed by repeating the other: A string t divides string s if and only if s can be constructed 
#by concatenating multiple copies of t. For example, "ABC" divides "ABCABC" because "ABCABC" = "ABC" + "ABC".

#Find the GCD of the lengths of the strings: If the lengths of str1 and str2 are len1 and len2, respectively, we compute the GCD 
#of these two lengths. This GCD will help us determine the potential length of the common divisor string.

#Check if the potential common divisor string actually divides both strings: Once we determine the potential length of the common
# divisor string, we construct the string by taking the first GCD(len1, len2) characters of str1 (or str2 since they should be the
# same if they both divide the strings). Then, we verify if this string can indeed divide both str1 and str2.

    
#Example 1:

#Input: str1 = "ABCABC", str2 = "ABC"
#Output: "ABC"
#Example 2:

#Input: str1 = "ABABAB", str2 = "ABAB"
#Output: "AB"
#Example 3:

#Input: str1 = "LEET", str2 = "CODE"
#Output: ""