# House Price In Lagos Prediction

[![house-in-lagos.jpg](https://i.postimg.cc/0NyZtLGm/house-in-lagos.jpg)](https://postimg.cc/pm3Drc6X)

Image credit: [Nigeria Property Centre](https://nigeriapropertycentre.com)

## Project Overview

* Created a web app that predicts the price of houses in Lagos (RMSE ~ 0.36) which helps potential house owners estimate the price of the house they are about to purchase.
* Scraped over 8000 houses from Nigeria Property Centre using Python and BeautifulSoup.
Optimised Random Forest Regressor using GridSearchCV to obtain the best model.
* Built an API using flask.

## Packages/Tools Used

Python Version: 3.9
Packages: BeautifulSoup, Request, Numpy, Matplotlib, Seaborn, Scikit Learn, Pickle, and Flask.

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

* extracted the address.
* parsed the numeric data out of bed, bath, toilet, parking space and price.
* removed aberrant entries and outliers.
* replaced the missing values with the median values.

## EDA

## Model Building

## Model Performance

## Flask App

[![app-interface.jpg](https://i.postimg.cc/qB3Jwmx0/app-interface.jpg)](https://postimg.cc/yW7CYyGr)
