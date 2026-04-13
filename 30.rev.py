# default and positional paratmeters 

def addA(x,y):
    print(x+y)

addA(20,30) 

#addA()  #TypeError: addA() missing 2 required positional arguments: 'x' and 'y'

# default paratmeters 

def addB(x=10,y=20):
    print(x+y)

addB(100,200)   
addB()


# positional paratmeters
def simpleInterest(p,n,r):
    sint = (p*n*r)/100
    print(sint)

#              p   n   r
simpleInterest(6,20000,3)    

simpleInterest(r=6,p=20000,n=3)  

#  *args

def addAll(*args):
    total = 0
    for x in args:
        total=total + x     #0+1 = 1 +2=3+3=6+4=10
    return total    

res = addAll(1,2,3,4,5,6,7,8,9)
print(res)

# **kwargs

info = {
    "name" : "dipanshu",
    "surname" :"chawde"
}

def addNewInfo(**kwargs):
    info.update(kwargs)

print(info)
addNewInfo(city = "pune")

print(info)

addNewInfo(skills = "Javascript")

print(info)

#---------------------------------------------------------------------
#operation with every element
#find age
birthYear = [2021,2000,1986,1999,2015,2008,2025]
age=[]

for yr in birthYear:
    age.append(2026-yr)     #2021,2000,1986....2008

print(age)

#---------------------------------------------------------------------
# filter element 
marks = [90,76,88,23,11,56,45,35]
passM =[]
failM=[]

for mk in marks:
    if mk>=35:
        passM.append(mk)
    else : 
        failM.append(mk)

print(passM)
print(failM)

#---------------------------------------------------------------------

#sum of all elements
nums = [22,66,88,99,55,66,99,33,11]

total =0

for x in nums:
    total=total+x

print(total)