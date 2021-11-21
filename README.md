# School_District_Analysis
##Overview of the school district analysis
Our purpose is simple; Aid the City School District by **preparing all standardized test data**, **analyzing that data**, 
then **reporting and presenting that data**. With the new data, we will be able to present **performance trends** and **patterns**
based on specifics such as ```School Type``` or even the ```Budget```.

###Analysis Issues
While analyzing the City School District data, it was discovered that the grades for the 9th graders at Thomas High School
were altered. Due to the dishonest reading and math scores, all of the grades of the 9th graders at Thomas High School
have been nullified by changing them to ```NaN```. The analysis was redone inorder to account for the new data set.

##Results
###How was the district summary affected?
Before we start, we need to look at the original City School District summary alongside the new summary.
####Original District Summary:
![Original Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/districtbefore.png)

####New District Summary:
![New Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/districtafter.png)

Now let's take a look at how removing the 9th graders grades effected the City School District Summary. Not everything
has been effected, so I've listed and discussed the column values that have changed below.
- ```Average Math Score```
  - Original Average Math Score: ```79.0```
  - New Average Math Score: ```78.9```
  - Decreased by: ```0.1```
    - As you can see, the **Average Math Score** has been **decreased**! It's not a significant change but in the big scheme
of things, this change matters. 
- ```% Passing Math```
  - Original % Passing Math: ```75```
  - New % Passing Math: ```74.8```
  - Decreased by: ```0.2%```
    - Again, another **decrease**. 
    
- ```% Passing Reading```
  - Original % Passing Reading: ```86```
  - New % Passing Reading: ```85.7```
  - Decreased by: ```0.3%```
    
- ```% Overall Passing```
  - Original % Passing Both: ```65```
  - New % Passing Both: ```65.9```
  - Decreased by: ```0.1%```

By looking at the new figures, we can see a decrease in almost every grade related column value.
###How is the school summary affected?

Next lets take a look at how our school summary dataframe was affected. Just like earlier, I'm going to display both the
original and new dataframes:
####Original School Summary:
![Original Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/districtbefore.png)
####New School Summary:
![New Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/districtafter.png)

As I'm sure you suspected the results you see above. You can see that Thomas High Schools values have decreased due to
the new analysis with the missing grades. Lets dive a little deeper!

###How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance relative to the other schools?
Before we dive in, lets take a look at the before and after values just like earlier:
####Original THS Summary:
![Original Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/BeforeChangedGrades.png)
####New THS Summary:
![New Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/AfterChangedGrades.png)

Here is a break down of the changes:

- ```Average Math Score```
  - Original Average Math Score: ```83.418349```
  - New Average Math Score: ```83.350937```
  - Decreased by: ```0.067412```
  
- ```Average Reading Score```
  - Original Average Reading Score: ```83.848930```
  - New Average Reading Score: ```83.896082```
  - Increased by: ```0.047152```

    
- ```% Passing Math```
  - Original % Passing Math: ```93.272171%```
  - New % Passing Math: ```93.185690%```
  - Decreased by: ```0.086481%```

- ```% Passing Reading```
  - Original % Passing Reading: ```97.308869%```
  - New % Passing Reading: ```97.018739%```
  - Decreased by: ```0.29013%```

- ```% Overall Passing```
  - Original % Passing Both: ```90.948012%```
  - New % Passing Both: ```90.630324%```
  - Decreased by: ```0.317688%```

The changes in the data can be attributed to the fact that the new scores are used to recalculate the data relative to
the other schools. As you can see, most values decreased, except for one:``Average Reading Score```, which in fact **increased!**

###The following is effected by replacing the 9th grades scores:

####Math and reading scores by grade

#####Original Math Scores By Grade:

![Original Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/thsMathBefore.png)

#####New Math Scores By Grade:

![New Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/thsMathAfter.png)


#####Original Reading Scores By Grade:
![Original Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/thsReadingBefore.png)

#####New Reading Scores By Grade:
![New Data](https://github.com/StickySitch/School_District_Analysis/tree/main/Images/thsReadingAfter.png)

Now when looking at this data, it's important to note the ```nan``` value in the new data sets. Since we removed the 9th
graders scores, ```nan``` will take its place essentially meaning skip this score and continue calculations. None of the
other scores are changed. This change in value also changes the overall scores of Thomas High School compared to other schools
as shown earlier. 

**The Following DataFrames had NO change in test scores by the replacement:**
- Scores by school spending
  - ```All values stayed the same```
- Scores by school size 
  - ```All values stayed the same```
- Scores by school type
  - ```All values stayed the same```

##Summary
To summarize the new data, there are two key factors to look at: ```District Summary``` and ```School Summary```. As seen
above in our School and District summary breakdown, most values decreased or stayed the same but the difference wasn't super significant.
No other data was affected due to the new scores from Thomas High School.

