#!/usr/bin/env python
# coding: utf-8

# In[858]:


# Importing dependencies
import pandas as pd
import numpy as np
# Loading .CSV resource files
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Reading the .CSV files and assign the DataFrame to a variable
school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)

# Cleaning Student Names by removing certain suffixes and prefixes
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

# Iterates through the words in the "prefixes_suffixes" list, looking for occurrences of
# that string appearing in the "student name" column of the 'student_data_df' DataFrame.
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

# Checking names.
student_data_df.head(10)


# ## Deliverable 1: Replace the reading and math scores.
# 
# ### Replace the 9th grade reading and math scores at Thomas High School with NaN.

# In[859]:


# Importing numpy as np.
import numpy as np

# Seeing what data types are used.
student_data_df.dtypes


# In[860]:


# Using the loc method on the student_data_df to select all the reading scores from the 9th grade at Thomas High School and replace them with NaN.
student_data_df.loc[(student_data_df['grade'] == '9th') & (student_data_df['school_name'] == 'Thomas High School'),['reading_score']] = np.nan
student_data_df



# In[861]:


# Using the loc method on the student_data_df to select all the math scores from the 9th grade at Thomas High School and replace them with NaN.
student_data_df.loc[(student_data_df['grade'] == '9th') & (student_data_df['school_name'] == 'Thomas High School'),['math_score']] = np.nan
student_data_df


# In[862]:


# Checks to see all 9th graders at Thomas High Schools grades have been changed to 'NaN'
student_data_df.loc[(student_data_df['grade'] == '9th') & (student_data_df['school_name'] == 'Thomas High School'),['math_score','reading_score']].isnull()


# In[863]:


# Checking to see 'NaN's have been placed
student_data_df.tail(10)


# ## Deliverable 2 : Repeat the school district analysis

# ### District Summary

# In[864]:


# Combining the data into a single dataset
school_data_complete_df = pd.merge(student_data_df, school_data_df, how="left", on=["school_name", "school_name"])
school_data_complete_df.head()


# In[865]:


# Calculates the Totals (Schools and Students)
school_count = len(school_data_complete_df["school_name"].unique())
student_count = school_data_complete_df["Student ID"].count()

# Calculates the Total Budget
total_budget = school_data_df["budget"].sum()


# In[866]:


# Calculates the Average Scores using the "clean_student_data".
average_reading_score = school_data_complete_df["reading_score"].mean()
average_math_score = school_data_complete_df["math_score"].mean()


# In[867]:


# Getting the number of students that are in ninth grade at Thomas High School.
# These students have no grades. 
ThomasHsStudentCount = student_data_df.loc[(student_data_df['grade'] == '9th') & (student_data_df['school_name'] == 'Thomas High School'),['school_name']].count()

# Getting the total student count
student_count = school_data_complete_df["Student ID"].count()


# Getting new student count by subtracting the Thomas HS 9th grader count
newStudentCount = student_count - ThomasHsStudentCount

#newStudentCount


# In[868]:


# Calculates the passing rates using the "clean_student_data".
passing_math_count = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)].count()["student_name"]
passing_reading_count = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)].count()["student_name"]


# In[869]:


# Calculates the passing percentages with the new total student count.
passing_math_percentage = (passing_math_count / newStudentCount) * 100
passing_reading_percentage = (passing_reading_count / newStudentCount) * 100


# In[870]:


# Calculates the students who passed both reading and math.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)
                                               & (school_data_complete_df["reading_score"] >= 70)]

# Calculates the number of students that passed both reading and math.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()


# Calculates the overall passing percentage with new total student count.
overall_passing_percentage = (overall_passing_math_reading_count / newStudentCount) * 100
overall_passing_percentage


# In[871]:


# Creates district summary DataFrame
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count, 
          "Total Students": student_count, 
          "Total Budget": total_budget,
          "Average Math Score": average_math_score, 
          "Average Reading Score": average_reading_score,
          "% Passing Math": float
          (passing_math_percentage),
         "% Passing Reading": float(passing_reading_percentage),
        "% Overall Passing": float(overall_passing_percentage)}])

district_summary_df


# In[872]:


# Formatting the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

# Formatting the "Total Budget" to have the comma for a thousands separator, a decimal separator and a "$".
district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

# Formatting the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.1f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.1f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.1f}".format)

# Displays the data frame
district_summary_df


# ##  School Summary

# In[873]:


# Determines the School Type
per_school_types = school_data_df.set_index(["school_name"])["type"]

# Calculates the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()

# Calculates the total school budget and per capita spending
per_school_budget = school_data_complete_df.groupby(["school_name"]).mean()["budget"]
# Calculates the per capita spending.
per_school_capita = per_school_budget / per_school_counts

# Calculates the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]

# Calculates the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]

# Calculates the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]

# Calculates the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100
per_school_passing_reading = per_school_passing_reading / per_school_counts * 100

# Calculates the students who passed both reading and math.
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)
                                               & (school_data_complete_df["math_score"] >= 70)]

# Calculates the number of students passing math and passing reading by school.
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]

# Calculates the percentage of passing math and reading scores per school.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100


# In[874]:


# Creates school summary DataFrame
per_school_summary_df = pd.DataFrame({
    "School Type": per_school_types,
    "Total Students": per_school_counts,
    "Total School Budget": per_school_budget,
    "Per Student Budget": per_school_capita,
    "Average Math Score": per_school_math,
    "Average Reading Score": per_school_reading,
    "% Passing Math": per_school_passing_math,
    "% Passing Reading": per_school_passing_reading,
    "% Overall Passing": per_overall_passing_percentage})


# per_school_summary_df.head()


# In[875]:


# Formatting the Total School Budget and the Per Student Budget
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)

# Displays the school summary DataFrame
per_school_summary_df


# In[876]:


# Getting the number of 10th-12th graders from Thomas High School (THS).
thsTenTwelve = school_data_complete_df.loc[(school_data_complete_df['school_name'] == 'Thomas High School')].count()['reading_score']

thsTenTwelve


# In[877]:


# Getting all the students passing math from THS
thsPassingMath = school_data_complete_df.loc[(school_data_complete_df['school_name'] == 'Thomas High School') & (school_data_complete_df['math_score']>=70)]
thsPassingMathCount = thsPassingMath.count()['student_name']
thsPassingMath.head()


# In[878]:


# Getting all the students passing reading from THS
thsPassingReading = school_data_complete_df.loc[(school_data_complete_df['school_name']=='Thomas High School') & (school_data_complete_df['reading_score']>=70)]
thsPassingReadingCount = thsPassingReading.count()['student_name']
thsPassingReading.head()


# In[879]:


# Getting all the students passing math and reading from THS
thsPassingBoth = school_data_complete_df.loc[(school_data_complete_df['reading_score'] >= 70) & (school_data_complete_df['math_score'] >= 70) & (school_data_complete_df['school_name']=='Thomas High School')]
thsPassingBothCount = thsPassingBoth.count()['student_name']
thsPassingBoth.head()


# In[880]:


# Calculates the percentage of 10th-12th grade students passing math from Thomas High School.
tenTwelveMathPerc = thsPassingMathCount / thsTenTwelve * 100
tenTwelveMathPerc


# In[881]:


# Calculates the percentage of 10th-12th grade students passing reading from Thomas High School.
tenTwelveReadingPerc = thsPassingReadingCount / thsTenTwelve * 100
tenTwelveReadingPerc


# In[882]:


# Calculates the overall passing percentage of 10th-12th grade from Thomas High School.
tenTwelveBothPerc = thsPassingBothCount / thsTenTwelve * 100
tenTwelveBothPerc


# In[883]:


# Replaces the passing math percent for Thomas High School in the per_school_summary_df.
per_school_summary_df.loc['Thomas High School','% Passing Math'] = tenTwelveMathPerc


# In[884]:


# Replaces the passing reading percentage for Thomas High School in the per_school_summary_df.
per_school_summary_df.loc['Thomas High School','% Passing Reading'] = tenTwelveReadingPerc


# In[885]:


# Replaces the overall passing percentage for Thomas High School in the per_school_summary_df.
per_school_summary_df.loc['Thomas High School','% Overall Passing'] = tenTwelveBothPerc
per_school_summary_df


# ## High and Low Performing Schools 

# In[886]:


# Sorts and shows top five schools.
topSchools = per_school_summary_df.nlargest(5,'% Overall Passing')
topSchools


# In[887]:


# Sorts and shows top five schools.
bottomSchools = per_school_summary_df.nsmallest(5,'% Overall Passing')
bottomSchools


# ## Math and Reading Scores by Grade

# In[888]:


# Creating a Series of scores by grade levels using conditionals.
ninthGraders = school_data_complete_df[(school_data_complete_df['grade']=='9th')]
tenthGraders = school_data_complete_df[(school_data_complete_df['grade']=='10th')]
eleventhGraders = school_data_complete_df[(school_data_complete_df['grade']=='11th')]
twelfthGraders = school_data_complete_df[(school_data_complete_df['grade']=='12th')]

# Groups each school Series by the school name for the average math score.
ninthGradersMathScores = ninthGraders.groupby(['school_name']).mean()['math_score']
tenthGradersMathScores = tenthGraders.groupby(['school_name']).mean()['math_score']
eleventhGradersMathScores = eleventhGraders.groupby(['school_name']).mean()['math_score']
twelfthGradersMathScores = twelfthGraders.groupby(['school_name']).mean()['math_score']

# Groups each school Series by the school name for the average reading score.
ninthGradersReadingScores = ninthGraders.groupby(['school_name']).mean()['reading_score']
tenthGradersReadingScores = tenthGraders.groupby(['school_name']).mean()['reading_score']
eleventhGradersReadingScores = eleventhGraders.groupby(['school_name']).mean()['reading_score']
twelfthGradersReadingScores = twelfthGraders.groupby(['school_name']).mean()['reading_score']


# In[889]:


# Combines each Series for average math scores by school into single data frame.
avgMathDf = pd.DataFrame({
    '9th Grade':ninthGradersMathScores,
    '10th Grade':tenthGradersMathScores,
    '11th Grade':eleventhGradersMathScores,
    '12th Grade':twelfthGradersMathScores
})


# In[890]:


# Combines each Series for average reading scores by school into single data frame.
avgReadingDf = pd.DataFrame({
    '9th Grade':ninthGradersReadingScores,
    '10th Grade':tenthGradersReadingScores,
    '11th Grade':eleventhGradersReadingScores,
    '12th Grade':twelfthGradersReadingScores
})


# In[891]:


# Formatting avgMathDf columns
avgMathDf['9th Grade'] = avgMathDf['9th Grade'].map('{:.1f}'.format)
avgMathDf['10th Grade'] = avgMathDf['10th Grade'].map('{:.1f}'.format)
avgMathDf['11th Grade'] = avgMathDf['11th Grade'].map('{:.1f}'.format)
avgMathDf['12th Grade'] = avgMathDf['12th Grade'].map('{:.1f}'.format)


# In[892]:


# Remove the index.
avgMathDf.index.name = None

# Display the data frame
avgMathDf.loc[['Thomas High School']]


# In[893]:


# Formatting avgReadingDf columns
avgReadingDf['9th Grade'] = avgReadingDf['9th Grade'].map('{:.1f}'.format)
avgReadingDf['10th Grade'] = avgReadingDf['10th Grade'].map('{:.1f}'.format)
avgReadingDf['11th Grade'] = avgReadingDf['11th Grade'].map('{:.1f}'.format)
avgReadingDf['12th Grade'] = avgReadingDf['12th Grade'].map('{:.1f}'.format)


# In[894]:


## Remove the index.
avgReadingDf.index.name = None

# Display the data frame
avgReadingDf.loc[['Thomas High School']]


# ## Scores by School Spending

# In[895]:


# Establishes the spending bins and group names.
spendingBins = [0, 585, 615, 645, 675]
groupNames = ['<$584', '$585-629','630-644','645-675']

# Categorizes spending based on the bins.
per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spendingBins, labels=groupNames)
per_school_summary_df


# In[896]:


# Calculates the averages for the desired columns.
spendingMathScores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]

spendingReadingScores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]

spendingPercPassingMath = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]

spendingPercPassingReading = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]

spendingPercPassingBoth = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing"]


# In[908]:


# Creating spending summary DataFrame
spendingSummaryDf = pd.DataFrame({
    'Average Math Score' : spendingMathScores,
    'Average Reading Score': spendingReadingScores,
    '% Passing Math': spendingPercPassingMath,
    '% Passing Reading': spendingPercPassingReading,
    '% Overall Passing': spendingPercPassingBoth})

spendingSummaryDf


# In[898]:


# Formatting the spending summary DataFrame
spendingSummaryDf['Average Reading Score'] = spendingSummaryDf['Average Reading Score'].map('{:.1f}'.format)
spendingSummaryDf['Average Math Score'] = spendingSummaryDf['Average Math Score'].map('{:.1f}'.format)
spendingSummaryDf['% Passing Math'] = spendingSummaryDf['% Passing Math'].map('{:.0f}'.format)
spendingSummaryDf['% Passing Reading'] = spendingSummaryDf['% Passing Reading'].map('{:.0f}'.format)
spendingSummaryDf['% Overall Passing'] = spendingSummaryDf['% Overall Passing'].map('{:.0f}'.format)

spendingSummaryDf


# ## Scores by School Size

# In[899]:


# Establishes school size bins.
sizeBins = [0, 1000, 2000, 5000]
sizeGroupNames = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# Categorizes school size based on the bins.
per_school_summary_df['School Size'] = pd.cut(per_school_summary_df['Total Students'],sizeBins,labels=sizeGroupNames)
per_school_summary_df.head()


# In[900]:


# Calculates averages for the desired columns.
sizeMathScores = per_school_summary_df.groupby(["School Size"]).mean()["Average Math Score"]

sizeReadingScores = per_school_summary_df.groupby(["School Size"]).mean()["Average Reading Score"]

sizePercPassingMath = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Math"]

sizePercPassingReading = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Reading"]

sizePercPassingBoth = per_school_summary_df.groupby(["School Size"]).mean()["% Overall Passing"]


# In[901]:


# Assembles school size DataFrame.
sizeDf = pd.DataFrame({
    'Average Math Score' : sizeMathScores,
    'Average Reading Score': sizeReadingScores,
    '% Passing Math': sizePercPassingMath,
    '% Passing Reading': sizePercPassingReading,
    '% Overall Passing': sizePercPassingBoth})


# In[902]:


# Formatting school size DataFrame
sizeDf['Average Reading Score'] = sizeDf['Average Reading Score'].map('{:.1f}'.format)
sizeDf['Average Math Score'] = sizeDf['Average Math Score'].map('{:.1f}'.format)
sizeDf['% Passing Math'] = sizeDf['% Passing Math'].map('{:.0f}'.format)
sizeDf['% Passing Reading'] = sizeDf['% Passing Reading'].map('{:.0f}'.format)
sizeDf['% Overall Passing'] = sizeDf['% Overall Passing'].map('{:.0f}'.format)

sizeDf


# ## Scores by School Type

# In[903]:


# Calculates averages for the desired columns based on school type.
typeMathScore = per_school_summary_df.groupby(['School Type']).mean()['Average Math Score']
typeReadingScore = per_school_summary_df.groupby(['School Type']).mean()['Average Reading Score']
typePassingMath = per_school_summary_df.groupby(['School Type']).mean()['% Passing Math']
typePassingReading = per_school_summary_df.groupby(['School Type']).mean()['% Passing Reading']
typePassingBoth = per_school_summary_df.groupby(['School Type']).mean()['% Overall Passing']


# In[904]:


# Assembles into DataFrame.
typeDf = pd.DataFrame({
    'Average Math Score' : typeMathScore,
    'Average Reading Score': typeReadingScore,
    '% Passing Math': typePassingMath,
    '% Passing Reading': typePassingReading,
    '% Overall Passing': typePassingBoth})


# In[905]:


# Formatting school type DataFrame
typeDf['Average Reading Score'] = typeDf['Average Reading Score'].map('{:.1f}'.format)
typeDf['Average Math Score'] = typeDf['Average Math Score'].map('{:.1f}'.format)
typeDf['% Passing Math'] = typeDf['% Passing Math'].map('{:.0f}'.format)
typeDf['% Passing Reading'] = typeDf['% Passing Reading'].map('{:.0f}'.format)
typeDf['% Overall Passing'] = typeDf['% Overall Passing'].map('{:.0f}'.format)


# In[906]:


typeDf

