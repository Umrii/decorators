word1 = "ab"
word2 = "pqrs"

arr=[]


def mergeAlternately(word1,word2):
    x=len(word1)
    y=len(word2)
    for x in range(min(x,y)):
        arr.append(word1[x])
        arr.append(word2[x])
        
    if x > y:
        arr.append(word1[y:])
    else:
        arr.append(word2[x:])
    return ''.join(arr)
print(mergeAlternately(word1,word2))
    