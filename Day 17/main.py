from question_model import Question
from data import question_data

#question_bank

for index in range(len(question_data)):
    for key in question_data[index]:
        print(question_data[index][key])

# dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
# for index in range(len(dataList)):
#     for key in dataList[index]:
#         print(dataList[index][key])