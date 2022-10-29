#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: Investigate a Dataset ( Tmdb Movies)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# This dataset contains information about 10000 movies collected from The Movies Database(TMDB).
# 
# The dataset also contains information about the movies grouped in 21 columns, i also deleted irrelevant 
# 
# columns in the course of data cleaning.
# 
# In the course of exploration i intend to answer question such as:
# 
# 1. which genres are most popularfrom year to year?
# 
# 2. What kinds of properties are associated with movies that have high revenue?
# 
# 
# 

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns




df_movies = pd.read_csv('tmdb-movies.csv')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# In the data wrangling process. i took the following steps:
# 
# 1. checked for null values and removed columns with null values
# 2. checked for dublicates and removed dublicate rows
# 3. removed irrelevant columns
# 4. split and exploded the genres columns
# 
# ### General Properties

# In[2]:


df_movies.head(1)


# In[3]:


#getting information about the project

df_movies.info(), df_movies.shape


# In[4]:


#checking for missing values in table rows


df_movies.isnull().sum()


# 
# 
# ### Data Cleaning
# 
# steps taken to clean the data
# 1. I checked for  and  dropped columns with null values
# 2. I checked for and dropped columns with dublicate rows
# 3. I also dropped irrelevant columns
# 4. I also split and exploded the genres columns 
# 

# In[12]:


#dropping rows with empty data

df_movies.dropna(inplace = True)


# In[6]:


#check if rows with empty data still exist
df_movies.isnull().sum()


# In[10]:


#check for table dublicates 
sum(df_movies.duplicated())


# In[14]:


# dropping irrelevant columns
df_movies.drop(['id','imdb_id','homepage'], axis = 1, inplace=True)


# In[15]:


#check if irrelevant tables have been dropped
df_movies.head(2)


# In[16]:


#checking for unique values in the genres column

df_movies['genres'].value_counts()


# In[17]:


#checking to see what my genres look like 
df_movies.head(1)


# In[18]:


#reassigning df_movies to clean_df so that df_movies remains safe
clean_df = df_movies


# In[19]:


#checking what the genres column looks like
clean_df.head(1)


# In[20]:


#convert genre column to a list and then exploding the list so  they can be in seperate lists
#assign result to df_genre

def split_column_genres():
    return clean_df.assign(genres =clean_df['genres'].str.split('|')).explode('genres')
    

df_genre = split_column_genres()


# In[21]:


#checking if changed have been made sucessfully

df_genre.head(2)


# In[ ]:





# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# 
# ### Which genres are most popular from year to year?

# #### first we need to find the mean popularity for each movie genre

# In[22]:


df_genre.describe()


# In[25]:


#find the mean popularity for each movie genre

df_popular = df_genre.groupby('genres').mean().popularity


# In[35]:


df_popular


# In[27]:


df_popular.index


# In[34]:


fig = plt.figure()
ax = fig.add_axes([0,0,2.5,2.5])
ax.bar(df_popular.index,df_popular)
plt.show()


# 

# ## Findings
# 
# 1. The barchart above shows that adventure movies are more popular.
# 2. The science fiction is second.

# In[ ]:





# ### What kinds of properties are associated with movies that have high revenue?

# In[39]:


#structure of dataset
df_genre.describe()


# In[40]:


#get mean revenue generated

df_genre.revenue.mean()


# In[45]:


# select samples of movies tha generated revenue above mean revenue

high_revenue_movies = df_genre.query(f'revenue >= {df_genre.revenue.mean()}')


# In[48]:


high_revenue_movies.describe()


# In[60]:


h_revenue_df = high_revenue_movies.genres.value_counts()


# In[62]:


h_revenue_df.index


# In[63]:


fig = plt.figure()
ax = fig.add_axes([0,0,2.5,2.5])
ax.bar(h_revenue_df.index,h_revenue_df)
plt.show()


# #### more drama  movies generated more revenue

# In[49]:


high_revenue_movies.plot(x="budget", y="genres", kind="scatter");


# In[50]:


high_revenue_movies.plot(x="popularity", y="genres", kind="scatter");


# In[51]:


high_revenue_movies.plot(x="vote_count", y="genres", kind="scatter");


# In[52]:


high_revenue_movies.plot(x="runtime", y="genres", kind="scatter");


# ### findings
# 1. properties such as vote count, popularity and budget have  strong effect on the revenue generated
# 2. the effect of the runtime is not that strong on the revenue generated
# 3. budget and vote count have the strongest effect

# <a id='conclusions'></a>
# ## Conclusions
# 
# 1. the adventure movies are most popular from year to year
# 2. the budget and vote count have the strongest effects on the revenue generated from the movie project
# 
# ### limitations
# 1. not enough test sample

# In[ ]:




