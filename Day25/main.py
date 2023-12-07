# data_list = []
# with open("weather_data.csv", "r") as file:
#     data_list.append(file.readlines())
#
# for item in data_list:
#     print(item)
#
# import csv
#
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(type(data))
print(type(data["temp"]))
data_dict = data.to_dict()
print(data_dict['day'][0])
temp_list = data["temp"].to_list()
print(temp_list)
summary = 0
for item in temp_list:
    summary += item
print(f"Avg temperature: {round(summary/len(temp_list))}")
average = sum(temp_list) / len(temp_list)
print(average)
#
# avg = sum_temp/len(temp_list)
# print(avg)
