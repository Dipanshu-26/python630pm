#generator
# reading large file 

def read_file_normal(file_path):
    with open(file_path ,"r") as f:
        return f.read()
    
content = read_file_normal("student_data.txt")    
print(content)

#-------------------------------
# Generator for reading a large file line by line (This is a real-life use case to save memory.)

def read_file(file_path):
    with open(file_path ,"r") as f:
        for line in f:
            yield line


#for line in read_file("student_data.txtx")