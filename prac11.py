#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      deepika
#
# Created:     21-03-2022
# Copyright:   (c) deepika 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from numpy import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

# Reading a excel file
fr = pd.read_csv("C:/Users/shwet/Desktop/mera kaam/CG/ml_linear.csv")
print (fr)

x = fr['size']
y = fr['price']

x = x.array.reshape(len(x),1)

# Creating a hypothesis model
model = LinearRegression()
model.fit(x, y)

print('Intercept-> ', model.intercept_)
print('Slope->', model.coef_)

# Predicting y values
def prid_y_func(x):
  return  model.coef_ * x + model.intercept_

y_pred = prid_y_func(x)
print('predicted response:', y_pred, sep='\n')

# Plotting a graph
plt.scatter(x, y, color = 'red')
plt.scatter(x, y_pred, color = 'blue',marker='s')
plt.plot(x, y_pred, color = 'green')
plt.xlabel('Size of the house')
plt.ylabel('Price of the house')
plt.title(" Linear Regression in one variable ")
plt.legend(['Original Values','Predicted values','Hypothesis line'])
plt.show()

# Testing a new data
x_new = int(input("Enter a size of house -> "))
new_y = prid_y_func(x_new)
print("Price of your house is -> ", new_y)