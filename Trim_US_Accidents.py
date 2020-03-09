#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Import Required Packages
import pandas as pd
import numpy as np
import dask.dataframe as dd


# In[7]:


#Read in US Accident Data and extract concerned cities
US_Accidents="C:/Users/herre/OneDrive/Documents/GITHUB/IST718_GROUP_PROJECT/DATASETS/ACCIDENT DATA/US_Accidents.csv"
US = dd.read_csv(US_Accidents)

cityList=('Atlanta','Athens', 'Cumberland', 'Statham', 'Duluth', 'Norcross'
         , 'Peachtree Corners', 'Monroe', 'Suwanee', 'Johns Creek', 'Winder'
        , 'Dallas','Forth Worth', 'Arlington', 'Forest Hill'
         , 'Grand Prairie', 'Cedar Hills', 'Duncanville', 'Mansfield'
        , 'Houston','Miami','Sunrise', 'Fort Lauderdale', 'Dania Beach', 'Hollywood'
        , 'Oakland Park', 'Wilton Manors', 'North Andrews Barden', 'Launderhills'
         , 'Lauderdale Lakes', 'Plantation', 'Davie')
ATLlist=('Atlanta','Athens', 'Cumberland', 'Statham', 'Duluth', 'Norcross'
         , 'Peachtree Corners', 'Monroe', 'Suwanee', 'Johns Creek', 'Winder')
DALlist=('Dallas','Forth Worth', 'Arlington', 'Forest Hill'
         , 'Grand Prairie', 'Cedar Hills', 'Duncanville', 'Mansfield')
HOUlist=('Houston')
MIAlist=('Miami','Sunrise', 'Fort Lauderdale', 'Dania Beach', 'Hollywood'
        , 'Oakland Park', 'Wilton Manors', 'North Andrews Barden', 'Launderhills', 'Lauderdale Lakes', 'Plantation', 'Davie')
USCity=US[US['City'].isin(cityList)]
USdf=USCity.compute()


# In[18]:


#Trim data to 2017 and later
USdf1=USdf[USdf['Start_Time']>('2016-12-31 23:59:59')]


# In[19]:


#Drop Unneeded columns
USdf1=USdf1.drop(columns=['ID','Description','County','Country','Airport_Code','TMC','Source','Street','Timezone'
                          ,'Astronomical_Twilight','Civil_Twilight','Nautical_Twilight'])


# In[20]:


#Split data by city
ATL_Accidents=pd.DataFrame(USdf1[USdf1['City'].isin(ATLlist)])
ATL_Accidents=pd.DataFrame(ATL_Accidents[ATL_Accidents['State']=='GA'])
DAL_Accidents=pd.DataFrame(USdf1[USdf1['City'].isin(DALlist)])
DAL_Accidents=pd.DataFrame(DAL_Accidents[DAL_Accidents['State']=='TX'])
HOU_Accidents=pd.DataFrame(USdf1[USdf1['City']==(HOUlist)])
HOU_Accidents=pd.DataFrame(HOU_Accidents[HOU_Accidents['State']=='TX'])
MIA_Accidents=pd.DataFrame(USdf1[USdf1['City'].isin(MIAlist)])
MIA_Accidents=pd.DataFrame(MIA_Accidents[MIA_Accidents['State']=='FL'])


# In[21]:


pd.options.display.max_columns = 100
print(ATL_Accidents)
print(DAL_Accidents)
print(HOU_Accidents)
print(MIA_Accidents)


# In[22]:


ATL_Accidents.to_csv('ATL_Accidents.csv', index=False)
DAL_Accidents.to_csv('DAL_Accidents.csv', index=False)
HOU_Accidents.to_csv('HOU_Accidents.csv', index=False)
MIA_Accidents.to_csv('MIA_Accidents.csv', index=False)


# In[ ]:





# In[ ]:




