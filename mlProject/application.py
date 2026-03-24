import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
application = Flask(__name__)
app = application

regressor = pickle.load(open('models/regressor.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))

@app.route('/')
def index():
    print(getattr(regressor, "feature_names_in_", "No feature names found"))
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        medinc = float(request.form['medinc'])
        house_age = float(request.form['houseage'])    
        ave_rooms = float(request.form['averooms'])
        ave_bedrms = float(request.form['avebedrms'])
        population = float(request.form['population'])
        ave_occup = float(request.form['aveoccupancy'])
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        new_data_scaled = standard_scaler.transform([[ medinc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude ]])
        result = regressor.predict(new_data_scaled)
        return render_template('home.html',result=result[0])
        
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)