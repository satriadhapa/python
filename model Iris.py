import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("dataset/Iris.csv")

mapping = {0: "Setosa", 1: "Vericolor", 2: "Virginica"}
data = data.replace(["Setosa", "Vericolor", "Virginica"],[0,1,2])

X = data.iloc[:,0:-1]
y = data.iloc[:,-1]

logreg = LogisticRegression()
logreg.fit(X,y)

def classify(a, b, c, d):
    arr = np.array([a, b, c, d])
    arr = arr.astype(np.float64)
    query = arr.reshape(1, -1)
    prediction = mapping[logreg.predict(query)[0]]