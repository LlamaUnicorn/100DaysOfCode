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
    # print(names_list)

# turn letter into a string
with open('./Input/Letters/starting_letter.txt') as file:
    read_letter = file.read()
    # read_letter = file.readlines()
    # string_letter = ''
    # # turn letter as a list into a string
    # for word in read_letter:
    #     string_letter += word
# Loop through the names_list:
for name in names_list:
    stripped_name = name.strip('\n') # removing extra characters
    # replace [name] with the name from the names_list
    replaced_name = read_letter.replace('[name]', stripped_name)
    # replaced_name = read_letter.replace('[name]', f'{stripped_name}')
    # saving as the finished letter
    with open(f'./Output/ReadyToSend/Invitation to {stripped_name}', 'w') as finished_letter:
        finished_letter.write(replaced_name)
# Strip extra characters from the names_list.
# names_string = ''
# for name in names_list:
#     names_string += name
#
# print(names_string)
# x = names_string.replace('\n', ' ')
# print(x)
# Insert names into the templates/
# with open('./Input/Letters/starting_letter.txt', 'w') as template:
#     for name in names_list:
#         names_list.replace()

# Hint 1: Return all lines in the file, as a list where each line is an item in the list object:
#
# f = open("demofile.txt", "r")
# print(f.readlines())


# Hint 2: Replace the word "bananas":
#
# txt = "I like bananas"
#
# x = txt.replace("bananas", "apples")
#
# print(x)


# Hint 3: Remove spaces at the beginning and at the end of the string:
#
# txt = "     banana     "
#
# x = txt.strip()
#
# print("of all fruits", x, "is my favorite")