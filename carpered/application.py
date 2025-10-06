from flask import Flask, render_template,request
import pickle
import pandas as pd

app = Flask(__name__)
model=pickle.load(open("LinearRegressionModel.pk1",'rb'))
car = pd.read_csv("Cleaned_Car_data.csv")

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    companies.insert(0,"select companies")
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique())
    fuel_types = sorted(car['fuel_type'].unique())
    return render_template('index.html', companies=companies, car_models=car_models, fuel_types=fuel_types, years=years)

@app.route('/predict',methods=['POST'])
def predict ():
    company=request.form.get('company')

    car_model=request.form.get('car_model')
    year=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    kms_driven=int(request.form.get('kilo_driven'))
    
    prediction= model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]],columns=['name','company','year','kms_driven','fuel_type']))
    return str(prediction)


if __name__ == "__main__":
    app.run(debug=True)
