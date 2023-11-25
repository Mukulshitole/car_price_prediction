import pandas as pd
from flask import  Flask,render_template

app=Flask(__name__)
car=pd.read_csv("Cleaned Car.csv")
@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    # .unique() returns an array of unique values in that column.
    # sorted() sorts those unique values alphabetically or numerically.
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(),reverse=True)
    #This line extracts the 'year' column from the DataFrame car, retrieves unique values, and sorts them in reverse order (from highest to lowest).

    fuel_type = sorted(car['fuel_type'].unique())

    return render_template('index.html',companies=companies,car_models=car_models,year=year,fuel_type=fuel_type)


if __name__=="__main__":
    app.run(debug=True)
    ###56.47