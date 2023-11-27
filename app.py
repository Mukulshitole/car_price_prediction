import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and car data only once outside the routes
model = pickle.load(open("LinearRegressionModel.pkl", 'rb'))
car = pd.read_csv("Cleaned Car.csv")

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())

    return render_template('index.html', companies=companies, car_models=car_models, year=year, fuel_type=fuel_type)

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')  # Fix the form field name
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    driven = int(request.form.get('kilo_driven'))

    # Create a DataFrame to match the model's input structure
    input_data = pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                               data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5))

    prediction = model.predict(input_data)
    # Assuming your prediction is a single numeric value, round it to two decimal places
    rounded_prediction = np.round(prediction[0], 2)

    return str(rounded_prediction)

if __name__ == "__main__":
    app.run(debug=True)
