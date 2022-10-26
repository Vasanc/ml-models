import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('dataset/possum.csv')
d = {'m':1, 'f':0}
df = df.dropna()
X = df.drop(["case", "site", "Pop", "sex", "hdlngth", "taill", "earconch", "eye", "belly"], axis=1)
y = df["sex"].map(d)
rf_model = RandomForestClassifier(n_estimators=50, random_state=44)
rf_model.fit(X, y)
pickle.dump(rf_model, open('pkl files/for.pkl','wb'))
