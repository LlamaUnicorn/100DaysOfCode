# Opening files. Option A:
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Opening files. Option B:
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing into file:
with open("my_file.txt", mode='w') as file:
    contents = file.write('New text.')
    print(contents)

# Appending
with open("my_file.txt", mode='a') as file:
    contents = file.write('\nNew text again.')
    print(contents)

with open("my_file_2.txt", mode='a') as file:
    contents = file.write('\nNew text again.')
    print(contents)
