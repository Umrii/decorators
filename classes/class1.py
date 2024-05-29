class Employee:
    class_variable='Hi i am new here'
    def __init__(self,first,last,mail):
        self.first=first
        self.last=last
        self.mail=mail
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay*1.04)
    

emp_1=Employee('Anas','Atiq','mail.me')
emp_2=Employee('Anas','Atiq','mail.me')

emp_2.fullname()
#this is an example of an instance variable because each instance can send different value to the class

print(emp_2.class_variable) # this is a class variable, where we are directly accessing a shared variable from the class
print(Employee.fullname(emp_1))


