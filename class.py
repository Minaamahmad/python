import pandas as pd 

df = pd.read_csv("orders.csv")
a = df[(df["Price"] >= 1000)]

print(a)
