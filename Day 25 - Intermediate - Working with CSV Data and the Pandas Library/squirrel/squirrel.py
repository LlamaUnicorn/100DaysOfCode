import pandas
data = pandas.read_csv('2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
# print(data['Primary Fur Color'])
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(data_dict)
df.to_csv('new_data.csv')

# My failed attempt (i put another dict into dict: lines 43, 44):

# Gray = []
# Cinnamon = []
# Black = []
#
# for color in data['Primary Fur Color']:
#     if color == "Gray":
#         Gray.append(color)
#     elif color == "Cinnamon":
#         Cinnamon.append(color)
#     elif color == "Black":
#         Black.append(color)
# print(len(Gray))
# print(len(Cinnamon))
# print(len(Black))
#
# gray_sq = len(Gray)
# cinnamon_sq = len(Cinnamon)
# black_sq = len(Black)
#
# squirrels = {
#     'Fur Color': {'Gray', 'Cinnamon', 'Black'}, # should be a list: ['Gray', 'Cinnamon', 'Black']
#     'Number': [int(gray_sq), int(cinnamon_sq), int(black_sq)]
# }

# squirrels_data = pandas.DataFrame(squirrels)
# print(squirrels)
# squirrels_data.to_csv('new_data.csv')
# generate csv with number of squirrels by their color
