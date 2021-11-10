
# Absolute path:

# Mediocre way:
# with open('C:\\Users\\holid\\Desktop\\my_file.txt') as file:
#     print(file.read())

# Better way:
# with open('/Users/holid/Desktop/my_file.txt') as file:
#     print(file.read())

# Relative path:
with open('../../../Desktop/my_file.txt') as file:
    print(file.read())
