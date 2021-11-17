print('hi')
nato_dict ={
    'a': 'Alpha',
    'b': 'Bravo',
    'c': 'Charlie',
    'd': 'Delta',
    'e': 'Echo',
}

user_input = input('Type your word: ')

# Comprehension with dictionary

# processed_query = {letter:nato_dict[letter] for letter in user_input.lower() if letter in nato_dict.keys()}


# Comprehension with list


# IF statement check

# processed_query = [nato_dict[letter] for letter in user_input.lower() if letter in nato_dict.keys()]

processed_query = [nato_dict[letter] for letter in user_input.lower()]

print(processed_query)