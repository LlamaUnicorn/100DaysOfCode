# Stage 1: vanilla opening
# with open('weather-data.csv') as file:
#     file_contents = file.readlines()
#     print(file_contents)

# Stage 2: opening with csv module
# import csv
# with open('weather-data.csv') as file:
#     data = csv.reader(file)
#     print(data)
#     temperatures = []
#     for row in data:
#         new_temperature = row[1]
#         if row[1] != 'temp':
#             # new_temperature = int(new_temperature)
#             # temperatures.append(new_temperature)
#             temperatures.append(int(new_temperature))
#         # if row[1] == 'temp':
#         #     pass
#         # else:
#         #     new_temperature = int(new_temperature)
#         #     temperatures.append(new_temperature)
#     print(temperatures)

# Stage 3: Pandas
import pandas
data = pandas.read_csv('weather-data.csv')
# print(data)
# print(data['temp'])

# DataFrame to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Series to list
# temp_list = data['temp'].to_list()
# print(temp_list)

# Average temperatures

# My crappy solution
# total_temp = 0
# for temperature in temp_list:
#     total_temp += temperature
# print('total temp', total_temp)
# avg_temp = total_temp / len(temp_list)
# print(avg_temp)

# Right solution
# average = sum(temp_list) / len(temp_list)
# print(average)

# Pandas solution
# print(data['temp'].mean())
# print(data['temp'].max())

# Without bracket notation
# print(data.condition) # Case sensitive

# Getting data in rows
# print(data[data.day == "Monday"])

# Print the row with the highest temperature
# print(data['temp'].max()) # prints max temp in dataframe
# print(data[data.temp == data['temp'].max()])

# Convert Celsius to Fahrenheit
# monday = data[data.day == 'Monday']
# temp_in_C = int(monday.temp)
# temp_in_F = temp_in_C * (9 / 5) + 32
# print(temp_in_F)

# Create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv('new_data.csv')
