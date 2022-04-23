#!/usr/bin/env python
# coding: utf-8

# In[3]:


# List of high schools
high_schools = ["Hernandez High School", "Figueroa High School",
                "Wilson High School","Wright High School"]


# In[4]:


for schools in high_schools:
    print(schools)


# In[5]:


# A dictionary of high schools and the type of school.
high_school_types = [{"High School": "Griffin", "Type":"District"},
                    {"High School": "Figueroa", "Type": "District"},
                    {"High School": "Wilson", "Type": "Charter"},
                    {"High School": "Wright", "Type": "Charter"}]
for schools in high_school_types:
    print(schools)


# In[6]:


# List of high schools
high_schools = ["Huang High School",  "Figueroa High School", "Shelton High School", "Hernandez High School","Griffin High School","Wilson High School", "Cabrera High School", "Bailey High School", "Holden High School", "Pena High School", "Wright High School","Rodriguez High School", "Johnson High School", "Ford High School", "Thomas High School"]


# In[7]:


import pandas as pd


# In[8]:


# Create a Pandas Series from a list.
school_series = pd.Series(high_schools)
school_series


# In[9]:


# A dictionary of high schools
high_school_dicts = [{"School ID": 0, "school_name": "Huang High    School", "type": "District"},
                   {"School ID": 1, "school_name": "Figueroa High School", "type": "District"},
                    {"School ID": 2, "school_name":"Shelton High School", "type": "Charter"},
                    {"School ID": 3, "school_name":"Hernandez High School", "type": "District"},
                    {"School ID": 4, "school_name":"Griffin High School", "type": "Charter"}]


# In[10]:


schools_df = pd.DataFrame(high_school_dicts)
schools_df


# In[11]:


# Three separate lists of information on high schools
school_id = [0, 1, 2, 3, 4]

school_name = ["Huang High School", "Figueroa High School",
"Shelton High School", "Hernandez High School","Griffin High School"]

type_of_school = ["District", "District", "Charter", "District","Charter"]


# In[12]:


#Initialize a new DataFrame
schools_df = pd.DataFrame()


# In[13]:


schools_df["School ID"] = school_id
schools_df["school_name"] = school_name
schools_df["type"] = type_of_school
schools_df


# In[14]:


schools_df.columns


# In[15]:


# Create a dictionary of information on high schools.
high_schools_dict = {'School ID': school_id, 'school_name':school_name, 'type':type_of_school}


# In[16]:


schoolsDf = pd.DataFrame(high_school_dicts)


# In[17]:


schoolsDf


# In[19]:


schoolsDf.columns


# In[21]:


schoolsDf.index


# In[20]:


schoolsDf.values

