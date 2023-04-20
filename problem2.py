import re

with open("day_1/regex_test.txt") as file:
    data = file.read()
    print(data) 
    file.close()
    
pattern=re.compile('(?P<first_name>[A-Z]{1}[a-z]+)(?P<middle_name> [A-Za-z]+)(?P<last_name> [A-Za-z-]+)?\n')

for found in pattern.findall(data):
    print(found)

print('\n')    
    
for found in pattern.finditer(data):
    if found.group("first_name"):
        print(f'{found.group("first_name")} {found.group("last_name")}')
    
    elif found.group("middle_name"):
        print(f'{found.group("first_name")} {found.group("middle_name")} {found.group("last_name")}')
    else:
        print("none")