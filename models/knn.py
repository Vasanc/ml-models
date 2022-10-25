# import all the lib
import pandas as pd
import pickle

# read the dataset using pandas
data = pd.read_csv('dataset/Iris.csv')

# Import label encoder
from sklearn import preprocessing

# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()

# Encode labels in column 'species'.
data['Species']= label_encoder.fit_transform(data['Species'])

#Independent variable
X = data.iloc[:,1:5]

#Dependent variable
y = data['Species']

#Creating ML Model
from sklearn.neighbors import KNeighborsClassifier
lr = KNeighborsClassifier(n_neighbors = 7)
 
#Fitting the data
lr.fit(X, y)

#creating pkl file
pickle.dump(lr, open('pkl files/knn.pkl','wb'))


