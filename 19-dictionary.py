# looping in python 

student={
    "fname": "tanish",
    "lname" : "chawde",
    "age" : 18,
    "city" :"pune"
}

print(student)

for key in student:
    print(key)

for key in student.keys():
    print(key)


for val in student.values():
    print(val)

student={
    #  k        v
    "fname": "tanish",
    "lname" : "chawde",
    "age" : 18,
    "city" :"pune"
}

for k,v in student.items():
    print(f"key = {k}  and value = {v}")    

# for k in range(len(student)):            #k=0,1,2,3
#     print(student[k])    

print(student["fname"])

student={
    #  k        v
    "fname": "tanish",
    "lname" : "chawde",
    "age" : 18,
    "city" :"pune"
}

skeys = list(student.keys())
print(skeys)      #['fname', 'lname', 'age', 'city']

for k in range(len(student)):            #k=     0,        1,      2,     3
    key=skeys[k]                     #keys =   'fname', 'lname', 'age', 'city'   
    print(student[key])    


i=0
while i<len(student):
    keys = skeys[i] 
    print(student[keys])  
    i=i+1
