file = open('F:/水果商场.txt', 'r+')
print(file.tell())
# print(file.read())
for f in file:
    print(f)

