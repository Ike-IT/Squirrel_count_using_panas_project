import pandas

squirrels_data = pandas.read_csv("squirrel_count.csv")
# print(squirrels_data)
gray_squirrels_count = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrels_data[squirrels_data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
# print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_result")