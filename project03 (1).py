#!/usr/bin/env python
# coding: utf-8

# In[43]:


#!/usr/bin/env python
# coding: utf-8


# In[3]:

# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import interact
import ipywidgets as widgets
import streamlit as st
import numpy as np


# In[10]:

# In[4]:


sales_data = pd.read_csv(r'C:\Users\deepankar\Downloads\salesdataset (1).csv')


# In[11]:

# In[5]:


sales_data.head(10)


# In[12]:

# In[47]:


sales_data.columns


# In[13]:

# In[48]:


sales_data.dropna(subset=['Discount Amount','Sales Price', 'Item Number'],inplace=True)


# In[14]:

# Generating descriptive statistics

# In[49]:


sales_data.describe()


# In[15]:

# In[50]:


sales_data01 = sales_data.copy()


# In[16]:

# Assuming 'Invoice Date' is not in datetime format

# In[51]:


sales_data['Invoice Date'] = pd.to_datetime(sales_data['Invoice Date'])


# Creating Year, Month, Quarter, Day Columns in Sales_data01

# In[52]:


sales_data01['Invoice_Year'] = sales_data['Invoice Date'].dt.year
sales_data01['Invoice_Month'] = sales_data['Invoice Date'].dt.month
sales_data01['Invoice_Quarter'] = sales_data['Invoice Date'].dt.quarter
sales_data01['Invoice_Day'] = sales_data['Invoice Date'].dt.day


# In[17]:

# In[53]:


sales_data01.info()


# In[18]:

# In[54]:


sales_data02 = sales_data01[['Custkey','Item','Invoice Date','Invoice_Year','Invoice_Quarter', 'Invoice_Month',
                           'Invoice_Day', 'Sales Quantity', 'Sales Amount Based on List Price','Discount Amount',
                           'Sales Amount', 'Sales Margin Amount','Sales Cost Amount','Sales Rep','U/M','List Price',
                           'Sales Price']]


# In[20]:

# Checking the correlation

# In[66]:


# Select only numeric columns for correlation
numeric_columns = sales_data.select_dtypes(include=[np.number])

# Calculate correlation on numeric columns only
correlation_matrix = numeric_columns.corr(method='pearson')

# Plotting the heatmap
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, vmin=-1, vmax=1, cmap='YlGnBu', ax=ax)
st.pyplot(fig)


# In[21]:

# set style

# In[56]:


sns.set(style='darkgrid')
DaySalesInsights = sales_data01.copy()
DaySalesInsights['Invoice_Date'] = pd.to_datetime(sales_data01['Invoice Date']).dt.date
top10sales = DaySalesInsights.groupby('Invoice_Date').sum().sort_values('Sales Amount', ascending=False)
top10sales = top10sales.reset_index().head(10)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(y='Sales Amount', x='Invoice_Date', data=top10sales, palette='turbo', ax=ax)
ax.set_title('Top 10 Days When Sales Were Highest')
st.pyplot(fig)


# In[22]:

# In[57]:


fig, ax = plt.subplots(figsize=(18, 7))
ax.pie('Sales Amount', labels='Invoice_Date', data=top10sales, autopct='%1.2f%%', shadow=True, startangle=90)
ax.axis('equal')
ax.set_title('Contribution Of Sales Amount Among 10 Days')
ax.legend(round(top10sales['Sales Amount'], 2), loc=7, fontsize='x-large')
st.pyplot(fig)


# In[29]:

# Assuming 'sales_data01' and 'sales_data02' DataFrames are available<br>
# Make sure to replace these with your actual data loading logic

# Load data

# In[58]:


sales_data01 = pd.read_csv(r'salesdataset (1).csv')
sales_data02 = pd.read_csv(r'salesdataset (1).csv')


# Set style

# In[59]:


sns.set(style='darkgrid')


# Convert 'Invoice Date' to datetime

# In[60]:


sales_data01['Invoice_Date'] = pd.to_datetime(sales_data01['Invoice Date']).dt.date


# Function to plot top days

# In[61]:


def plot_top_days(start_date, end_date):
    filtered_data = sales_data01[(sales_data01['Invoice_Date'] >= start_date) & (sales_data01['Invoice_Date'] <= end_date)]
    top_sales = filtered_data.groupby('Invoice_Date')['Sales Amount'].sum().sort_values(ascending=False).head(10)

    # Plotting
    st.subheader("Top 10 Days When Sales Were Highest:")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=top_sales.index, y=top_sales.values, palette='turbo', ax=ax)
    plt.title('Top 10 Days When Sales Were Highest')
    plt.xlabel('Invoice Date')
    plt.ylabel('Sales Amount')
    plt.xticks(rotation=45)
    st.pyplot(fig)


# Create interact widget for the date slicer

# In[62]:


st.sidebar.title("Date Range Slicer")
date_range = pd.date_range(sales_data01['Invoice_Date'].min(), sales_data01['Invoice_Date'].max(), freq='D')
start_date = st.sidebar.date_input("Start Date", date_range.min())
end_date = st.sidebar.date_input("End Date", date_range.max())


# Display interactive plot

# In[63]:


plot_top_days(start_date, end_date)


# Pie chart for sales contribution

# In[68]:


st.subheader("Contribution Of Sales Amount Among 10 Days:")
fig, ax = plt.subplots(figsize=(18, 7))
ax.pie('Sales Amount', labels='Invoice_Date', data=top10sales,
        autopct='%1.2f%%', shadow=True, startangle=90)
ax.axis('equal')
ax.set_title('Contribution Of Sales Amount Among 10 Days')
ax.legend(round(top10sales['Sales Amount'], 2), loc='best', fontsize='x-large')
st.pyplot(fig)


# #Report
# Problem statement
# •Sales management has gained importance to meet increasing competition and the need for improved methods of distribution to reduce cost and to increase profits. Sales management today is the most important function in a commercial and business enterprise.
# •Do ETL : Extract-Transform-Load some Amazon dataset and find for me Sales-trend -> month wise , year wise , yearly-month wise
# •Find key metrics and factors and show the meaningful relationships between attributes.
# 
# Solution
# Sales trended down, resulting in a 10.42% decrease between January 2017 and January 2018. Sales started trending down in January 2017, falling by 10.42% ($23,69,531.66) in 4 quarters. Sales dropped from $2,27,29,856.29 to $2,03,60,324.63 during its steepest decline between January 2017 and January 2018. Sales trended down, resulting in a 5.06% decrease between January 2018 and October 2019. Sales started trending up on April 2019, rising by 6.22% ($11,31,718.23) in 2 quarters. Sales jumped from $1,81,99,115.14 to $1,93,30,833.37 during its steepest incline between April 2019 and October 2019.
# Profits trended down, resulting in a 6.82% decrease between January 2017 and January 2018. Profits started trending down in January 2017, falling by 6.82% ($6,52,731.37) in 4 quarters. Profits dropped from $95,66,880.82 to $89,14,149.45 during their steepest decline between January 2017 and January 2018. Profits trended down, resulting in a 15.16% decrease between January 2018 and October 2019.
# At $87,73,249.43, Better Large Canned Shrimp had the highest Sales and was 42,85,596.56% higher than Kiwi Lox, which had the lowest Sales at
# $204.71. Sales and total Profits are negatively correlated with each other. Better Large Canned Shrimp accounted for 9.10% of Sales. Sales and Profits diverged the most when the Item was Better Large Canned Shrimp when Sales were $57,32,729.64 higher than Profits.
# 
# Top 10 sales margin
# he top item is Better Large Canned Shrimp, which has a sales margin of 19.21%. This means that for every $100 of Better Large Canned Shrimp that the store sells, it makes a profit of $19.21.
# The second item is Better Fancy Canned Sardines, which has a sales margin of 16.39%.
# The third item is Tell Tale Red Delicious Apples, which has a sales margin of 9.95%.
# The fourth item is High Top Dried Mushrooms, which has a sales margin of 6.70%.
# The fifth item is Big Time Frozen Cheese Pizza, which has a sales margin of 6.96%.
# Every year invoice
# In the 2017 the invoice was the highest in the first month and 6 and 9 month have the same result.
# Sales Contribution
# The 2017 have the highest sales contribution followed by 2019 as the second highest.
# Top 10 days when sales were highest
# Highest Profit Day: December 24, 2017, with a sales margin amount of around 600,000 (currency units).
# Other High-Profit Days:
# June 26, 2017
# June 18, 2017
# September 29, 2017
# July 8, 2019
# June 30, 2019
# March 19, 2018
# February 12, 2018
# December 1, 2017
# September 3, 2017
# Date Range: The graph covers a period from September 2017 to July 2019.
# Insights:
# 
# Seasonality: The top 3 dates for profits all fall within the holiday season (June and December), suggesting a strong influence of holidays on sales.
# Variability: Profits vary significantly across different days, with the highest day being over 6 times more profitable than the lowest day in the top 10.
# Potential for Further Analysis: It would be valuable to explore factors that might contribute to these variations, such as marketing campaigns, product launches, or external events.
# Additional Considerations:
# 
# 
# 

# In[ ]:
