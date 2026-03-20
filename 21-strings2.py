# upper , lower , capitalize,count, find, index , endswith, startswith,
#isLower(), isUpper()

print("hello".upper())
print("HEllo".lower())
print("hello".capitalize())

a="nitin"
print(a.count("t"))

#startsWith
b="dipanshu"
print(b.startswith("d"))
print(b.startswith("dip"))
print(b.startswith("D"))
print(b.startswith("Dip"))

#endsWith
b="dipanshu"
print(b.endswith("u"))
print(b.endswith("shu"))
print(b.endswith("U"))
print(b.endswith("SHU"))

#find--> return index of first matching ch,if not found matching ch returns -1

c="tanish"
res = c.find("a")
print(res)

print(c.find("tan"))
print(c.find("taa"))

c="nitin"
print(c.find("i"))

#index 
d="dipanshu"
print(d.index("i"))
print(d.index("n"))
print(c.index("n"))
#print(d.index("x"))    #error

name="122"
print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())

name = "neel"
print(name.islower())
print(name.isupper())

#isSpace()
print("  ".isspace())
print("  a".isspace())

#istitle()
x="My Name Is Dipanshu"
print(x.title())
print(x.istitle())

# join ()

info = ["dipanshu", "chawde", "9922447802"]
print("@".join(info))