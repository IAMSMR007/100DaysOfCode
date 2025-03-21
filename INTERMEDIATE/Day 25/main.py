import pandas
data =pandas.read_csv("weather_data.csv")


data_dict=data.to_dict()
print(data_dict)

temp_data=data["temp"].to_list()
print(temp_data)


print(data["temp"].max())

print(data[data.temp==data.temp.max()])

monday=data[data.day=="Monday"]
temp=monday.temp[0]
print((temp*1.8)+32)



