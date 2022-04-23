#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


studentDataPath = "Resources/students_complete.csv"

studentData = pd.read_csv(studentDataPath)
studentData.head()


# In[4]:


studentNames = studentData["student_name"].tolist()
studentNames


# In[5]:


# Split the student name and determine the length of the split name.
for name in studentNames:
    print(name.split(),len(name.split()))


# In[6]:


# Create a new list and use it for the for loop to iterate through the list.
studentsToFix = []

# Use an if statement to check the length of the name.
# If the name is greater than or equal to "3", add the name to the list.
for name in studentNames:
    if len(name.split()) >= 3:
        studentsToFix.append(name)
        
# Get the length of the students whose names are greater than or equal to "3".
len(studentsToFix)


# In[7]:


# Add the prefixes less than or equal to 4 to a new list.
prefixes = []
for name in studentsToFix:
    if len(name.split()[0]) <= 4:
        prefixes.append(name.split()[0])
set(prefixes)


# In[8]:


#getting suffix possabilities
suffixes = []

for names in studentsToFix:
    if len(names.split()[-1]) <= 3:
        suffixes.append(names.split()[-1])
set(suffixes)


# In[9]:


for name in studentsToFix:
    print(name.replace("Dr.", ""))


# In[10]:


prefix_suffix = [' DDS',' DVM', "MD",
' PhD','Dr. ','Miss ','Mrs. ','Ms. ','Mr. ']

for word in prefix_suffix:
    studentData["student_name"] = studentData["student_name"].str.replace(word,"",regex=False)
studentData.head(10)


# In[11]:


checkLength = studentData['student_name'].tolist()
checkLength


# In[12]:


students_fixed = []

for name in checkLength:
    if len(name.split()) >= 3:
        students_fixed.append(name)
len(students_fixed)


# In[ ]:




