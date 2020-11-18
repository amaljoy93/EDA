#!/usr/bin/env python
# coding: utf-8

# # pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language
# Pandas - Panel Data
# Datatypes in Pandas
# Series
# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index.
# 
# Dataframe
# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.
# 
# Panel
# A panel is a 3D container of data
# 
# To install
# pip install pandas

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


get_ipython().run_line_magic('pinfo', 'pd')


# In[4]:


s=pd.Series([10,30,50,np.nan,60,89])#here we are creating a Series using a list


# In[5]:


s


# In[6]:


type(s)


# In[6]:


s.shape #shape will show the shape(#rows and # columns) - For series #columns will be always 1.


# In[7]:


s.head() #head used to display the first n number of observations default n = 5


# In[8]:


s.tail() #tail used to display the last n number of observations default n = 5


# In[12]:


s.dtypes #dtypes used to identify the datatype of the series/dataframe


# In[9]:


s1 = pd.Series([9, 12, 15, 18, 21, 24])


# In[11]:


s1.add(1)


# In[13]:


s1.subtract(1)


# In[14]:


s1.mean()


# In[16]:


s1.median()


# In[19]:


s.mode()[0]


# In[20]:


arr=np.arange(10,20,2)
s2=pd.Series(arr)#creating a Series from numpy array


# In[21]:


s2


# In[22]:


s2.dtypes


# # Dataframe 

# In[24]:


df=pd.read_csv("C://Users/Amil/Downloads/supermarket_sales.csv") # read_csv is used to read a csv file and create a DataFrame


# In[26]:


type(df)


# In[16]:


df.shape


# In[25]:


df.head()


# In[26]:


df.tail(20)


# In[27]:


df.columns #columns will display all the column names


# In[28]:


df.index #index will display the index of rows


# In[25]:


df.dtypes


# In[29]:


df.size


# In[89]:


df.shape[0]*df.shape[1]


# In[30]:


df.describe()#describe function will give us the summary of dataframe (only numerical features)


# In[31]:


df.describe(include='O')#Summary of Object columns


# In[36]:


# checking for missing values information
df.isna().sum()#is not available function
# Theres is no missing value in the present data set


# In[38]:


s=pd.read_csv("C://Users/Amil/Downloads/pqrs.csv")


# In[41]:


s.isna().sum()


# # creating data frame

# In[109]:


#1 Loading existing data
#2 create a DataFrame Programatically

df=pd.DataFrame([["Amal",10],["Babu",11],["Cat",12],["Don",13]],columns=['Name','Age'])


# In[110]:


df.shape


# In[111]:


df.tail()


# In[112]:


df.head()


# In[113]:


df.describe()


# In[114]:


df['Gender']=['M','M','M','F']


# In[104]:



df


# #  Access Data from DataFrame

# In[115]:


# to access a column
df['Name']


# In[116]:


df[['Name','Age']]


# In[117]:


#to acess row we need to specify the row index.
#loc means location -we are specifying the location by index.

df.loc[[0,1,2]]


# In[118]:


df.loc[0]


# In[119]:


df.loc[0:4]


# In[120]:


df.index=df['Name']


# In[121]:


df


# In[122]:


df.loc['Amal']


# In[95]:


df


# In[123]:


df.loc[['Amal','Babu','Cat']] #in loc function we are providing the actual index.


# In[65]:


# iloc fuction accept range index ie (0,1,2,4///)


# In[124]:


df.iloc[range(0,df.shape[0])]


# In[126]:


#To access a cell using loc
df.loc['Amal','Age']=27


# In[127]:


df.iloc[0,1]


# In[128]:


df


# In[129]:


# duplicatr index
# loading existing data
# crate a DataFrame Programtically
df1=pd.DataFrame([["A",20],["B",21],["C",22],["A",23]],columns=['Name','Age'])
df1


# In[130]:


df1.index=df1['Name']


# In[131]:


df1['Age']


# In[132]:


df1.iloc[:,1]


# In[133]:


df1.loc['B','Age']


# In[134]:


df.iloc[:,:]


# In[113]:


df.iloc[:,1]


# In[92]:


df.iloc[1,1]


# # Delete rows and columns from DataFrame

# In[136]:


# for deleting rows and columns we use function called 'drop'
# we have to specift the axis
# Axis=0 for rows
# Axis=1 for columns
df1=df1.drop('A')


# In[138]:


df1


# In[139]:


df


# In[141]:


df=df.drop('Gender',axis=1)


# In[142]:


df


# In[143]:


del df['Age']#del command is an alternative to delete columns


# In[144]:


df


# In[4]:


df=pd.read_csv("C://Users/Amil/Downloads/supermarket_sales.csv")


# In[5]:


df.head()


# In[103]:


df.describe()


# In[9]:


# what is tge total gross income?
total_income=df['gross income'].sum()
print("total gross income=",total_income)


# In[119]:


df.iloc[:,15].sum()


# In[13]:



list(df['Payment'].unique())


# In[14]:


# which is the most commonly used payment type

df['Payment'].describe()


# In[15]:


#  what is the average unit price of the products¶
df['Unit price'].mean()


# In[17]:


df.iloc[:,6].mean()


# In[18]:


# what is the total number of sales
df['Invoice ID'].unique()


# In[130]:


df['Invoice ID'].describe()


# In[22]:


sales=df.describe(include='O').loc['unique','Invoice ID']
print("Total number of sales:",sales)


# In[19]:


#  what is the average gross income
df['gross income'].mean()


# In[20]:


# what is the standard deviation of product unit price
df['Unit price'].std()


# In[24]:


# unique and nunique
# what are the different types of Product line
df['Product line'].unique()


# In[26]:


# How many customer classes are there
df['Product line'].nunique()


# In[115]:


s=pd.read_csv("C://Users/Amil/Downloads/adult.csv")


# In[34]:


s.describe(include='O')


# In[29]:


s.head()


# In[32]:


s.shape


# In[33]:


s.columns


# In[35]:


s.head()


# In[36]:


s.isna().sum()


# In[37]:


s['occupation'].unique()


# In[38]:


s['occupation'].nunique()


# In[39]:


s.dtypes


# # can you calculate average hours per week
# c

# In[40]:


s.describe()


# In[43]:


s['hours-per-week'].mean()


# # can you calculate average hours per male
# 

# In[44]:


# when we use grope by it will create data frame into groups in this example it will group into a data frame that consist only of male and other data frame consist of female


# In[46]:


k=s.groupby('gender')


# In[47]:


print(k)


# In[49]:


k['hours-per-week'].mean()


# In[51]:


s['race'].unique()


# In[54]:


s.groupby('race')['hours-per-week'].mean()


# In[65]:


output_df=s.groupby(['race','gender'])[['age','hours-per-week']].median()


# In[66]:


print(output_df)


# In[78]:


output_df1=s.groupby(['race','gender']).median()[['age','hours-per-week']]


# In[68]:


print(output_df1)


# In[72]:


# work class and gender hours per week
s.groupby(['workclass','gender'])['age','hours-per-week'].mean()


# In[75]:


output_df3=s.groupby(['workclass','gender']).median()['hours-per-week']


# In[76]:


print(output_df3)


# In[109]:


output_df3


# # we can create csv file and store our result using following code

# In[113]:


output_df3.to_csv('C://Users/Amil/Downloads/class18mmresults.csv')
# saving as a csv file


# In[114]:


output_df3.to_excel('C://Users/Amil/Downloads/class18mmresults.xlsx')
# saving as a csv file


# # value counts 
# value counts() function used to calculate the distrbution

# In[116]:


s['workclass'].value_counts()


# In[118]:


s['gender'].value_counts()


# # combaining 2 dataframes
# 

# In[135]:


dataframe1=pd.DataFrame([[1,25,'F'],[2,26,'M'],[3,27,'F'],[4,28,'F'],[7,29,'M'],[89,30,'F'],[390,31,'F']],columns=['ID','Age','Gender'])


# In[128]:


print(dataframe1)


# In[136]:


dataframe2=pd.DataFrame([[1,'A'],[2,'B'],[3,'C'],[29,'D'],[7,'E'],[39,'F'],[38,'G']],columns=['ID','Name'])


# In[137]:


print(dataframe2)


# # Merge is the funtion used for SQL joins in Pandas

# In[138]:


inner_join=pd.merge(dataframe1,dataframe2,how="inner",on="ID")
# dataframe1 is left table

#  dataframe2 is the right table


# In[139]:


print(dataframe1)
print(dataframe2)
print(inner_join)


# In[141]:


left_join=pd.merge(dataframe1,dataframe2,how="left",on="ID")
print(left_join)


# In[142]:


right_join=pd.merge(dataframe1,dataframe2,how="right",on="ID")
print(right_join)


# In[143]:


outer_join=pd.merge(dataframe1,dataframe2,how="outer",on="ID")
print(outer_join)


# In[ ]:




