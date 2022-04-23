#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Define the function "say_hello" so it prints "Hello!" when called.
def sayHello():
    print('HELLO!')
sayHello()


# In[2]:


# Define the function "say_something" so it prints whatever is passed as the variable when called.
Jane_says = "Hi, my name is Jane. I'm learning Python!"
def saySomething(something):
    print(something)


# In[3]:


saySomething(Jane_says)


# In[4]:


def passingMathPercentage(passingMathCount, studentCount):
    return passingMathCount / float(studentCount) * 100


# In[5]:


passMathCount = 29370
totalStudentCount = 39170


# In[6]:


passingMathPercentage(passMathCount,totalStudentCount)


# In[7]:


# A list of my grades.
my_grades = ['B', 'C', 'B' , 'D']


# In[8]:


# Import pandas.
import pandas as pd
# Convert the my_grades to a Series
my_grades = pd.Series(my_grades)
my_grades


# In[9]:


# Change the grades by one letter grade.
my_grades.map({'B':'A','C':'B','D':'C'})


# In[10]:


# Using the format() function.
my_grades = [92.34, 84.56, 86.78, 98.32]

for grade in my_grades:
    print("{:.0f}".format(grade))


# In[11]:


# Convert the numerical grades to a Series.
my_grades = pd.Series([92.34, 84.56, 86.78, 78.32])
my_grades


# In[12]:


my_grades.map('{:.0f}'.format)

