thislist=['apple','banana','citrus']

print(thislist)
print(len(thislist))

print(thislist[0])

print(thislist[0:2]) # The search will start at index 0 (included) and end at index 2 (not included).

#This example returns the items from the beginning to, but NOT including, "citrus":

print(thislist[:3])

print(thislist[0:]) #This example returns the items from begining to the end:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist.insert(2, "watermelon") # To insert a new list item, without replacing any of the existing values, we can use the insert() method.

#The insert() method inserts an item at the specified index:
print(thislist)


thislist[1:3] = ["blackcurrant", "watermelon"] # 1 and 2 index are changed, 3 is excluded
print(thislist)
thislist.append("orange")
print(thislist)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist.remove("papaya")
#If there are more than one item with the specified value, the remove() method removes the first occurrence:
print(thislist)

thislist.pop(0) #If you do not specify the index, the pop() method removes the last item.
print(thislist)

del thislist[1]
print(thislist)


 
for i in range(len(thislist)):
  print(thislist[i])
# list comprehensions

# if not used 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#using them

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
#newlist = [expression for item in iterable if condition == True]
print(newlist)

thislist.sort(reverse = True)
print(thislist)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)