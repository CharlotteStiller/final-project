# final-bootcamp

The objective of this project was to is to build a model that will provide insight into product clustering and rating of beauty product in e-commerce,  as well as answer additional questions by top management related to the matter.

In ordert o to this, I used web scraping, agile project planning in Github and made use of SQL, Redshift, Python and Tableau.

## About the project

I worked with two datasets. The first data I've got from scraping the web of one of the
leading beauty e-commerce company in europe. The second I've got through redshift from a abo-commerce company.   

We want to understand the demographics and other characteristics of beauty products that are well rated by the customers. Both datasets have ratings from 1-5 stars for the worst and the best products. 

The goal of the classification project is to analyse the characteristics of the beauty products and to train a model to predict if a product get rated with 5 stars or not. 


## Dataset Web Scraping 
For the project I scraped details from 18.000??? products with the following columns:  


| Column           | Description                        | Example                   |
|------------------|------------------------------------|---------------------------|
| item_nb          | Item number                        | 037414                    |
| brand            | Name of the brand                  | Clinique                  |
| product          | Name of the product                | Lash Power                |
| typ              | Typ of the product                 | Mascara                   |
| size             | ml of the product                  | 6ml                       |
| price            | Price in €                         | 18,39                     |
| category         | Hair, Face, Make-up, Body, Perfume | Make-up                   |
| scope            | Area of application                | Face                      |
| charesteristics  | Find trending charesteristics      | highly pigmented, shaping |
| effect           | Desired effect of the product      | refining                  |
| product_award    | Find trending awards               | perfume free              |
| ingredients      | Find trending topics               | Jojoba, Aqua              |
| age              | For which product is recommended   | 20+                       |
| number_rating    | How many people rate the product   | 55                        |
| rating           | Star rating 1-5                    | 4,5                       |
| url              | URL ID                             | 50000050                  |


## Dataset Redshift 

| Column           | Description                        | Example                   |
|------------------|------------------------------------|---------------------------|
| item_nb          | Item number                        | 037414                    |
| size             | ml of the product                  | 6ml                       |
| price            | Price in €                         | 18,39                     |
| category         | Hair, Face, Make-up, Body, Perfume | Make-up                   |
| number_rating    | How many people rate the product   | 55                        |
| rating           | Star rating 1-5                    | 4,5                       |



## Workflow


1. **Scraping the data with Beautiful Soup**
    - Files: web_scraping.ipynb / helper.py / df.csv
    - Scrape five categories of beauty products to get all characteristics that could give us insights 

  
2.  **Logistic regression / Classification in Python** 
    - Files: Solutions_Python - Classification.ipynb / helper.py
    - EDA
    - Data processing, feature engineering
    - Model evaluation
    - Overview - model results

  
3. **Visualize the data and storytelling in Tableau** 
    - Files: Conclusions.ipynb / Conclusions.twb 
    - Extract demographics and other characteristics of the rated products and visualize them 
    - Give some insights in the conclusions 


## Conclusions
Note: For futher details, please refer to the related files


1.  **Logistic regression / Classification in Python** 
- Placeholder: 
- Logistic Regression with changed class weights fits best for this dataset. Highest Yes recall: 0.69.  
- Next step to evaluate this model: Cut the variables which do not improve the prediction and improve the weight/balance
- For the next marketing study I would recommend to change the questions which have no relationship to the target variable (Like shown in point 5.2.), target people who live in a household of the size 3 or 4, and to build bins (For example house hold size 5-9) 


2. **Analyse and vizualize the data in Tableau** 
- Placeholder: 
- There is a huge jump in average balance from Q1 to Q2 for households with size 8.
- The jump is caused by the fact that only one out of 18.000 customers has a household size of 8 and this particular person has an unusually high balance.

## Libaries 
- helper_classification 
- IPython
- pandas as pd
- scipy
- seaborn as sns
- matplotlib
- numpy as np
- imblearn
- sklearn
- warnings

