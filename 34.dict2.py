employees = [
    {"id": 1, "name": "John",   "age": 28, "salary": 45000, "department": "IT"},
    {"id": 2, "name": "Alice",  "age": 34, "salary": 72000, "department": "HR"},
    {"id": 3, "name": "Bob",    "age": 25, "salary": 38000, "department": "IT"},
    {"id": 4, "name": "David",  "age": 42, "salary": 96000, "department": "Finance"},
    {"id": 5, "name": "Sara",   "age": 30, "salary": 55000, "department": "HR"}
]

#extract name of all employees
for x in employees:
    print(x['name'])

print('------------------')
nms = [x['name'] for x in employees]
print(nms)

print('------------------')
print(list(map(lambda x : x['name'] , employees)))