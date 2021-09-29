file = open("regex_test.txt")
data = file.read()

regex = re.compile('.\w?[A-Z]\w*$', re.M)
my_names = regex.findall(data)
for name in my_names:
    print(name)