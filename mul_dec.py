def Subtract(function):
    def sub_wrapper():
        var=function()
        return var-1
    return sub_wrapper
    
def Add(function):
    def add_wrapper():
        var=function()
        return var+2
    return add_wrapper

@Add
@Subtract
def multiply():
    var=5
    return var
hello=multiply()
print(hello)