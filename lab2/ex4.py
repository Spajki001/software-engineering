import json


with open("./lab2/ex2-text.csv", "r", encoding="utf-8") as f:
    txt = f.readlines()

employees = []
for line in txt:
    split_line = line.split(',')
    split_line = [ x.strip() for x in split_line ]
    employee = {}
    employee['employee'] = split_line[0]
    employee['title'] = split_line[1]
    employee['age'] = split_line[2]
    employee['office'] = split_line[3]
    if (split_line[0] == "Employee"):
        continue
    else:
        employees.append(employee)

with open('./lab2/ex4-employees.json', 'w', encoding='utf-8') as f:
    json.dump(employees, f)