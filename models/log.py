# import all the lib
import pandas as pd
import pickle

# read the dataset using pandas
dataset = pd.read_csv('dataset/diabetes.csv')

#Independent variable
x = dataset.iloc[:, [1,2,4,5,7]].values

#Dependent variable
y = dataset.iloc[:, 8].values


#Creating ML Model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)

#Fitting the data
classifier.fit(x,y)

#creating pkl file
pickle.dump(classifier, open('pkl files/log.pkl','wb'))


