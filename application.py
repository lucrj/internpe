from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
car = pd.read_csv("carpered\Cleaned_Car_data.csv")

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique())
    fuel_types = sorted(car['fuel_type'].unique())
    return render_template('index.html', companies=companies, car_models=car_models, fuel_types=fuel_types, years=years)

if __name__ == "__main__":
    app.run(debug=True)
