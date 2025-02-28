from flask import Flask, request, render_template, app, jsonify, url_for
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/predict', methods=['POST']):
    def predict_api():
        data = request.json['data']
        print(f'my data: {data}')
        #Since the data is in json format (dictionary), we will have to reshape it in a list format and np array
        data_in_array = np.array(list(data.values())).reshape(1, -1)
        print(f'my data in array format: {data_in_array}')
        new_data = scalar.transform(data_in_array)
        prediction = model.predict(new_data)
        print(f'prediction is: {prediction[0]}')
        retrun jsonify(prediction[0])
        
        
if __name__ == '__main__':
    app.run(debug=True)