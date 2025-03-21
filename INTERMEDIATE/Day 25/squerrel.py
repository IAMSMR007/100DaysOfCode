import pandas
data =pandas.read_csv("Squirrel_Census.csv")




# Primary Fur Color
# White
# Cinnamon
# Gray


# Count of Primary Fur Color
black = len(data[data["Primary Fur Color"]=="Black"])
cinnamon = len(data[data["Primary Fur Color"]=="Cinnamon"])
gray = len(data[data["Primary Fur Color"]=="Gray"])

print(f"white squerrel {black}\n",
      f"cinnamon squerrel {cinnamon}\n",
      f"gray squerrel {gray}\n"
)