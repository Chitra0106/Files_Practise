import pandas

data = pandas.read_csv(
    r"C:\Users\mailc\Files_Practise\SquirrelCensusDataAnalysis\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)
#print(data.columns)
data.columns = data.columns.str.strip()
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Red"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count":[len(gray_squirrels),len(red_squirrels),len(black_squirrels)],
}
df_sqirrel = pandas.DataFrame(data_dict).to_csv(r"C:\Users\mailc\Files_Practise\SquirrelCensusDataAnalysis\squirrel_Count.csv")

