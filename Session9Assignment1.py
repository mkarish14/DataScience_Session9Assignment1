
# coding: utf-8

# In[2]:


import pandas as pd

df= pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
df.head()


# In[8]:


df.drop(df.columns[df.columns.str.contains('Unnamed',case = False)],axis = 1,inplace=True)
df.head()


# In[9]:


#df['Gender'].describe()
df.groupby('Gender').describe()


# In[1]:


df['Name'].head(5)


# In[12]:


df['Name'].value_counts().head(5)


# In[29]:


import pandas as pd

df= pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
df.head()
df.groupby(['State', 'Gender'])['Count'].count()


# In[25]:


#df.groupby(['State', 'Gender'])['Count'].sum()
df[[df.columns.str.contains('State',case = False)]]

