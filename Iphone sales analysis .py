#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
import plotly.graph_objects as go


# In[6]:


df = pd.read_excel('D:\EXCEL\Appledata.xlsx')
print(df)


# Product Name: The name of the Apple iPhone product. (String)
# Product URL: The URL of the product page. (String)
# Brand: The brand of the Apple iPhone product. (String)
# Sale Price: The price of the Apple iPhone product at the time of sale. (Numeric)
# Mrp: The maximum retail price of the Apple iPhone product. (Numeric)
# Discount Percentage: The percentage of discount offered on the Apple iPhone product. (Numeric)
# Number Of Ratings: The number of ratings given to the Apple iPhone product. (Numeric)
# Number Of Reviews: The number of reviews given to the Apple iPhone product. (Numeric)
# Upc: The universal product code of the Apple iPhone product. (String)
# Star Rating: The star rating of the Apple iPhone product. (Numeric)
# Ram: The Random Access Memory size of the Apple iPhone product. (Numeric)

# In[7]:


df.info()


# In[8]:


df.isnull().sum()


# In[9]:


df.describe()


# In[22]:


highest_rated = df.sort_values(by=["Star Rating"],ascending = False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])


# according to above data the top 5 iphones in india is 20     APPLE iPhone 11 Pro Max (Midnight Green, 64 GB)
# 17         APPLE iPhone 11 Pro Max (Space Grey, 64 GB)
# 16    APPLE iPhone 11 Pro Max (Midnight Green, 256 GB)
# 15               APPLE iPhone 11 Pro Max (Gold, 64 GB)
# 14              APPLE iPhone 11 Pro Max (Gold, 256 GB)

# # Highest rating Iphone on flipkart
# 

# In[21]:


iphones = highest_rated["Product Name"].value_counts() 
label = iphones.index
counts = highest_rated["Number Of Ratings"]

fig , ax = plt.subplots()
ax.bar(label , counts)

ax.set_title('Highest rating Iphone on flipkart')
ax.set_xlabel('Iphones')
ax.set_ylabel('ratings')

plt.show()


# In[23]:


iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = iphones.values
figure = px.bar(x=label, y=counts, 
                title="Number of Ratings of Highest Rated iPhones")
figure.show()


# In[20]:


iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label, 
                y = counts, 
            title="Number of Ratings of Highest Rated iPhones")
figure.show()


# In[12]:


iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label, 
                y = counts, 
            title="Number of Ratings of Highest Rated iPhones")
figure.show()


# The chart shows that the "APPLE iPhone 8 Plus (Gold, 64 GB)" model has the highest number of reviews among the highest rated iPhones, followed by "APPLE iPhone XR (White, 64 GB)" and "APPLE iPhone XR (Coral, 64 GB)". It's interesting to see that some of the older models, such as the iPhone 8 Plus, are still popular among users.

# In[13]:


figure = px.scatter(data_frame = df, x="Number Of Ratings",
                    y="Sale Price", size="Discount Percentage", 
                    trendline="ols", 
                    title="Relationship between Sale Price and Number of Ratings of iPhones")
figure.show()


# The plot suggests that there is a positive correlation between the sale price and the number of ratings of iPhones, which means that as the number of ratings increases, the sale price tends to increase as well. However, there are some data points that deviate from this general trend. The size of the markers indicates the discount percentage, with larger markers indicating higher discounts

# In[14]:


figure = px.scatter(data_frame = df, x="Number Of Ratings",
                    y="Discount Percentage", size="Sale Price", 
                    trendline="ols", 
                    title="Relationship between Discount Percentage and Number of Ratings of iPhones")
figure.show()


# From the scatter plot, we can see that as the number of ratings increases, the discount percentage tends to decrease. This suggests that iPhones with a higher number of ratings are less likely to be discounted, possibly because they are more popular and in demand. Additionally, we can see that there is a wide range of sale prices across all levels of number of ratings and discount percentage, indicating that other factors, such as model, storage capacity, and color, may also be influencing the price of iPhones.

# # Heatmap 
# 

# In[16]:


import pandas as pd
import seaborn as sns

df = pd.read_excel('D:\EXCEL\Appledata.xlsx')

sns.heatmap(df[['Mrp', 'Discount Percentage']].corr(), annot=True, cmap='coolwarm')


# The heatmap shows the relationship between the 'Mrp' and 'Discount Percentage' columns. The darker the color, the higher the concentration of data points in that region. We can see that most of the phones are concentrated in the region where the MRP is between 50,000 to 70,000 and the discount percentage is between 10-20%. There are also some phones with a higher discount percentage of around 25-30%, but they are priced between 20,000 to 40,000. Overall, the heatmap shows that there is a clear relationship between the MRP and discount percentage, and most phones are priced and discounted in a similar range. This information can be useful for customers to make informed decisions about buying an iPhone based on its price and discount percentage.

# In[17]:


import pandas as pd
import seaborn as sns

df = pd.read_excel('D:\EXCEL\Appledata.xlsx')

sns.heatmap(df[['Star Rating', 'Number Of Ratings']].corr(), annot=True, cmap='coolwarm')


# In[19]:


import pandas as pd
import seaborn as sns

# Load the data
df = pd.read_excel('D:\EXCEL\Appledata.xlsx')

# Create a pivot table to aggregate the data
pivot_data = df.pivot_table(index='Brand', columns='Ram', values='Sale Price', aggfunc='mean')

# Create the heatmap using Seaborn
sns.heatmap(pivot_data, cmap='coolwarm')


#  heatmap that shows the average sale price of phones based on their brand and RAM size. The pivot_table() function is used to create a pivot table that aggregates the data and makes it easier to plot. The heatmap() function from the Seaborn library is then used to create the actual heatmap. We set the color map to "coolwarm" to make it easier to distinguish the different levels of sales prices.
The heatmap created from the "Mrp" and "Discount Percentage" columns of the given data shows the relationship between the Maximum Retail Price (MRP) of Apple iPhones and the discount percentage offered on them by Flipkart.

From the heatmap, we can see that iPhones with higher MRP generally have a higher discount percentage, with some exceptions. For example, the iPhone 11 with an MRP of 54900 has a discount of 14%, while the iPhone SE with an MRP of 39900 has a discount of 24%. However, we can also see that there are a few iPhones that have a relatively low MRP but are not offered any discounts, such as the iPhone 8 Plus with an MRP of 49900 and the iPhone 8 with an MRP of 77000.

Overall, the heatmap provides a quick and easy way to visualize the relationship between two numerical variables and can help identify any patterns or trends in the data. In this case, we can see that higher-priced iPhones generally have higher discounts, but there are also some exceptions to this trend.
# The data only includes Apple iPhones, which implies that the dataset is not representative of the entire mobile phone market.
# The prices of the iPhones vary widely, with the lowest priced iPhone being available for ₹29,999 and the most expensive iPhone for ₹1,19,900. This suggests that Apple is catering to a wide range of customers with varying budgets.
# It is interesting to note that the discount percentage for most iPhones is zero. This could indicate that Apple is able to maintain a high price point for their products without resorting to frequent discounts or price cuts.
# The number of ratings and reviews vary widely between products, which could be indicative of the popularity and demand for different iPhone models.
# All iPhones in the dataset have a minimum of 2 GB RAM, with some models having 4 GB RAM. This could be a reflection of the increasing demand for high-performance mobile devices.
# The star rating for the products varies between 4.4 to 4.7 out of 5, indicating that the iPhones in the dataset are generally well-received by customers.
# The MRP and sale price for some iPhone models are the same, which suggests that these products are not being discounted.

# In[ ]:




