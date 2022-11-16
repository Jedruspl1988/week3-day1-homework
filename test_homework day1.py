import re 

with open('regex_test.txt') as f:
    data = f.read()
    print(data)

test = ("Abraham Lincoln,Andrew P Garfield,Connor Milliken,Jordan Alexander Williams,Madonna,programming is cool")
pattern = re.compile(r'([A-Z]+[a-z]+) ([A-Za-z]+) ?([A-Za-z]+)')
match = pattern.findall(test)

for name in test.split(','):
    match = pattern.search(name)

    if match:
        print(match.group())

    else:
        print('none')