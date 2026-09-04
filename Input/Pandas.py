import pandas as pd
data = pd.read_csv(r"C:\Users\mailc\Files_Practise\Input\Weather_Card.csv")
#print(data["Temp"])
#print(data.head())
# dataframe = pd.DataFrame(data)
# print(dataframe.head())
# print(dataframe.describe())
print(data["Temp"].mean()) # Average
print(data["Temp"].max())
temp_list = data["Temp"].to_list()
sum_temp = sum(temp_list)
len_temp = len(temp_list)
print(sum_temp/len_temp)
data_dict = data.to_dict() # column data-  Dictionary
data_dict_rows = data.to_dict(orient="records")
# print(data_dict_rows)
#print(data_dict)
#print(data.Day=="Monday")
print(data[data.Temp ==data.Temp.max()])
monday = data[data.Day =="Monday"]
monday_temp = monday.Temp[0]
Temp_FH = (monday_temp *9/5 +32)
print(Temp_FH)