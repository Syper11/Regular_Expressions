import re

with open("day_1/names.txt") as file:
    data = file.read()
    print(data) 
    file.close()
    
regex=re.compile('(?P<fullname>[\w ]*, [\w -]*)\t(?P<optional>[.\+\-\w\d]+@[-,.\w\d\s\(\)]+)?(?P<twitter>@[\w\d-]+)?\n')

for found in regex.findall(data):
    print(found)

print('\n')    
    
for found in regex.finditer(data):
    if found.group("twitter"):
        print(f'{found.group("fullname").split(", ")[1]} {found.group("fullname").split(", ")[0]} / {found.group("twitter")}')
    