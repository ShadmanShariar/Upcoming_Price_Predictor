import pandas
import matplotlib.pyplot as mp
from sklearn.linear_model import LinearRegression
data = pandas.read_csv\
    ("iphone_price.csv")
print(data)
#----------------------------------------->matplotlib.pyplot
mp.scatter(data["version"],data["price"])
mp.show()
mp.plot(data["version"],data["price"])
#mp.legend()
mp.show()
mp.bar(data["version"],data["price"])
mp.show()
model = LinearRegression()
#------------------------------------------->sklearn.linear_model
model.fit(data[["version"]],data[["price"]])
future_model_number = 30;
print(model.predict([[future_model_number]]))