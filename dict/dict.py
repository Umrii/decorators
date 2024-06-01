thisdict={

    'owner':'Anas',
    'car':'mustang',
    'model':'2012',
    'color':'blue'
}
print('keys:',thisdict.keys())
print('items:',thisdict.items())
print('values',thisdict.values())

thisdict['model']='2019'
thisdict['make']='toyota'

print(thisdict.items())
print(thisdict.get("model"))

if 'color' in thisdict:
    print('Yes color is present as a key in this dictionary as well')

thisdict.update({"model": 2020})

print(thisdict.items())

thisdict.pop("model")
print(thisdict.items())
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)
del thisdict["owner"]
print(thisdict)
for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x in thisdict.items():
  print(x)
for x, y in thisdict.items():
  print(x, y)
newdict=thisdict.copy()
print(newdict.items())

mydict = dict(thisdict)
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)