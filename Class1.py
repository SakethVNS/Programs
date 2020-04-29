#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:15:42 2020

@author: sakethvns
"""


"""Why classes??

logically group data and functions to reuse and easy to build upon
attributes and methods
Methods == Function associated with class

Ex: for each employee there are various attributes like name, email etc

Class is blueprint to create instances

each unique employee will be instance of 'Employee' class


Instance variables and class variables are different

Instance variables contain data unique to each instance

class variables are shared among instances of that class

*Each method within a class automatically takes instance as first argument and that
argument is always called 'self'*

So we have to create one argument in method of a class even though we don't use any arguments 
while calling the method because when we call a method instance is automatically sent 
as an argument

"""


"""Class Variables:
    To update the salary we may change amount of raise by 6% not 4%
    So we use class variables
    But if we want to use class variables in methods we can't call directly
    To access class variables we need to access through class itself or through instance of the
    class
    So we can use Employee.raise_amount(through class) or self.raise_amount(through instance) 

    
"""


""" Methods, class methods and Static methods:
    Regular methods and class automatically takes instance as first argument
    We use a decorator @classmethod before defining the method as shown below
    Class methods pass class as first argument instead of instance
    Static methods don't pass anything as first argument. They are same as functions

"""


"""Inheritance:
    Inheritance allows inherit attributes and methods from a parent class. 
    So we can create sub classes and get functionality of parent class so we can overwrite or add new 
    functionalities without effecting parent class.
    Example:
        In our employee data class if we want to create different type of employees
        Like one may be developer and other may be manager 
        Both developers and managers will have names, email and pay columns
        Method resolution order is the order in which python searches for attributes and methods
        use help(class_name) to see method resolution order, methods inherited, attributes inherited
        


"""


"""Special Dunder methods(few):
    __repr__(self) and __str__(self)



"""


class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay): #__method__ are called as Dunder method
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay
        
        Employee.num_of_emps+= 1 #So if we create employees init method is accessed so
                                 #we have to change class' employee number not self
        
    def fullname(self):
        return'{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount
    
    
    @classmethod
    def set_raise_amt(cls, amount):#cls is class variable name not instance
        cls.raise_amount = amount
        
    def __repr__(self): #Check documentation
        return("Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay))
    
    def __str__(self): #Check documentation
        return("{} - {}".format(self.fullname(), self.email))
    
    """
    here first, last and email which are class variables are called attributes of class
      
    """
    
class developer(Employee): #putting parenthesis we can give class we want to inherit
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #super() will be useful if we use multiple inheritance
        # Employee.__init__(self, first, last, pay) #Both this and above statement can be used
        self.prog_lang = prog_lang                                        #


class manager(Employee):
    def __init__(self, first, last, pay, employees = None):#Don't pass mutable data types as default 
        super().__init__(first, last, pay)                 #arguments
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        
        for emp in self.employees:
            print("-->", emp.fullname())






emp_1 = Employee("Saketh", "vns", 100000) #This is efficient method to create variables and
emp_2 = Employee("Test", "name", 80000)  #instances
emp_3 = Employee("Kavya"," Chandrika", 70000) 
dev_1 = developer("my", "name", 60000, "python") 
mgr_1 = manager("Sai", "Saketh", 200000, [emp_1,emp_2,emp_3,dev_1])

"""


emp_1.first = "Saketh"
emp_1.last = "VNS" 
emp_1.email = 'Saketh.VNS@gmail.com'

emp_2.first = "Test"
emp_2.last = "name"
emp_2.email = 'test.NAME@gmail.com'

If instance variables are created manually at each of the instance variable that would be
inefficient. So we create init method to initialize class variables that are common
for many instances that are created


"""




print(repr(emp_1))#Check documentation
print(str(emp_2)) #Check documentation










