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

@app.route('/linearpredicts',methods=['POST'])
def linearpredict():
    
    model = pickle.load(open('pkl files\linear.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('linear.html', prediction_text='Employee Salary should be ${}'.format(output))

@app.route('/multipredicts',methods=['POST'])
def multipredict():
    
    model = pickle.load(open('pkl files\multi.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('multi.html', prediction_text='Price of the house must be ${}'.format(output))

if __name__ == "__main__":
    app.run()