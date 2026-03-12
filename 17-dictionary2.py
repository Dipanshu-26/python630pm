#dictionary in python CRUD
info = {
    "fname" : "dipanshu",
    "lname" : "chawde",
    "age" : 42,
    "roll" : 34

}
a= info.get("fname")
b=info.get("lname")
print(a)
print(b)

info["class"] = "python"
print(info)

info["class"] = "javascript"

info.update({"location" : "pune"})
print(info)
info.update({"location" : "mumbai"})
print(info)

del info["location"]
print(info)

info.pop("age")
print(info)

info.popitem()
print(info)

info.clear()
print(info)

info = {
    "fname" : "dipanshu",
    "lname" : "chawde",
    "age" : 42,
    "roll" : 34

}

print(info.keys())
print(info.values())
print(info.items())

#looping-------------------------------------------

for k in info.keys():
    print(k)

for v in info.values():
    print(v)    

for k,v in info.items():
    print(f'keys : {k}  values : {v}')    

# set default---------------------------------
info = {
    "fname" : "dipanshu",
    "lname" : "chawde",
    "age" : 42,
    "roll" : 34

} 

info["location"] = "pune"

q1= info.setdefault("location" ,"mumbai")
print(info)
print(q1)

q2 = info.setdefault("language","marathi")
print(info)
print(q2)

info.setdefault("skills",[]).append("python")
print(info)

info.setdefault("skills",[]).append("javascript")
print(info)