from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredicationPipeline
from src.utils import load_object
from src.logger import logging

application = Flask(__name__)

app = application

# route for home page
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        pred_df = data.get_data_as_dataframe()

        logging.info(f"Dataframe for Prediction: {pred_df}")

        predict_pipeline = PredicationPipeline()
        result = predict_pipeline.predict(pred_df)
        logging.info(f"Prediction Result: {result}")

        return render_template('home.html', prediction_text=f"Predicted Score: {result[0]:.2f}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)