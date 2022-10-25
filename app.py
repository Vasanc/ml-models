import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
linear = pickle.load(open('pkl files\linear.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/linear')
def linear():
    return render_template('linear.html')

@app.route('/predict',methods=['POST'])
def linearpredict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = linear.predict(final_features)

    output = round(prediction[0], 2)
    return render_template('linear.html', prediction_text='Employee Salary should be ${}'.format(output))

if __name__ == "__main__":
    app.run()