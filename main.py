import pandas as pd
import math
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

def convertTo(priceEuro=1,conversionTax=0):
  return math.floor((priceEuro * conversionTax)*100)/100

df = pd.read_excel('https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/res/<id>/')
def handler_exercise(id):
    match int(id):
        case 1:
            quartiere = request.args.get('quartiere')
            result = df[(df['neighborhood'].isna() == False) & (df['neighborhood'] == quartiere)].sort_values(by='date')
            return render_template('result.html', products=result.to_html())
        case 2:
            return render_template('index.html')
        case 3: 
            result = df.sort_values(by='neighborhood',ascending=True)[['neighborhood']].drop_duplicates()
            return render_template('result.html', products=result.to_html())
        case 4:
            zona = request.args.get('zona')
            result = df[df['neighborhood'] == zona][['price']].mean()
            return render_template('result.html', products=result.to_html())
        case 5:
            return render_template('index.html')
        case 6:
            return render_template('index.html')
        case _:
            return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)