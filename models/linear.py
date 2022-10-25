# import all the lib
import pandas as pd
import pickle

# read the dataset using pandas
data = pd.read_csv('dataset/Salary_Data.csv')

#Independent variable
X = data.iloc[:,0:1]

#Dependent variable
y = data['Salary']

#Creating ML Model
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

#Fitting the data
lr.fit(X,y)

#creating pkl file
pickle.dump(lr, open('pkl files/linear.pkl','wb'))


