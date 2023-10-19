#!/usr/bin/env python
# coding: utf-8

# In[28]:


from selenium import webdriver
import pandas as pd


# In[63]:


ataa = webdriver.Chrome()


# In[64]:


#request to my driver
ataa.get("https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW")


# In[65]:


#scrap titles and released year together
My_movies = ataa.find_elements("xpath",'//a[@class="a-link-normal"]')
#scrap the profit
gross = ataa.find_elements("xpath",'//td[@class="a-text-right mojo-field-type-money"]')


# In[76]:


#select my text only and append it into lists
Movies = []
my_gross = []
for element in My_movies:
    Movies.append(element.text)
for money in gross:
    my_gross.append(money.text)
print(len(Movies), len(my_gross))


# In[80]:


#slice movies to clean my selected data
Movies = Movies[1:401]
#extract names and years from Movies by slicing with Appropriate steps
titles = Movies[::2]
years = Movies[1::2]
print(len(Movies),len(years), len(titles))


# In[79]:


#convert to data frame 
data = {"title": titles,"years":years ,"Lifetime Gross": my_gross}
df = pd.DataFrame(data)
#save to csv file
df.to_csv("D:\ITI\Data Engineering\Data Exploration and preparation\day 1\lab\Top200Movies.csv", index = False)
df


# In[ ]:





# In[ ]:




