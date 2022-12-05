# importing pandas package
import pandas as pd
  
# making data frame from csv file
data = pd.read_csv("file.csv")
print(data)
data=data.drop_duplicates(subset =["name","dept"])
print("----------------")
print(data)
