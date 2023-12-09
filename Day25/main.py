import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count_gray = data['Primary Fur Color'].value_counts()["Gray"]
count_black = data['Primary Fur Color'].value_counts()["Black"]
count_cinnamon = data['Primary Fur Color'].value_counts()["Cinnamon"]
count = data['Primary Fur Color'].value_counts()
print(count_gray)
print(count_black)
print(count_cinnamon)
print(count)
data_fur = {
    "Fur" : ["grey", "red", "black"],
    "Count" : [count_gray, count_cinnamon, count_black],
}
data2 = pandas.DataFrame(data_fur)
data2.to_csv("squirrel_count.csv")
print(data2)
