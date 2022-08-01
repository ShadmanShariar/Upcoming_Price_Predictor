import pandas
import numpy as np
import csv
import matplotlib.pyplot as mp
from sklearn.linear_model import LinearRegression
data = pandas.read_csv\
    ("iphone_price.csv")

CSVData = open("iphone_price2.csv")
Array2d_result = np.loadtxt(CSVData, delimiter=",")

# print(Array2d_result)
print(data)
# mp.scatter(data["version"],data["price"])
# mp.show()
mp.plot(data["version"],data["price"])
mp.title("Upcoming Price Predictor")
mp.xlabel("Model Number")
mp.ylabel("Price")
mp.show()
# mp.bar(data["version"],data["price"])
# mp.show()
model = LinearRegression()
model.fit(data[["version"]],data[["price"]])
print("Enter Your Model Number")
mod = int(input())
c = 1
ans = 0
for i in range (len(Array2d_result)):
    if(Array2d_result[i][0]==mod):
       ans = int(Array2d_result[i][1])
       c=2
       break
try:
 if(c==1):
    future_model_number = mod;
    print("Upcoming predicted price")
    print(int(model.predict([[future_model_number+2]])),"$")
 else:
    print("Upcoming predicted price")
    print(ans,"$")
except NameError:
  print("")
