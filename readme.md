# House Price In Lagos Prediction

[![house-in-lagos.jpg](https://i.postimg.cc/0NyZtLGm/house-in-lagos.jpg)](https://postimg.cc/pm3Drc6X)

Image credit: [Nigeria Property Centre](https://nigeriapropertycentre.com)

## Project Overview

* Created a web app that predicts the price of houses in Lagos (RMSE ~ 0.36) which helps potential house owners estimate the price of the house they are about to purchase.
* Scraped over 8000 houses from Nigeria Property Centre using Python and BeautifulSoup.
Optimised Random Forest Regressor using GridSearchCV to obtain the best model.
* Built an API using flask.

## Packages/Tools Used

* Python Version: 3.9
* BeautifulSoup
* Request
* Numpy
* Matplotlib
* Seaborn
* Scikit-Learn
* Pickle
* Flask.

## Data

The data was scraped from [Nigeria Property Centre](https://nigeriapropertycentre.com). The data was scraped in batches to avoid sending too many requests at Nigeria Property Centre's server.
The data was stored as a csv file after the data collection. The scraped data contains:

* Title
* Address
* Number of bedrooms
* Number of bathrooms
* Number of toilets
* Parking Space

## Data Cleaning

The features (columns) contained messy entries and were tidied using regular expression and some custom functions. The following steps were taken.

* extracted the address and the building type.
* parsed the numeric data out of bed, bath, toilet, parking space and price.
* removed aberrant entries and outliers.
* replaced the missing values with the median values.
* filtered out houses with fewer locations to avoid skewing the analysis.

## EDA

* The count of each loacation used in the data analysis after filtering out outliers and abnormal values.
[![image-2021-06-20-103750.png](https://i.postimg.cc/ydwFjDLZ/image-2021-06-20-103750.png)](https://postimg.cc/Q9J9xdG8)

* The important features that affect the price of houses in Lagos are:
![feature_importance](https://i.postimg.cc/KY3X3LLS/image-2021-06-20-102809.png)

## Model Building

* The categorical feature (location) was transformed into numerical data and I used a test size of 20% for the data modelling.
* I applied log transformation on the price which transformed the price to a fairly Gaussian distribution.
* Root mean squared error (**RMSE**) which is the square root of the sum of the difference between the true value and the predicted value was the metric used to evaluate the performance of the model.
* **Multiple Linear Regression**, **Ridge Regression**, **Random Forest Regressor**, **Ada Boost Regressor** and **Support Vector Regressor** models were all built.
* **Random Forest Regressor** was chosen because it had a lower RMSE

## Model Performance

* Random Forest Regressor model performed better than other models.
* The optimal parameters were chosen using GridSearchCV.
[![evaluation.jpg](https://i.postimg.cc/x1SN4yfg/evaluation.jpg)](https://postimg.cc/fJBb3d00)

## Flask App

I built a flask app and an API. The app and the API take in a list of values and output an estimated range of the price of the house.
The [web app](https://lagoshouseprice.herokuapp.com) was deployed on the cloud using Heroku.
[![app-interface.jpg](https://i.postimg.cc/ht9TDZyH/app-interface.jpg)](https://postimg.cc/RWZNGdzR)
