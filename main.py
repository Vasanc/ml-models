import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/linear')
def linear():
    return render_template('linear.html')

@app.route('/multi')
def multi():
    return render_template('multi.html')

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/knn')
def knn():
    return render_template('knn.html')

@app.route('/svm')
def svm():
    return render_template('svm.html')

@app.route('/for')
def forr():
    return render_template('for.html')

@app.route('/ada')
def ada():
    return render_template('ada.html')

@app.route('/xg')
def xg():
    return render_template('xg.html')

@app.route('/linearpredict',methods=['POST'])
def linearpredict():
    
    model = pickle.load(open('pkl files\linear.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('linear.html', prediction_text='Employee Salary should be ${}'.format(output))

@app.route('/multipredict',methods=['POST'])
def multipredict():
    
    model = pickle.load(open('pkl files\multi.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('multi.html', prediction_text='Price of the house must be ${}'.format(output))


@app.route('/logpredict',methods=['POST'])
def logpredict():
    
    model = pickle.load(open('pkl files\log.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if output==1:
        return render_template('log.html', prediction_text='You have diabetes')
    else:
        return render_template('log.html', prediction_text='You don\'t have diabetes')

@app.route('/knnpredict',methods=['POST'])
def knnpredict():
    model = pickle.load(open('pkl files\knn.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if output==0:
        return render_template('knn.html', prediction_text='The flower is Iris-Setosa')
    elif output==1:
        return render_template('knn.html', prediction_text='The flower is Iris-Versicolor')
    else:
        return render_template('knn.html', prediction_text='The flower is Iris-Virginica')
    
@app.route('/svmpredict',methods=['POST'])
def svmpredict():
    
    model = pickle.load(open('pkl files\svm.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if output==1:
        return render_template('svm.html', prediction_text='The Penguin is Male')
    else:
        return render_template('svm.html', prediction_text='The Penguin is Female')
    
    
@app.route('/forpredict',methods=['POST'])
def forpredict():
    
    model = pickle.load(open(r'pkl files\for.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if output==1:
        return render_template('for.html', prediction_text='The Possum is Male')
    else:
        return render_template('for.html', prediction_text='The Possum is Female')

@app.route('/adapredict',methods=['POST'])
def adapredict():
    
    model = pickle.load(open(r'pkl files\ada.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if output==0:
        return render_template('ada.html', prediction_text='The flower is Iris-Setosa')
    elif output==1:
        return render_template('ada.html', prediction_text='The flower is Iris-Versicolor')
    else:
        return render_template('ada.html', prediction_text='The flower is Iris-Virginica')


@app.route('/xgpredict',methods=['POST'])
def xgpredict():
    
    model = pickle.load(open(r'pkl files\xg.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if output==1:
        return render_template('xg.html', prediction_text='You have diabetes')
    else:
        return render_template('xg.html', prediction_text='You don\'t have diabetes')

if __name__ == "__main__":
    app.run(debug = False, host = '0.0.0.0')