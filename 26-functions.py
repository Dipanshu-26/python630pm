x=10
y=20

#function with parameter and without return type
def calc(a,b):            #a,b paraameters
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)

calc(x,y)    #x,y arguments

print("-------------------")
#function with parameter and with return type
def add(a,b):
    return a+b

res = add(x,y)
print(res)

res2 = add(15.5,17.7)
print(res2)

res3 = add("dip","anshu")
print(res3)

print("-------------------")
#find where person can deivr or not
#age
#int as parameter and boolean as return type
def canDrive(age):
    if age >=18:
        return True
    else:
        return False

res = canDrive(30)
print(res)

print("-------------------")
#int as parameter and string as return type
#find where person can deivr or not
#age

def canDrive(age):
    if age >=18:
        return "can drive"
    else:
        return "can not drive"

res = canDrive(10)
print(res)

print("-------------------")
#string as parameter and string(with concatination) as return type
def greet(name):
    return "hello "+name+"... How are you?"

print(greet("dipanshu"))

#list as parameter and list as return type

city=["pune","nagpur","amravati","mumbai","nashik"]

def addCity(cityList,cityName):
    cityList.append(cityName)
    return cityList

print(city)
city2 = addCity(city,"nanded")
print(city2)

#dict as parameter and as return type
info={
    "name" : "dipanshu",
    "lname" : "chawde"
}

def addCityy(info):
    info['city'] = "pune"
    return info

print(info)
info2=addCityy(info)
print(info2)
print(info)

#tuple as parameter and tuple as returntype
numbers = (11,22,33)
def addToTuple(tupA):
    tupA = list(tupA)     #tuple is converted in list
    tupA.append(55)       #new element added to list
    tupA= tuple(tupA)     # list is converted in tuple
    return tupA

print(numbers)
finalTuple = addToTuple(numbers)
print(finalTuple)
print(numbers)

# set as parameter and set as return tupy

setA={1,2,3,4,5}
def addToSet(setB):
    setB.add(66)
    return setB

print(setA)

setF = addToSet(setA)
print(setF)
print(setA)