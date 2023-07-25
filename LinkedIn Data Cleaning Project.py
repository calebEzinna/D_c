#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('linkdin_Job_data.csv')
df = pd.DataFrame(data)
print(df.head())


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


print(df.shape)


# In[6]:


df.drop(['company_id', 'alumni', 'Hiring_person', 'linkedin_followers', 'Column1', 'hiring_person_link', 'job_details'], axis=1, inplace=True)
print(df)


# In[7]:


df.fillna({"no_of_employ" : df['no_of_employ'].mode()[0]}, inplace = True)
print(df.head)


# In[8]:


df['no_of_employees'] = df['no_of_employ'].str.split(' ').str[0]
print(df)


# In[9]:


df.drop(['no_of_employ'], axis=1, inplace = True)
print(df)


# In[10]:


df.fillna(method = 'ffill', inplace =True)
df.fillna(method = 'bfill', inplace =True)
print(df)


# In[11]:


df.isna().sum()


# In[12]:


print(df.head())


# In[13]:


pd.unique(df['full_time_remote'])


# In[14]:


df['full_time_remote'] = df['full_time_remote'].replace(['1-10 employees','11-50 employees'],['Executive','Director'])
df


# In[15]:


df['job'] = df['job'].str.split(',').str[0]
df


# In[16]:


df.isnull().sum()


# In[17]:


df.rename(columns = {'full_time_remote': 'employment_type'}, inplace = True)
df


# In[ ]:




