#!/usr/bin/env python
# coding: utf-8

# In[498]:


#Adding Panadas dependency
import pandas as pd
import os


# In[499]:


#Load CSV Files
school_data_to_load = os.path.join("Resources","schools_complete.csv")
student_data_to_load = os.path.join("Resources","students_complete.csv")


# In[500]:


#Reading CSV Files
studentDataDf = pd.read_csv(student_data_to_load)
schoolDataDf = pd.read_csv(school_data_to_load)

#Skipping header row in CSV files
schoolDataDf.head()


# In[501]:


studentDataDf.head()


# In[502]:


#Checking for missing data with "count()"
schoolDataDf.count()


# In[503]:


#Checking for missing data with "count()"
studentDataDf.count()


# In[504]:


#Checking for missing data with "isnull()"
schoolDataDf.isnull()


# In[505]:


#Checking for missing data with "isnull()"
studentDataDf.isnull()


# In[506]:


#Checking for missing data by chaining "sum()" with "isnull()"
studentDataDf.isnull().sum()


# In[507]:


#Checking for missing data with "notnull()"
schoolDataDf.notnull()


# In[508]:


#Checking for missing data by chaining "sum()" with "notnull()"
studentDataDf.notnull().sum()


# In[509]:


#Checking column data types
studentDataDf.dtypes


# In[510]:


schoolDataDf.dtypes


# In[511]:


# Adding each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

#Iterating through each "student_name",
#checking for and remove any prefixes or suffixes
for words in prefixes_suffixes:
    #replacing prefix or suffix with nothing
    studentDataDf['student_name'] = studentDataDf['student_name'].str.replace(words,'',regex=False)
studentDataDf


# In[512]:


# Combine the data into a single dataset.
schoolDataCompleteDf = pd.merge(studentDataDf, schoolDataDf, on=['school_name','school_name'])
schoolDataCompleteDf.head()


# In[513]:


studentCount = schoolDataCompleteDf['Student ID'].count()
studentCount


# In[514]:


# Calculate the total number of schools.
schoolCount = schoolDataDf['school_name'].count()
schoolCount


# In[515]:


schoolCount2 = schoolDataCompleteDf['school_name'].unique()
len(schoolCount2)


# In[516]:


# Calculate total budget
totalBudget = schoolDataDf['budget'].sum()
totalBudget


# In[517]:


# Calculate average reading score
avgReading = schoolDataCompleteDf['reading_score'].mean()
avgReading


# In[518]:


# Calculating average math score
avgMath = schoolDataCompleteDf['math_score'].mean()
avgMath


# In[519]:


passingMath.head(10)


# In[520]:


# Get all the students who are passing math in a new DataFrame.
passingMath = schoolDataCompleteDf[schoolDataCompleteDf['math_score'] >= 70]
passingMath.head()


# In[521]:


# Get all the students that are passing reading in a new DataFrame.
passingReading = schoolDataCompleteDf[schoolDataCompleteDf['reading_score'] >= 70]
passingReading.head()


# In[522]:


# Calculate the number of students passing math.
passingMathCount = passingMath['student_name'].count()

# Calculate the number of students passing reading.
passingReadingCount = passingReading['student_name'].count()

print("Passing math count: " + str(passingMathCount))
print("Passing reading count: " + str(passingReadingCount))


# In[523]:


#Calculating passing percentages
passingReadingPerc = passingReadingCount / float(studentCount) * 100
passingMathPerc = passingMathCount / float(studentCount) * 100
print(f'Passing math percentage {passingMathPerc}\n'
      f'Passing reading percentage {passingReadingPerc}')


# In[524]:


#Looking for students that passed BOTH math and reading
passingBoth = schoolDataCompleteDf[(schoolDataCompleteDf['math_score'] >= 70) & (schoolDataCompleteDf['reading_score'] >= 70)]

passingBoth.head()


# In[525]:


#Get count of students who passed BOTH math & english
passingBothCount = passingBoth['student_name'].count()
passingBothCount


# In[526]:


#Calculate passing both percentage
passingBothPerc = passingBothCount / studentCount * 100
passingBothPerc


# In[527]:


districtSummaryDf = pd.DataFrame(
    [{"Total Schools": schoolCount,
      "Total Students": studentCount,
      "Total Budget": totalBudget,
      "Average Math Score": avgMath,
      "Average Reading Score": avgReading,
      "% Passing Math": passingMathPerc,
      "% Passing Reading": passingReadingPerc,
      "% Overall Passing": passingBothPerc}])
districtSummaryDf


# In[528]:


# Format the "Total Students" to have the comma for a thousands separator.
districtSummaryDf['Total Students'] = districtSummaryDf['Total Students'].map('{:,}'.format)

districtSummaryDf['Total Students']


# In[529]:


districtSummaryDf['Total Budget'] = districtSummaryDf['Total Budget'].map("${:,.2f}".format)

districtSummaryDf['Total Budget']


# In[530]:


#Formatting all columns
districtSummaryDf['Average Math Score'] = districtSummaryDf['Average Math Score'].map('{:.1f}'.format)

districtSummaryDf['Average Reading Score'] = districtSummaryDf['Average Reading Score'].map('{:.1f}'.format)

districtSummaryDf['% Passing Reading'] = districtSummaryDf['% Passing Reading'].map('{:.0f}'.format)

districtSummaryDf['% Passing Math'] = districtSummaryDf['% Passing Math'].map('{:.0f}'.format)

districtSummaryDf['% Overall Passing'] = districtSummaryDf['% Overall Passing'].map('{:.0f}'.format)


# In[531]:


districtSummaryDf


# In[532]:


perSchoolType = schoolDataDf.set_index(['school_name'])['type']
perSchoolType


# In[533]:


df = pd.DataFrame(perSchoolType)
df


# In[534]:


perSchoolCount = schoolDataDf.set_index(['school_name'])['size']
perSchoolCount


# In[535]:


perSchoolCount = schoolDataCompleteDf['school_name'].value_counts()
perSchoolCount


# In[536]:


#Get budget for each school
perSchoolBudget = schoolDataDf.set_index(['school_name'])['budget']
perSchoolBudget


# In[537]:


perSchoolCapita = perSchoolBudget / perSchoolCount
perSchoolCapita


# In[538]:


# Calculate the math scores.
studentSchoolMath = studentDataDf.set_index(['school_name'])['math_score']
studentSchoolMath


# In[539]:


# Get passing math grades
passingMath = schoolDataCompleteDf['math_score'] >= 70


# In[540]:


perSchoolAverages = schoolDataCompleteDf.groupby(['school_name']).mean()
perSchoolAverages


# In[541]:


perSchoolMath = schoolDataCompleteDf.groupby(['school_name']).mean()['math_score']

if __name__ == '__main__':
    perSchoolReading = schoolDataCompleteDf.groupby(['school_name']).mean()['reading_score']
perSchoolMath


# In[542]:


perSchoolReading


# In[543]:


perSchoolPassingMath = schoolDataCompleteDf[(schoolDataCompleteDf['math_score'] >= 70)]

perSchoolPassingReading = schoolDataCompleteDf[(schoolDataCompleteDf['reading_score'] >= 70)]


# In[544]:


perSchoolPassingMath = perSchoolPassingMath.groupby(['school_name']).count()['student_name']
perSchoolPassingMath


# In[545]:


perSchoolPassingReading = perSchoolPassingReading.groupby(['school_name']).count()['student_name']
perSchoolPassingReading


# In[546]:


perSchoolPassingMath


# In[547]:


perSchoolPassingMath = perSchoolPassingMath / perSchoolCount * 100

perSchoolPassingReading = perSchoolPassingReading / perSchoolCount * 100
perSchoolPassingReading


# In[548]:


perSchoolPassingMath


# In[549]:


perPassingBoth = schoolDataCompleteDf[(schoolDataCompleteDf['math_score'] >= 70) & (schoolDataCompleteDf['reading_score'] >= 70)]
perPassingBoth.head()


# In[550]:


# Calculate the number of students who passed both math and reading.
perPassingBoth = perPassingBoth.groupby(['school_name']).count()['student_name']
perPassingBoth


# In[551]:


# Calculate the overall passing percentage.
perOverallPassingPerc = perPassingBoth / perSchoolCount * 100
perOverallPassingPerc


# In[552]:


perSchoolSummaryDf = pd.DataFrame({
    'School Type': perSchoolType,
    'Total Students': perSchoolCount,
    'Total School Budget': perSchoolBudget,
    'Per Student Budget': perSchoolCapita,
    'Average Math Score': perSchoolMath,
    'Average Reading Score': perSchoolReading,
    '% Passing Math': perSchoolPassingMath,
    '% Passing Reading': perSchoolPassingReading,
    '% Overall Passing': perOverallPassingPerc})
perSchoolSummaryDf


# In[553]:


# Formatting the Total School Budget and the Per Student Budget columns.
perSchoolSummaryDf['Total School Budget'] = perSchoolSummaryDf['Total School Budget'].map('${:,.2f}'.format)

perSchoolSummaryDf['Per Student Budget'] = perSchoolSummaryDf['Per Student Budget'].map('${:,.2f}'.format)

# Displaying the data frame
perSchoolSummaryDf.head()


# In[554]:


topSchools = perSchoolSummaryDf.sort_values(['% Overall Passing'], ascending=False)
topSchools.head()


# In[555]:


bottomSchools = perSchoolSummaryDf.sort_values(['% Overall Passing'], ascending=True)
bottomSchools.head()


# In[556]:


passingMath = schoolDataCompleteDf['math_score'] >= 70
passingReading = schoolDataCompleteDf['reading_score'] >= 70


# In[557]:


# Creating a grade level DataFrames.
ninthGraders = schoolDataCompleteDf[(schoolDataCompleteDf['grade'] == '9th')]

tenthGraders = schoolDataCompleteDf[(schoolDataCompleteDf['grade'] == '10th')]

eleventhGraders = schoolDataCompleteDf[(schoolDataCompleteDf['grade'] == '11th')]

twelfthGraders = schoolDataCompleteDf[(schoolDataCompleteDf['grade'] == '12th')]


# In[558]:


ninthGraders


# In[559]:


ninthGradersMathScores = ninthGraders.groupby(['school_name']).mean()['math_score']

tenthGradersMathScores = tenthGraders.groupby(['school_name']).mean()['math_score']

eleventhGradersMathScores = eleventhGraders.groupby(['school_name']).mean()['math_score']

twelfthGradersMathScores = twelfthGraders.groupby(['school_name']).mean()['math_score']


# In[560]:


ninthGradersMathScores


# In[561]:


eleventhGradersMathScores


# In[562]:


ninthGradersReadingScores = ninthGraders.groupby(['school_name']).mean()['reading_score']

tenthGradersReadingScores = tenthGraders.groupby(['school_name']).mean()['reading_score']

eleventhGradersReadingScores = eleventhGraders.groupby(['school_name']).mean()['reading_score']

twelfthGradersReadingScores = twelfthGraders.groupby(['school_name']).mean()['reading_score']


# In[563]:


ninthGradersReadingScores


# In[564]:


twelfthGradersReadingScores


# In[565]:


mathScoresByGrade = pd.DataFrame({
    '9th': ninthGradersMathScores,
    '10th': tenthGradersMathScores,
    '11th': eleventhGradersMathScores,
    '12th': twelfthGradersMathScores
})
mathScoresByGrade


# In[566]:


readingScoresByGrade = pd.DataFrame({
    '9th': ninthGradersReadingScores,
    '10th': tenthGradersReadingScores,
    '11th': eleventhGradersReadingScores,
    '12th': twelfthGradersReadingScores
})
readingScoresByGrade


# In[567]:


#formattig math scores to one decimal place
mathScoresByGrade['9th'] = mathScoresByGrade['9th'].map('{:.1f}'.format)
mathScoresByGrade['10th'] = mathScoresByGrade['10th'].map('{:.1f}'.format)
mathScoresByGrade['11th'] = mathScoresByGrade['11th'].map('{:.1f}'.format)
mathScoresByGrade['12th'] = mathScoresByGrade['12th'].map('{:.1f}'.format)

# Making sure the columns are in the correct order.'
mathScoresByGrade = mathScoresByGrade[['9th','10th','11th','12th']]
#Removing index name
mathScoresByGrade.index.name = None

mathScoresByGrade.loc[['Thomas High School']]


# In[568]:


#formattig reading scores to one decimal place
readingScoresByGrade['9th'] = readingScoresByGrade['9th'].map('{:.1f}'.format)
readingScoresByGrade['10th'] = readingScoresByGrade['10th'].map('{:.1f}'.format)
readingScoresByGrade['11th'] = readingScoresByGrade['11th'].map('{:.1f}'.format)
readingScoresByGrade['12th'] = readingScoresByGrade['12th'].map('{:.1f}'.format)

# Making sure the columns are in the correct order.'
readingScoresByGrade = readingScoresByGrade[['9th','10th','11th','12th']]
#Removing index name
readingScoresByGrade.index.name = None

readingScoresByGrade.loc[['Thomas High School']]


# In[569]:


perSchoolCapita.describe()


# In[570]:


spendingBins = [0, 585, 615, 645, 675]


# In[571]:


pd.cut(perSchoolCapita,spendingBins)


# In[572]:


# Cut the per_school_capita into the spending ranges. *INCORRECT*
spending_bins = [585, 615, 645, 675]
pd.cut(perSchoolCapita, spending_bins)


# In[573]:


# Cut the per_school_capita into the spending ranges.
perSchoolCapita.groupby(pd.cut(perSchoolCapita, spendingBins)).count()


# In[574]:


spendingBins = [0, 585, 630, 645, 675]
perSchoolCapita.groupby(pd.cut(perSchoolCapita, spendingBins)).count()


# In[575]:


groupNames = ['<$584', '$585-629','630-644','645-675']


# In[576]:


perSchoolSummaryDf['Spending Ranges (Per Student)'] = pd.cut(perSchoolCapita,spendingBins,labels=groupNames)

perSchoolSummaryDf


# In[577]:


#calculating the averages for the desired columns.
spendingMathScore = perSchoolSummaryDf.groupby(['Spending Ranges (Per Student)']).mean()['Average Math Score']

spendingReadingScore = perSchoolSummaryDf.groupby(['Spending Ranges (Per Student)']).mean()['Average Reading Score']

spendingPassingMath = perSchoolSummaryDf.groupby(['Spending Ranges (Per Student)']).mean()['% Passing Math']

spendingPassingReading = perSchoolSummaryDf.groupby(['Spending Ranges (Per Student)']).mean()['% Passing Reading']

spendingPassingAll = perSchoolSummaryDf.groupby(['Spending Ranges (Per Student)']).mean()['% Overall Passing']
spendingPassingAll


# In[588]:


#Assembling the spending dataframe
spendingSummaryDf = pd.DataFrame({
    'Average Math Score': spendingMathScore,
    'Average Reading Score': spendingReadingScore,
    '% Passing Math': spendingPassingMath,
    '% Passing Reading': spendingPassingReading,
    '% Overall Passing': spendingPassingAll
})

spendingSummaryDf


# In[579]:


spendingSummaryDf['Average Math Score'] = spendingSummaryDf['Average Math Score'].map('{:.1f}'.format)

spendingSummaryDf['Average Reading Score'] = spendingSummaryDf['Average Reading Score'].map('{:.1f}'.format)

spendingSummaryDf['% Passing Math'] = spendingSummaryDf['% Passing Math'].map('{:.0f}'.format)


spendingSummaryDf['% Passing Reading'] = spendingSummaryDf['% Passing Reading'].map('{:.0f}'.format)

spendingSummaryDf['% Overall Passing'] = spendingSummaryDf['% Overall Passing'].map('{:.0f}'.format)

spendingSummaryDf


# In[580]:


# Establish the bins.
sizeBins = [0, 1000, 2000, 5000]
sizeGroupNames = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[581]:


# Categorize spending based on the bins.\
perSchoolSummaryDf['School Size'] = pd.cut(perSchoolSummaryDf['Total Students'],sizeBins,labels=sizeGroupNames)
perSchoolSummaryDf.head()


# In[582]:


# Categorize spending based on the bins.
sizeMathScores = perSchoolSummaryDf.groupby(['School Size']).mean()['Average Math Score']

sizeReadingScores = perSchoolSummaryDf.groupby(['School Size']).mean()['Average Reading Score']

sizePassingMath = perSchoolSummaryDf.groupby(['School Size']).mean()['% Passing Math']

sizePassingReading = perSchoolSummaryDf.groupby(["School Size"]).mean()['% Passing Reading']

sizePassingAll = perSchoolSummaryDf.groupby(['School Size']).mean()['% Overall Passing']


# In[583]:


# Assembling into a DataFrame
sizeSummaryDf = pd.DataFrame({
    'Average Math Score': sizeMathScores,
    'Average Reading Score':sizeReadingScores,
    '% Passing Math': sizePassingMath,
    '% Passing Reading': sizePassingReading,
    '% Overall Passing': sizePassingAll
})
sizeSummaryDf


# In[584]:


sizeSummaryDf['Average Math Score'] = sizeSummaryDf['Average Math Score'].map('{:.1f}'.format)

sizeSummaryDf['Average Reading Score'] = sizeSummaryDf['Average Reading Score'].map('{:.1f}'.format)

sizeSummaryDf['% Passing Math'] = sizeSummaryDf['% Passing Math'].map('{:.0f}'.format)


sizeSummaryDf['% Passing Reading'] = sizeSummaryDf['% Passing Reading'].map('{:.0f}'.format)

sizeSummaryDf['% Overall Passing'] = sizeSummaryDf['% Overall Passing'].map('{:.0f}'.format)

sizeSummaryDf


# In[585]:


# Calculate averages for the desired columns.
typeMathScores = perSchoolSummaryDf.groupby(["School Type"]).mean()["Average Math Score"]

typeReadingScores = perSchoolSummaryDf.groupby(["School Type"]).mean()["Average Reading Score"]

typePassingMath = perSchoolSummaryDf.groupby(["School Type"]).mean()["% Passing Math"]

typePassingReading = perSchoolSummaryDf.groupby(["School Type"]).mean()["% Passing Reading"]

typeOverallPassing = perSchoolSummaryDf.groupby(["School Type"]).mean()["% Overall Passing"]


# In[586]:


typeSummaryDf = pd.DataFrame({
    'Average Math Score': typeMathScores,
    'Average Reading Score':typeReadingScores,
    '% Passing Math': typePassingMath,
    '% Passing Reading': typePassingReading,
    '% Overall Passing': typeOverallPassing
})
typeSummaryDf


# In[587]:


typeSummaryDf['Average Math Score'] = typeSummaryDf['Average Math Score'].map('{:.1f}'.format)

typeSummaryDf['Average Reading Score'] = typeSummaryDf['Average Reading Score'].map('{:.1f}'.format)

typeSummaryDf['% Passing Math'] = typeSummaryDf['% Passing Math'].map('{:.0f}'.format)


typeSummaryDf['% Passing Reading'] = typeSummaryDf['% Passing Reading'].map('{:.0f}'.format)

typeSummaryDf['% Overall Passing'] = typeSummaryDf['% Overall Passing'].map('{:.0f}'.format)

typeSummaryDf

