#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Read names from the list and save them to the names_list.
with open('./Input/Names/invited_names.txt') as invited_names:
    names_list = invited_names.readlines()
    print(names_list)

# Strip extra characters from the names_list.
names_string = ''
for name in names_list:
    names_string += name

print(names_string)
x = names_string.replace('\n', ' ')
print(x)
# Insert names into the templates/
# with open('./Input/Letters/starting_letter.txt', 'w') as template:
#     for name in names_list:
#         names_list.replace()

# Return all lines in the file, as a list where each line is an item in the list object:
#
# f = open("demofile.txt", "r")
# print(f.readlines())


# Replace the word "bananas":
#
# txt = "I like bananas"
#
# x = txt.replace("bananas", "apples")
#
# print(x)


# Remove spaces at the beginning and at the end of the string:
#
# txt = "     banana     "
#
# x = txt.strip()
#
# print("of all fruits", x, "is my favorite")