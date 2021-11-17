student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

# student_data_frame = pandas.DataFrame()
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
# for (index, row) in data.iterrows():
#     print(row.letter, row.code)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter your word: ').upper()
processed_query = [phonetic_dict[letter] for letter in word]

print(processed_query)
# print(new_dict['A'])