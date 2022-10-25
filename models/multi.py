#importing all the libraries
import pandas as pd
import pickle


#importing dataset using panda
dataset = pd.read_csv('dataset/Real-estate1.csv')

# #dropping the id and date column
dataset.drop(['date', 'sqft_lot', 'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement','yr_built', 'yr_renovated', 'street', 'city', 'statezip', 'country'], axis=1, inplace=True)

#separating independent and dependent variable
X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0].values


#Creating ML Model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting the data
regressor.fit(X, y)

#creating pkl file
pickle.dump(regressor, open('pkl files/multi.pkl','wb'))