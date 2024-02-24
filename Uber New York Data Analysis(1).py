#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install pandas


# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


import os 


# In[4]:


os.listdir(r"C:\Users\User\Downloads\Projects\Project 1\Datasets")


# In[6]:


uber_15 = pd.read_csv(r"C:\Users\User\Downloads\Projects\Project 1\Datasets/uber-raw-data-janjune-15_sample.csv")


# In[10]:


uber_15.shape


# In[11]:


type(uber_15)


# In[71]:


uber_15.drop_duplicates(inplace=True)


# In[69]:


uber_15.duplicated().sum()


# In[72]:


uber_15.shape


# In[73]:


uber_15.dtypes


# In[23]:


uber_15.isnull().sum()


# In[24]:


uber_15['Pickup_date'][0]


# In[25]:


type(uber_15['Pickup_date'][0])


# In[29]:


uber_15['Pickup_date'] = pd.to_datetime(uber_15['Pickup_date'])


# In[30]:


uber_15['Pickup_date'].dtype


# In[32]:


uber_15.dtypes


# In[33]:


uber_15


# In[35]:


uber_15['Pickup_date'].dt.month_name()


# In[39]:


uber_15['month'] = uber_15['Pickup_date'].dt.month_name()


# In[40]:


uber_15['month'] 


# In[43]:


uber_15['month'] .value_counts().plot(kind='bar')


# In[51]:


uber_15['weekday'] = uber_15['Pickup_date'].dt.day_name()
uber_15['day'] = uber_15['Pickup_date'].dt.day
uber_15['hour']= uber_15['Pickup_date'].dt.hour
uber_15['minute'] = uber_15['Pickup_date'].dt.minute


# In[52]:


uber_15.head(4)


# In[76]:


pivot = pd.crosstab( index=uber_15['month'], columns= uber_15['weekday'])


# In[77]:


pivot


# In[79]:


pivot.plot(kind='bar' , figsize =(8,6))


# In[84]:


summary = uber_15.groupby(['weekday','hour'] , as_index=False).size()


# In[85]:


summary


# In[87]:


plt.figure(figsize=(8,6))
sns.pointplot(x="hour", y="size", hue="weekday", data=summary)


# In[14]:


uber_15.columns


# In[7]:


os.listdir(r"C:\Users\User\Downloads\Projects\Project 1\Datasets")


# In[15]:


uber_foil = pd.read_csv(r"C:\Users\User\Downloads\Projects\Project 1\Datasets/Uber-Jan-Feb-FOIL.csv")


# In[16]:


uber_foil.shape


# In[96]:


uber_foil.head(3)


# In[17]:


get_ipython().system('pip install chart_studio')
get_ipython().system('pip install plotly')


# In[18]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px

from plotly.offline import download_plotlyjs , init_notebook_mode , plot , iplot


# In[102]:


init_notebook_mode(connected=True)


# In[104]:


uber_foil.columns


# In[19]:


px.box(x='dispatching_base_number' , y='active_vehicles' , data_frame=uber_foil)


# In[20]:


px.violin(x='dispatching_base_number' , y='active_vehicles' , data_frame=uber_foil)


# In[21]:


files = os.listdir(r"C:\Users\User\Downloads\Projects\Project 1\Datasets")[-8:]


# In[22]:


files.remove('uber-raw-data-janjune-15.csv')


# In[113]:


files


# In[114]:


files.remove('uber-raw-data-janjune-15_sample.csv')


# In[115]:


files


# In[33]:


final = pd.DataFrame()

path = r"C:\Users\User\Downloads\Projects\Project 1\Datasets"
for file in files :
    current_df = pd.read_csv(path+'/'+file)
    final = pd.concat([current_df , final])


# In[34]:


final.shape


# In[35]:


final.duplicated().sum()


# In[36]:


final.drop_duplicates(inplace=True)


# In[37]:


final.shape


# In[123]:


final.head(3)


# In[38]:


rush_uber = final.groupby(['Lat','Lon'] , as_index=False).size()


# In[39]:


rush_uber.head(6)


# In[40]:


get_ipython().system('pip install folium')


# In[41]:


import folium


# In[42]:


folium.Map()


# In[43]:


basemap = folium.Map()


# In[77]:


from folium.plugins import HeatMap


# In[ ]:





# In[76]:


HeatMap(rush_uber).add_to(basemap)


# In[ ]:





# In[75]:


basemap


# In[48]:


final.columns


# In[49]:


final.head(3)


# In[50]:


final.dtypes


# In[51]:


final['Date/Time'][0]


# In[52]:


pd.to_datetime(final['Date/Time'], format ="%m/%d/%Y %H:%M:%S")


# In[53]:


final['Date/Time'] = pd.to_datetime(final['Date/Time'], format ="%m/%d/%Y %H:%M:%S")


# In[54]:


final['Date/Time']


# In[64]:


final['Date/Time'].dtype


# In[55]:


final['day'] = final['Date/Time'].dt.day
final['hour'] = final['Date/Time'].dt.hour


# In[56]:


final.head(4)


# In[65]:


pivot = final.groupby(['day','hour']).size().unstack()


# In[58]:


pivot


# In[61]:


pivot.style.background_gradient()


# In[60]:


def gen_pivot_table(df, col1, col2):
    pivot = final.groupby([col1,col2]).size().unstack()
    return pivot.style.background_gradient()


# In[62]:


final.columns


# In[63]:


gen_pivot_table(final , "day" , "hour")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




