#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


pip install dash pandas


# In[26]:


sales_data = pd.read_csv('salesdataset (1).csv')


# In[27]:


sales_data.head(10)


# In[29]:


sales_data.shape


# In[30]:


sales_data.columns


# In[31]:


sales_data.info()


# In[33]:


# Removing Null Values
sales_data.dropna(subset=['Discount Amount','Sales Price', 'Item Number'],inplace=True)


# In[34]:


# Generating descriptive statistics
sales_data.describe()


# In[35]:


sales_data01 = sales_data.copy()


# In[36]:


sales_data01['Item Class'].value_counts()


# In[42]:


import pandas as pd

# Assuming 'Invoice Date' is not in datetime format
sales_data['Invoice Date'] = pd.to_datetime(sales_data['Invoice Date'])

# Creating Year, Month, Quarter, Day Columns in Sales_data01
sales_data01['Invoice_Year'] = sales_data['Invoice Date'].dt.year
sales_data01['Invoice_Month'] = sales_data['Invoice Date'].dt.month
sales_data01['Invoice_Quarter'] = sales_data['Invoice Date'].dt.quarter
sales_data01['Invoice_Day'] = sales_data['Invoice Date'].dt.day


# In[43]:


sales_data01.info()


# In[47]:


# Creating DataFrame only with neccessary values.
sales_data02 = sales_data01[['Custkey','Item','Invoice Date','Invoice_Year','Invoice_Quarter', 'Invoice_Month',
                           'Invoice_Day', 'Sales Quantity', 'Sales Amount Based on List Price','Discount Amount',
                           'Sales Amount', 'Sales Margin Amount','Sales Cost Amount','Sales Rep','U/M','List Price',
                           'Sales Price']]


# In[48]:


sales_data02.isnull().sum()


# In[49]:


# Checking the correlation
plt.figure(figsize=(12,8))
sns.heatmap(sales_data.corr(method='pearson'), annot=True, vmin=-1, vmax=1, cmap='YlGnBu')


# #Observations:
# 1 Discount Amount is highly related to Sales Amount, Sales Cost Amount, Sales Amount Based on List Price & Sales Margin Amount and moderately related to Sales Quantity.
# 2- List Price highly related to sales price and has no relations with Sales amount, Sales cost amount, Sales amount based on list price & sales margin amount.
# 3- Sales quantity is moderately related to Sales amount, discount amount, sales margin amount.
# Their is no relation Between Sales Rep and Sales Amount, Sales Margin Amount.
# 

# In[51]:


# set style
sns.set(style = 'darkgrid')
DaySalesInsights = sales_data01.copy()
DaySalesInsights['Invoice_Date'] = pd.to_datetime(sales_data01['Invoice Date']).dt.date
top10sales = DaySalesInsights.groupby('Invoice_Date').sum().sort_values('Sales Amount', ascending = False)
top10sales = top10sales.reset_index().head(10)
sns.catplot(y = 'Sales Amount', x = 'Invoice_Date', data = top10sales, aspect = 2,palette='turbo',kind="bar")
plt.title('Top 10 Days When Sales Were Highest')
top10sales[['Sales Amount']]
plt.show()


# In[66]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import interact
import ipywidgets as widgets

# Set style
sns.set(style='darkgrid')

# Assuming 'sales_data01' and 'sales_data' DataFrames are available

# Convert 'Invoice Date' to datetime
sales_data01['Invoice_Date'] = pd.to_datetime(sales_data01['Invoice Date']).dt.date

# Function to plot top days
def plot_top_days(start_date, end_date):
    filtered_data = sales_data01[(sales_data01['Invoice_Date'] >= start_date) & (sales_data01['Invoice_Date'] <= end_date)]
    top_sales = filtered_data.groupby('Invoice_Date').sum().sort_values('Sales Amount', ascending=False).head(10)

    # Plotting
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_sales.index, y='Sales Amount', data=top_sales, palette='turbo')
    plt.title('Top 10 Days When Sales Were Highest')
    plt.xlabel('Invoice Date')
    plt.ylabel('Sales Amount')
    plt.xticks(rotation=45)
    plt.show()

# Get date range for the slicer
date_range = pd.date_range(sales_data01['Invoice_Date'].min(), sales_data01['Invoice_Date'].max(), freq='D')

# Create interact widget for the date slicer
interact(
    plot_top_days,
    start_date=widgets.DatePicker(value=date_range.min(), description='Start Date'),
    end_date=widgets.DatePicker(value=date_range.max(), description='End Date')
)
plt.figure(figsize=(18,7))
plt.pie('Sales Amount',labels='Invoice_Date',data = top10sales,
        autopct='%1.2f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.title('Contribution Of Sales Amount Among 10 Days')
plt.legend(round(top10sales['Sales Amount'],2), loc=7, fontsize = 'x-large')
plt.show()

top10profits = DaySalesInsights.groupby('Invoice_Date').sum().sort_values('Sales Margin Amount', ascending = False)
top10profits = top10profits.reset_index().head(10)
sns.catplot(y = 'Sales Margin Amount', x = 'Invoice_Date', data = top10profits, aspect = 2,palette='turbo',kind="bar")
plt.title('Top 10 Days When Profits Were Highest')
top10profits[['Sales Margin Amount']]

Yearly_Sales =  sales_data02[['Custkey','Item','Invoice Date','Invoice_Year','Invoice_Month',
                            'Sales Quantity', 'Sales Amount Based on List Price','Discount Amount',
                           'Sales Amount', 'Sales Margin Amount','Sales Cost Amount','Sales Rep','U/M','List Price',
                           'Sales Price']]
Yearly_Sales01 = Yearly_Sales.groupby('Invoice_Year').sum().reset_index()
sns.catplot(y = 'Sales Amount', x = 'Invoice_Year', data = Yearly_Sales01, palette='Reds',kind="bar")
plt.xlabel('Year')
plt.ylabel('Sales Amount')
plt.title('Yearly Sales')
Yearly_Sales01[['Invoice_Year', 'Sales Amount']]
#Plotting Piechart to know Sales Share among 3 years
plt.figure(figsize=(17,6))
plt.pie('Sales Amount',labels='Invoice_Year',data=Yearly_Sales01,
        autopct='%1.2f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.title('Sales Contribution')
plt.legend(round(Yearly_Sales01['Sales Amount'],2), loc=7, fontsize = 'xx-large')
plt.show()
plt.figure(figsize=(20, 7))
sales_data01['Sales Rep'].value_counts().plot.bar()
plt.xlabel('Sales Rep')
plt.ylabel('Count')
print('Sales Rep "108" were used most often while sales rep "150" has been used the least.')
Yearly_Monthwise_Sales = sales_data02.groupby(['Invoice_Year','Invoice_Month']).sum().reset_index()
Yearly_Monthwise_Sales.iloc[:,6:].describe()
sns.catplot(y = 'Sales Amount', x = 'Invoice_Month', data = Yearly_Monthwise_Sales, palette='turbo',kind="bar",
            col='Invoice_Year', col_wrap=3)
High_Profit = sales_data01.groupby('Item').sum().sort_values('Sales Margin Amount', ascending=False).reset_index()
High_Profit.index+=1
High_Profit=High_Profit.reset_index().rename(columns={"index":"Rank"})
plt.figure(figsize=(8,7))
sns.barplot(x='Rank', y='Sales Margin Amount',data = High_Profit.head(10), palette = 'turbo')
plt.legend(High_Profit['Item'].head(10))
High_Profit[['Rank', 'Item', 'Sales Margin Amount']].head(10)
plt.figure(figsize=(22,8))
plt.pie('Sales Margin Amount',labels='Rank',data=High_Profit.head(10),autopct='%1.2f%%',
        shadow=True,startangle=90, explode = (0.13, 0, 0, 0, 0, 0, 0, 0, 0, 0.1))
plt.axis('equal')
plt.title('Top 10 Item by Sales Margin Amount')
plt.legend(High_Profit['Item'].head(10), loc=7, fontsize = 'xx-large')
plt.show()


# In[ ]:


#Report
Problem statement
•Sales management has gained importance to meet increasing competition and the need for improved methods of distribution to reduce cost and to increase profits. Sales management today is the most important function in a commercial and business enterprise.
•Do ETL : Extract-Transform-Load some Amazon dataset and find for me Sales-trend -> month wise , year wise , yearly-month wise
•Find key metrics and factors and show the meaningful relationships between attributes.

Solution
Sales trended down, resulting in a 10.42% decrease between January 2017 and January 2018. Sales started trending down in January 2017, falling by 10.42% ($23,69,531.66) in 4 quarters. Sales dropped from $2,27,29,856.29 to $2,03,60,324.63 during its steepest decline between January 2017 and January 2018. Sales trended down, resulting in a 5.06% decrease between January 2018 and October 2019. Sales started trending up on April 2019, rising by 6.22% ($11,31,718.23) in 2 quarters. Sales jumped from $1,81,99,115.14 to $1,93,30,833.37 during its steepest incline between April 2019 and October 2019.
Profits trended down, resulting in a 6.82% decrease between January 2017 and January 2018. Profits started trending down in January 2017, falling by 6.82% ($6,52,731.37) in 4 quarters. Profits dropped from $95,66,880.82 to $89,14,149.45 during their steepest decline between January 2017 and January 2018. Profits trended down, resulting in a 15.16% decrease between January 2018 and October 2019.
At $87,73,249.43, Better Large Canned Shrimp had the highest Sales and was 42,85,596.56% higher than Kiwi Lox, which had the lowest Sales at
$204.71. Sales and total Profits are negatively correlated with each other. Better Large Canned Shrimp accounted for 9.10% of Sales. Sales and Profits diverged the most when the Item was Better Large Canned Shrimp when Sales were $57,32,729.64 higher than Profits.

Top 10 sales margin
he top item is Better Large Canned Shrimp, which has a sales margin of 19.21%. This means that for every $100 of Better Large Canned Shrimp that the store sells, it makes a profit of $19.21.
The second item is Better Fancy Canned Sardines, which has a sales margin of 16.39%.
The third item is Tell Tale Red Delicious Apples, which has a sales margin of 9.95%.
The fourth item is High Top Dried Mushrooms, which has a sales margin of 6.70%.
The fifth item is Big Time Frozen Cheese Pizza, which has a sales margin of 6.96%.
Every year invoice
In the 2017 the invoice was the highest in the first month and 6 and 9 month have the same result.
Sales Contribution
The 2017 have the highest sales contribution followed by 2019 as the second highest.
Top 10 days when sales were highest
Highest Profit Day: December 24, 2017, with a sales margin amount of around 600,000 (currency units).
Other High-Profit Days:
June 26, 2017
June 18, 2017
September 29, 2017
July 8, 2019
June 30, 2019
March 19, 2018
February 12, 2018
December 1, 2017
September 3, 2017
Date Range: The graph covers a period from September 2017 to July 2019.
Insights:

Seasonality: The top 3 dates for profits all fall within the holiday season (June and December), suggesting a strong influence of holidays on sales.
Variability: Profits vary significantly across different days, with the highest day being over 6 times more profitable than the lowest day in the top 10.
Potential for Further Analysis: It would be valuable to explore factors that might contribute to these variations, such as marketing campaigns, product launches, or external events.
Additional Considerations:


# 
