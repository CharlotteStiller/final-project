# using e-commerce ratings for product development

The objective of this project is to build a model that is able to predict the rating of products in e-commerce and to find out what its need to put together the ideal product for a e-commerce shop. 

In order to do this, I used web scraping and made use of Python and Tableau.

![alt text](https://img.freepik.com/vecteurs-libre/gens-tiennent-etoiles-illustration-concept-illustration-concept-client-commentaires-illustration-style-cartoon-plat_313437-1.jpg?size=626&ext=jpg)

## About the project

I worked with a dataset that I got from scraping the website of one of the leading beauty e-commerce companies in Europe. 

I wanted to understand which attributes of beauty products drive customer ratings. Products are rated on a scale from 1 to 5 stars.

The goal of the classification project is to train a model to predict the rating of a product based on its attributes. The analysis is the base to identify gaps in the product range and therefore opportunities to create the next best-selling product for an e-commerce shop.

## Dataset 
For the project I scraped details from 50.000 products with the following columns:  


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
| age              | For which product is recommended   | 20+                       |
| number_rating    | How many people rate the product   | 55                        |
| rating           | Star rating 1-5                    | 4,5                       |
| url              | URL ID                             | 50000050                  |



## Workflow


1. **Scraping the data with Beautiful Soup**
    - Files: scraping.ipynb / helper_scraping.py
    - Scraped 15 different attributes from 50.000 products that could give insights about products and their rating 

1. **Cleaning the dataset**
    - Files: cleaning_data_first_insights.ipynb / helper: helper_cleaning_first_insights.py
    - Cleaned and selected relevant data. Encoded the columns characteristics, effect, product_award.
  
2.  **Logistic regression / Classification in Python** 
    - Files: EDA_model.ipynb / helper_EDA_model.py
    - EDA
    - Data processing, feature engineering
    - Model evaluation
    - Overview - model results

  
3. **Visualize the data and storytelling in Tableau** 
    - Files: rating_attributes.twb 
    - Extracted attributes of the rated products and visualize them 
    - Tableau Story: Brings the conclusions together to build the perfect product  


## Conclusions
Note: For futher details, please refer to the related files


1.  **Logistic regression / Classification in Python** 
- Logistic Regression with changed class weights fits best for this dataset. Highest recall for rating 1 and rating 2. Accuracy score 0.77.  
- Next step to evaluate this model: Cut the variables which do not improve the prediction and improve the weight/balance


2. **Analyse and vizualize the data in Tableau** 
- The perfect must-have product for this e-commerce shop would unites all of the following demands:
- Category: Body 
- Scope: Hands 
- Type: bath additional or bodylotion
- Price: 70-80 € 
- Size: 75-100 ml/g 
- Attributes: Smoothing, gloss-imparting, moisturizing, nourishing and free from paraben, paraffin, lactose, micro-plastic, gluten 
- On the base of this knowledge I would recommend a bath oil that unites all of these demands 

## Libaries 
- BeautifulSoup
- IPython
- pandas
- scipy
- seaborn
- matplotlib
- numpy
- imblearn
- sklearn
