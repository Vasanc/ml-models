# import all the lib
from seaborn import load_dataset
import pandas
import pickle

# loading the dataset using seaborn
df = load_dataset('penguins')

# Dropping missing records
data = df.dropna()

#Independent variable
X = data[['bill_length_mm', 'bill_depth_mm','flipper_length_mm','body_mass_g']]

# Import label encoder
from sklearn import preprocessing

# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()
#Dependent variable
y = label_encoder.fit_transform(data['sex'])


#Creating ML Model
from sklearn.svm import SVC
clf = SVC(kernel='linear')

#Fitting the data
clf.fit(X,y)

#creating pkl file
pickle.dump(clf, open('pkl files/svm.pkl','wb'))


