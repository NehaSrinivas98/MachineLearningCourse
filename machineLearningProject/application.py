from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
application = Flask(__name__)
app = application

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = CustomData(
            gender= request.form.get('gender'),
            race_ethnicity= request.form.get('ethnicity'),
            parental_level_of_education= request.form.get('parental_level_of_education'),
            lunch= request.form.get('lunch'),
            test_preparation_course= request.form.get('test_preparation_course'),
            reading_score= int(request.form.get('reading_score')),
            writing_score= int(request.form.get('writing_score'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        preds = predict_pipeline.predict(pred_df)
        print('pred',preds)
        return render_template('index.html', results=preds[0])
if __name__ == "__main__":
    app.run(host="0.0.0.0",)