import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from utils import load_estimator

# instantiate Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """
    This is the home page.
    """
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    This is the predictions page.
    """
    # load estimator
    estimator = load_estimator()
    reg = estimator.get('reg') 
    le_location = estimator.get('location')
    # get the data from the form
    new_data = [[request.form.get('location'), request.form.get('bed'), request.form.get('bath'), 
    request.form.get('toilet'), request.form.get('pkn_space')]]
    # convert to array
    new_data = np.array(new_data)
    # encode the location
    new_data[:, 0] = le_location.transform(new_data[:, 0])
    # make predictions
    price = reg.predict(new_data)
    # convert the price from log_price to actual price
    act_price = np.exp(price) + 1
    act_price = round(act_price[0], 0)  # round to the neaarest Naira
    return render_template('index.html', prediction_text=f"The estimated cost of the property is NGN {act_price:,}")


@app.route('/predict_api', methods=['POST'])
def predict_api():
    """
    Make predictions using the API.
    """
    # load estimator
    estimator = load_estimator()
    reg = estimator.get('reg') 
    le_location = estimator.get('location')
    # get data from user
    data = request.get_json()
    new_data = {}  # empty dict
    # add the input as a list from postman to the dictionary
    new_data['location'] = [data['location']]
    new_data['bed'] = [data['bed']]
    new_data['bath'] = [data['bath']]
    new_data['toilet'] = [data['toilet']]
    new_data['pkn_space'] = [data['pkn_space']]
    # convert dictionary to dataframe
    df = pd.DataFrame.from_dict(new_data, orient='columns')
    # con vert to array
    new_data = df.to_numpy()
    # encode the location
    new_data[:, 0] = le_location.transform(new_data[:, 0])
    # make predictions
    price = reg.predict(new_data)
    # convert the price from log_price to actual price
    act_price = np.exp(price) + 1
    act_price = round(act_price[0], 0)  # round to the neaarest Naira
    return {'Estimated_cost': act_price}



if __name__ == '__main__':
    app.run(debug=True)