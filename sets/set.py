# Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Duplicates Not Alloweds

#the elements themselves must be immutable. This means that you cannot have mutable objects like lists or dictionaries 
#as elements within a set. However, immutable objects like integers, strings, and tuples are perfectly acceptable as elements
# in a set.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#Note: If the item to remove does not exist, discard() will NOT raise an error, remove will raise an error
#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#You can use the | operator instead of the union() method, and you will get the same result.
# join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#The update() method inserts all items from one set into another.

#The update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#Both union() and update() will exclude any duplicate items.

#set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#You can use the & operator instead of the intersection() method, and you will get the same result.

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
#Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)