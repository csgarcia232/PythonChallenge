#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv


# In[2]:


budgetdata_df = "Resources/budget_data.csv"
budgetdata_df= pd.read_csv(budgetdata_df)
budgetdata_df.head()


# In[3]:


total_months_test = budgetdata_df["Date"].sum()
total_months_test


# In[4]:


budgetdata_df.dtypes


# In[5]:


total_months = budgetdata_df["Date"].count()
total_months


# In[6]:


profit_lossesdf = budgetdata_df["Profit/Losses"].describe()
profit_lossesdf


# In[7]:


profit_lossesdf = profit_lossesdf.map("${:.2f}".format)
profit_lossesdf


# In[8]:


total = budgetdata_df["Profit/Losses"].sum()
total


# In[9]:


average = budgetdata_df["Profit/Losses"].mean()
average


# In[10]:


greatest_increase = budgetdata_df["Profit/Losses"].max()
greatest_increase


# In[11]:


greatest_decrease =  budgetdata_df["Profit/Losses"].min()
greatest_decrease


# In[12]:


print("Financial Analysis")
print("------------------")
print("Total Months: 86")
print("Total: $38,382,578")
print("Average: $446,309.05")
print("Greatest Increase in Profits: $1,170,593")
print("Greatest Decrease in Profits: $1,196,225")


# In[13]:


# So I didn't calculate the 'Average Change', I couldn't find the code to do so. I'm sure I just overlooked it, but I couldn't remember if we'd gone over that or not. 
# I also couldn't figure out how to incorporate the numbers I found through the 
# functions into the print out I made at the bottom, so I just typed it out.
# I am sure this is not ideal in real life. I did everything with Pandas because it
# made more sense to me. Ethan stated this was okay. 


# In[ ]:





# In[ ]:




