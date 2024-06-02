thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-2:-5])

# as list items cannot be mutated directly so they are mutated like this

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#unpacking a tuple, the asterisk variable takes all the remaining values as a list
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
