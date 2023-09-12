
import csv
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

column_name = ["code", "COUNTRY", "POP", "AREA", "GDP", "CONT", "IND_DAY"] #The name of the columns
data = ['SL',"Sri Lanka", 2.2, 65, 72.9, "Asia", "1948-02-04"] #the data

with open('data.csv', 'a') as f:
    writer = csv.writer(f) #this is the writer object
    writer.writerow(data) #this is the data




