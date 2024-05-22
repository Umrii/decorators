def decorator(function):
    def wrapper():
        xyz=function()
        yyz=xyz.upper()
        return yyz
    return wrapper
@decorator
def say_hi():
    return 'hey! how ya doing!'
print(say_hi())