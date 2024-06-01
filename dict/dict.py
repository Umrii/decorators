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
