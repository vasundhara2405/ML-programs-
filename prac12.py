#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      deepika
#
# Created:     21-03-2022
# Copyright:   (c) deepika 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/shwet/Desktop/mera kaam/CG/plantdata.csv')
df.head()
x=df.drop(['PE'], axis=1).values
y=df['PE'].values

print(x)
print(y)

#Split the dataset into training and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.33, random_state=0)

#Train the model on the training set
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train, y_train)

#Print values of intercept and respective coefficients
print(model.intercept_)
print(model.coef_)

#Predict the test set results
y_pred=model.predict(x_test)

#Difference between predicted and actual values
table = pd.DataFrame({"Actual value": y_test, "Predicted value": y_pred, "Difference": y_test-y_pred})
print(table)

#Predict for a given case
model.predict([[14.96, 41.76, 1024.07, 73.17]])

#Calculate the errors
from sklearn import metrics
print(metrics.mean_absolute_error(y_test, y_pred))
print(metrics.mean_squared_error(y_test, y_pred))
print(np.sqrt(metrics.mean_absolute_error(y_test, y_pred)))

#Evaluate the model
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

#Plot the results
plt.figure(figsize=(20,20))
plt.scatter(y_test, y_pred)
plt.xlabel('Actual', fontsize=18)
plt.ylabel('Predicted', fontsize=18)
plt.title('Multivariate Linear Regression: Actual vs Predicted', fontsize=18)