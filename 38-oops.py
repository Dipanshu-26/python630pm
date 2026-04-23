a=[1,2,3,4]
print(a)
print(type(a))



a="dipanshu"
print(a)
print(type(a))

a=11
print(a)
print(type(a))

a={"name" : "dipanshu"}
print(a)
print(type(a))


# class ---> 
# methods , properties 

# type 
# introvert           extrovert
# calm                 loud
# less outing          more outing
# less social          more social

# Human 
# properties ----> name, hight, weight ....
# method     -----> walk(), talk()

# method ----> healthy ,  discuss , solution , motivate 

# vehicle 
# properties--->coloe,model logo  , company 
# methods -----> start(), stop(),move()

# bank 
# properties ---> accno, accname, baranchname,bal
# method --> deposit(),withdorw()

#program 1

#class , objects , properties , methods 


class Person:
    #properties
    fname =  None
    lname = None
    #method 
    def displayName(self):         #self ==>object
        print(f"Name = {self.fname} and surname = {self.lname}")


#self ==> adi
adi = Person()  
print(adi.fname)
print(adi.lname)

adi.fname="aditya"
adi.lname = "masalkar"
adi.displayName()
print(adi.fname)
print(adi.lname)


#self===>dip
dip = Person()
print(dip.fname)
print(dip.lname)

dip.fname="dipanshu"
dip.lname="chawde"
dip.displayName()
print(dip.fname)
print(dip.lname)

# a=[1,2,3,4,5,6]
# a.pop()

print("--------------------------------------------")
#program 2 
#constructor 
# a constructor is a special method in a class that is automatically called when a new object is created.
# Its main purpose is to initialize the object’s attributes (set initial values) when the object is instantiated. 
# __init__

class Person2:
    #constructor
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln

    #method 
    def displayName(self):         #self ==>object
        print(f"Name = {self.fname} and surname = {self.lname}")

adi2 = Person2("aditya2","masalkar2")
adi2.displayName()
print(adi2.fname)

dip2 = Person2("dipanshu2","chawde2")
dip2.displayName()
print(dip2.fname)


# Key Pointsof constructor:
# The first parameter is always self, which refers to the current object.
# You can have default values for parameters.


#prgram 3 
class Person3:
    def __init__(self):
        self.fname = None
        self.lname = None
    #method 
    def displayName(self):         #self ==>object
        print(f"Name = {self.fname} and surname = {self.lname}")

adi3 =Person()
print(adi3.fname)
print(adi3.lname)

adi3.fname="aditya3"
adi3.lname = "masalkar3"
adi3.displayName()
print(adi3.fname)
print(adi3.lname)