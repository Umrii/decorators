class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __str__(self):
        return f"CustomList with items: {self.items}"

    def __repr__(self):
        return f"CustomList({self.items})"

# Usage
clist = CustomList([1, 2, 3, 4])
print(len(clist))          # Output: 4
print(clist[2])            # Output: 3
clist[2] = 10
print(clist[2])            # Output: 10
del clist[2]
print(clist)               # Output: CustomList with items: [1, 2, 4]
print(repr(clist))         # Output: CustomList([1, 2, 4])
