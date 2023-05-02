#!/usr/bin/env python
# coding: utf-8

# In[14]:



import numpy as np
import pandas as pd

pd.Series([10,2,5])


# In[17]:


vector = np.array([5,4,3])
pd.Series(vector)


# In[11]:


import pandas as pd

data = [[1, 'a'], [2, 'b'], [3, 'c']]
df = pd.DataFrame(data)
print(df)


# In[12]:


import numpy as np
import pandas as pd

data = np.array([[1, 'a'], [2, 'b'], [3, 'c']])
df = pd.DataFrame(data)
print(df)


# In[13]:


import pandas as pd

data = [[1, 'a'], [2, 'b'], [3, 'c']]
columns = ['num', 'letter']
df = pd.DataFrame(data, columns=columns)
print(df)


# In[18]:


import pandas as pd

df = pd.read_csv('titanic.csv')
print(df.head())


# In[19]:


selected_columns = df[["Survived", "Pclass", "Age", "Sex"]]
print(selected_columns)


# In[20]:


selected_rows = df.loc[200:400, ["Name", "Age"]]
print(selected_rows)


# In[21]:


df.rename(columns={"PassengerId": "ID"}, inplace=True)
print(df.head())


# In[22]:


selected_data = df.loc[(df["Sex"] == "female") & (df["Pclass"] == 1)]
print(selected_data)


# In[23]:


selected_data = df.loc[(df["Sex"] == "male") & (df["Pclass"] == 2) & (df["Age"] < 18)]
print(selected_data)


# In[24]:


mean_age_by_sex = df.groupby("Sex")["Age"].mean()
print(mean_age_by_sex)


# In[25]:


survivors_by_sex = df.groupby("Sex")["Survived"].sum()
print(survivors_by_sex)


# In[ ]:




