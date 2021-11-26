import numpy as np
import scipy.stats as stats
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


'''
this function gives an overview about the percantage of NaN values in a dataframe
'''
def percantage_null(data):
    nulls = pd.DataFrame(data.isna().sum()*100/len(data), columns=['percentage'])
    print(nulls.sort_values('percentage', ascending = False))


''' 
this function shows the distribution of the categorical values in the columns
input is a dataframe and the size of the plot 
output are a plot for every column
'''    
def plot_column_distribution(df, max_plots, plots_per_row):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] 
    max_plots, max_plots = df.shape
    columnNames = list(df)
    nGraphRow = (max_plots + plots_per_row - 1) / plots_per_row
    plt.figure(num = None, figsize = (6 * plots_per_row, 8 * plots_per_row), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(max_plots, plots_per_row)):
        plt.subplot(plots_per_row, plots_per_row, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()



''' 
this two functions shows the correlation of the categorical values in the input columns
input is a dataframe and the columns we want the correlations for 
output are if the null hypothesis is rejected or not for every combination of columns
'''    
def chi_square_execute(data, columns=[]):
    for i in columns:
        for j in columns:
            if i != j:
                chi_square(data, i, j)
    
def chi_square(data, m, n):
    data_crosstab = pd.crosstab(data[m], data[n], margins=True, margins_name="Total")
    # significance level
    alpha = 0.05
    # Calcualtion of Chisquare test statistics
    chi_square = 0
    rows = data[m].unique()
    columns = data[n].unique()
    for i in columns:
        for j in rows:
            O = data_crosstab[i][j]
            E = data_crosstab[i]['Total'] * data_crosstab['Total'][j] / data_crosstab['Total']['Total']
            chi_square += (O-E)**2/E
    print("\n--------------------------------------------------------------------------------------")
    print("\n--------------------------------------------------------------------------------------")
    print("H₀: column", m, " and column", n, "are independent, i.e. no relationship")
    print("H₁: column", m, " and column", n, "are independent, i.e. ∃ a relationship")
    print("α = 0.05")
   

# The p-value approach
    print("The p-value approach: The p-value approach to hypothesis testing in the decision rule")
    p_value = 1 - stats.norm.cdf(chi_square, (len(rows)-1)*(len(columns)-1))
    conclusion = "Failed to reject the null hypothesis."
    if p_value <= alpha:
        conclusion = "Null Hypothesis is rejected."
        
    print("chisquare-score is:", chi_square, " and p value is:", p_value)
    print(conclusion)
    
    # The critical value approach

    print("The critical value approach: The critical value approach to hypothesis testing in the decision rule")
    critical_value = stats.chi2.ppf(1-alpha, (len(rows)-1)*(len(columns)-1))
    conclusion = "Failed to reject the null hypothesis."
    if chi_square > critical_value:
        conclusion = "Null Hypothesis is rejected."
        
    print("chisquare-score is:", chi_square, " and p value is:", critical_value)
    print(conclusion)
    
    
''' 
this functions gives the boxcox transoformation to the input columns
input is a dataframe - the function select only the numerical columns
output are the transformed columns
'''      
def boxcox_transform(data):
    numeric_cols = data.select_dtypes(np.number).columns
    _ci = {column: None for column in numeric_cols}
    for column in numeric_cols:
        data[column] = np.where(data[column]<=0, np.NAN, data[column]) 
        data[column] = data[column].fillna(data[column].mean())
        transformed_data, ci = stats.boxcox(data[column])
        data[column] = transformed_data
        _ci[column] = [ci] 
    return data, _ci




''' 
this functions removes the outliers from the input columns
input is a dataframe, threshold, columns to remove outliers, columns to skip
output are the columns with removed outliers
'''    
def remove_outliers(data, threshold=1.5, in_columns=[], skip_columns=[]):
    for column in in_columns:
        if column not in skip_columns:
            upper = np.percentile(data[column],75)
            lower = np.percentile(data[column],25)
            iqr = upper - lower
            upper_limit = upper + (threshold * iqr)
            lower_limit = lower - (threshold * iqr)
            data = data[(data[column]>lower_limit) & (data[column]<upper_limit)]
    return data

