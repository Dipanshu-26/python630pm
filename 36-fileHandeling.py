# File Handeling in python
#---------------------------------------

# Writing data into a file
#---------------------------------------
#"r","w","a","a+"

# file = open("student_data.txt","w")
# file.write("Name : Dipanshu Chawde\n")
# file.write("Courese : Pyyhon \n")
# file.write("Python Module : File Handeling \n")
# file.write("Batch : Evening Batch\n")

# file.close()

# print("Data is written successfully...")

# Reading data from the file
#---------------------------------------

# file = open("student_data.txt","r")

# content = file.read()
# print(content)
# file.close()

# Writing data again into a file
#---------------------------------------
# file = open("student_data.txt","w")
# file.write("Name : Neel Chawde\n")
# file.write("Courese : Javascript \n")
# file.write("JS Module : File Handeling \n")
# file.write("Batch : Evening Batch\n")

# file.close()

# print("Data is written successfully...")

#data is replaced---------------------------
#--------------------------------------------------
# Appending the contents in existing file

# f=open("student_data.txt","a")
# f.write("Name : Akay \n")
# f.write("Courese : SQL \n")

# #read data
# file = open("student_data.txt","r")

# content = file.read()
# print(content)

# file.close()

print("--------------------------------")
#---------------------------------------------------
# copying file 

# f1=open("student_data.txt","r")
# f2=open("copied_file.txt","w")
# f2.write(f1.read())
# f1.close()
# f2.close()

# f2=open("copied_file.txt","r")
# content = f2.read()
# print(content)
# f2.close()

# ----------------------------------------------
#a+ open the file for appending and reading instead of using w and r and seek()

# fc= open("copied_file.txt","a+")

# fc.write("\n\nThis is new line by a+")

# content = fc.read()
# print(f"***new content*** \n {content}")

# fc.close()

#----------------------------------------------------
#seek()

fc= open("copied_file.txt","a+")

fc.write("\n\nThis is new line for seek")

fc.seek(0,0)
content = fc.read()
print(f"***new content*** \n {content}")

fc.close()