def upper_case(function):
    def wrapper():
        xyz=function()
        return xyz.upper()
    return wrapper

def say_hi():
    return 'I am okay'
hello=upper_case(say_hi)

print(hello())
    
