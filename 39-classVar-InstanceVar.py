# Class Variable vs Instance Variable

class Students:
    #class variable
    country = "India"
    
    #instance variable using constructor
    def __init__(self,fn,ln,age):
        #instance variable
        self.fname = fn
        self.lname = ln 
        self.age = age

    @classmethod
    def changeCountry(cls,nc):
        cls.country=nc

    #instance method
    def displayName(self):
        print(f"name = {self.fname} and surname = {self.lname}")        

    #instance method
    def updateAge(self,inc):
        self.age = self.age + inc


tan = Students("tanish","chawde",18)
print(tan.fname)
print(tan.country)
print(tan.age)

tan.displayName()

tan.updateAge(2)
print(tan.age)

#tan.changeCountry("UK")     #this changes value of class variable
tan.country = "UK"           #this changes value of object variable
print(tan.country)

print("------------------------------")
raj = Students("rajasi","gaware",10)
print(raj.fname)
print(raj.country)
print(raj.age)

raj.displayName()

raj.updateAge(3)
print(raj.age)

#raj.changeCountry("USA")   #this changes value of class variable
raj.country="USA"
print(raj.country)

print(tan.country)
print("------------------------------")
ak = Students("Akay","masalkar",2)
print(ak.country)

print("------------------------------")
Students.changeCountry("Bharat")
print(tan.country)
print(raj.country)
print(ak.country)