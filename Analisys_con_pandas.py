#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("delitos2019.csv")


# In[2]:


df.info()


# In[3]:


total_delitos = df['id'].count()
print("Total de delitos denunciados en 2019:", total_delitos)


# In[4]:


top_barrios_mas_delitos = df['barrio'].value_counts().head(5)
print("Top 5 de barrios con más delitos:")
print(top_barrios_mas_delitos)


# In[5]:


top_barrios_menos_delitos = df['barrio'].value_counts().tail(5)
print("Top 5 de barrios con menos delitos:")
print(top_barrios_menos_delitos)


# In[8]:


horarios_delitos = df['franja_horaria'].value_counts().sort_values(ascending=False)
print("Horario (franja horaria) ordenado de forma descendente desde el peor horario al menos problemático:")
print(horarios_delitos)


# In[7]:


print(df.columns)


# In[ ]:




