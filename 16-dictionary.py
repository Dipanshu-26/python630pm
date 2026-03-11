#info = ["dipanshu","chawde",42,23]

# descriptive datatype
#dictionary in python 
# key : value

dictA = {
    "fname":"dipanshu",
    "lanem":"chawde",
    "age": 42,
    "rollno" : 32
}

print(dictA)
print(type(dictA))

#------------------------------------
vechile = {
    "color" : "red",
    "type" : "SUV"
}
print(vechile)
print(vechile["color"])
print(vechile["type"])
#-------------------------------------

#CRUD operations  , loops

student={
    "fname": "neel",
    "lname":"chawde",
    "age":10,
    "rollno" : 23
}
print(student)
print(student["fname"])
print(student["lname"])

print("age" in student)
print("class" in student)

print(student.get("fname"))
print(student.get("rollno"))

print(student.keys())
print(student.values())
print(student.items())

print(student.keys(),  student.values())

# add / update-----------------------------------------
student={
    "fname": "neel",
    "lname":"chawde",
    "age":10,
    "rollno" : 23
}

print(student)
student["class"]="3B"
print(student)


student["class"]="4A"
print(student)

#using update method
student.update({"language":"marathi"})
print(student)
student.update({"language":"english"})
print(student)

# delete---------------------------------------------
#delete any key

# del -------------
print(student)
del student["language"]
print(student)

#pop() ==>delete key returns deleted value

print(student)
dval = student.pop("class")
print(dval)
print(student)

#popitem()  ==> last key delets
student={
    "fname": "neel",
    "lname":"chawde",
    "age":10,
    "rollno" : 23
}
print(student)
student.popitem()
print(student)

# clear() ==>remove all keys

student.clear()
print(student)

batch = {
    "sec": "A",
    "total" : 20
}
batch.pop("age",None)
print(batch)

