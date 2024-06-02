#without a decorator
def upper_case(function):
    def wrapper():
        xyz = function()
        yyz = xyz.upper()
        return yyz
    return wrapper

def say_hi():
    return "I am okay"


upper_case_wrapper = upper_case(say_hi)
result = upper_case_wrapper()
print(result)  

# 
# using decorator
def upper_case(function):
    def wrapper():
        xyz = function()
        return xyz.upper()
    return wrapper

@upper_case
def say_hi():
    return 'I am okay'


hello = say_hi()
print(hello)




    
