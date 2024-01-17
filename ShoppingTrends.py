#!/usr/bin/env python
# coding: utf-8

# In[1]:


## import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


## load data set
ST = pd.read_csv('shopping_trends.csv')
ST


# In[3]:


##Review info for the csv
ST.info()


# In[4]:


##Count NaN values of whole DataFrame
ST.isnull().sum()


# In[5]:


ST.describe()


# In[6]:


plt.figure(figsize=(10,6))
A = ST['Gender'].value_counts()
bars = plt.bar(A.index, A.values, color='Blue')

plt.xlabel('Gender')
plt.ylabel('Total Number')
plt.title('Gender Distribution')

plt.show()


# In[7]:


##kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, analogous to a histogram
plt.figure(figsize=(10, 6))
plt.hist(ST['Age'],edgecolor = 'black',alpha=0.7,bins=25,color = 'skyblue',density=True) 
ST['Age'].plot(kind='kde', color = 'red')

plt.xlabel('Age')
plt.ylabel('Count / Density')
plt.title('Age Distribution with density curve')
plt.legend(['Density Curve', 'Histogram'])

plt.show()


# In[8]:


# Category
ST["Category"].value_counts()


# In[9]:


plt.figure(figsize=(10, 6))
c = ST['Category'].value_counts()
bar=plt.bar(c.index,c.values,color= 'gray')

plt.xlabel('Categories')
plt.ylabel('Total Number')
plt.title('Category Distribution')

plt.show()


# In[10]:


# Create a count plot to visualize the relationship
plt.figure(figsize=(10, 6))
sns.countplot(data=ST, x='Category', hue='Gender',palette='dark')
plt.title('Product Category by Gender')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.legend(title='Gender', labels=ST['Gender'].unique())

# Show the plot
plt.show()


# In[21]:


# Create a count plot to visualize the relationship
plt.figure(figsize=(20, 8))
sns.countplot(data=ST, x='Item Purchased', hue='Gender',palette='dark')
plt.title('Product Category by Gender')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.legend(title='Gender', labels=ST['Gender'].unique())

# Show the plot
plt.show()


# In[22]:


plt.figure(figsize=(15,5))
sns.countplot(data=ST,x='Category' ,hue='Size')
plt.title('Category distribution by Gender')
plt.show()


# In[24]:


plt.figure(figsize=(20,5))
sns.countplot(data=ST,x='Item Purchased' ,hue='Size')
plt.title('Category distribution by Gender')
plt.show()


# In[25]:


plt.figure(figsize=(10,4))
sns.countplot(data=ST,x='Category',hue='Season')


# In[30]:


count=ST['Subscription Status'].value_counts()
count.plot(kind='pie', explode=(0,0.1),autopct='%1.1f%%')
plt.title('Subscription Status distribution')
plt.show()


# In[34]:


plt.figure(figsize=(10, 6))
c=ST['Shipping Type'].value_counts()
bar=plt.bar(c.index,c.values)

plt.xlabel('Shipping Type')
plt.ylabel('Total Number')
plt.title('Shipping type Distribution')


# In[39]:


plt.figure(figsize=(8,6))
sns.countplot(data=ST,x='Category',hue='Promo Code Used')


# In[43]:


#Average age of the customer
average_age = ST['Age'].mean()
print("Average Age:", average_age)


# In[42]:


#Total purchase amount for each category 

TotalPur = ST.groupby('Category')['Purchase Amount (USD)'].sum()
print("Total purchases for each category:", TotalPur)


# In[45]:


#The most common payment method used by customers 
most_common_payment_method = ST['Payment Method'].mode()[0]
print("Most Common Payment Method:", most_common_payment_method)


# In[47]:


# How many customers have opted for the Subscription 
subscription_count = ST[ST['Subscription Status'] == 'Yes']['Customer ID'].count()
print("Number of Customers with Subscription: ", subscription_count)


# In[49]:


# What is the most common season for purchases?
most_common_season = ST['Season'].mode()[0]
print("Most Common Season for Purchases:", most_common_season)


# In[51]:


#How many customers used a promo code for their purchase
promo_code_count = ST[ST['Promo Code Used'] == 'Yes']['Customer ID'].count()
print("Number of Customers who used Promo Code:", promo_code_count)


# In[52]:


#What is the maximum and minimum review rating in the dataset?
max_review_rating = ST['Review Rating'].max()
min_review_rating = ST['Review Rating'].min()
print("Maximum Review Rating:", max_review_rating)
print("Minimum Review Rating:", min_review_rating)


# In[53]:


# What is the most common shipping type for customers with a review rating above 4 ?
common_shipping_high_rating = ST[ST['Review Rating'] > 4]['Shipping Type'].mode()[0]
print("Most Common Shipping Type for High Review Ratings:", common_shipping_high_rating)


# In[54]:


#How many customers have made more than 30 previous purchases ?
customers_above_30_previous_purchases = ST[ST['Previous Purchases'] > 30]['Customer ID'].count()
print("Number of Customers with more than 30 Previous Purchases:", customers_above_30_previous_purchases)

