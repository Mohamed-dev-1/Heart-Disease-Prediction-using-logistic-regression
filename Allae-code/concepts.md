## This File has Explanation of some important concepts we had faced them during the project :


**1/ Fill missing values with "median" ?**

**Note : fortunately all the columns values are `int` and `float` so we have no `str`, we're working with numbers only**


---

here is the story from the beginning :

i checked for any missing values in the data set and found this :

male                 0
age                  0
education          105      <-
currentSmoker        0
cigsPerDay          29      <-
BPMeds              53      <-
prevalentStroke      0
prevalentHyp         0
diabetes             0
totChol             50      <-
sysBP                0
diaBP                0
BMI                 19      <-
heartRate            1      <-
glucose            388      <-
TenYearCHD           0



* The question now is : **How to fill those missing values ? and with what ?**

* The answer is : **we can fill those empty cells by the median of the column's values**


But , **Why with median exactly ?**

<h3>Let's understand why using **median** exactly for this project ?</h3>


Suppose we have:

Age:

45
52
38
Nan
49
61

-> we have 1 missing value

The model does not know what to do with `Nan`, so we need to replace it with some reasonable value. [This is called **value imputation** (إسناد القيمة) ]

in **imputation** we can use : "mean" , "median" , "mode" , or more advanced methods

But for our project , we're using the "**median**"

* **What is the median ?**

    - The **median is simply the middle value after sorting the data** , example:

    we have : 10, 20, 30, 40, 50

    => The median (middle value) is : 30

    and if we have an even number of values like: 10, 20, 30, 40

    the middle 2 values are 20 and 30, then :

        median = (20 + 30) / 2

        median = 25


* Why noy just use the mean (the average of all the column values) ?


Imagine we have people's cholesterol values:

    180
    190
    195
    200
    205
    210

All the values are resonably close to each other.

   - **using the mean** : 

    mean = (180 + 190 + 195 + 200 + 205 + 210) / 6

    **mean = 196.6**

   - **using the median** :

    median = (195 + 200) / 2

    **median = 197**

    So, Either using the median or the mean , the results would be similar for both.

But imagine we have this data :

    180
    190
    195
    200
    205
    800

   - **using the mean** : 

    mean = (180 + 190 + 195 + 200 + 205 + 800) / 6

    **mean = 295**

    The value 800 is an extreme value , it takes the mean value way too far comparing to the other values of the column.


   - **using the median** :

    median = (195 + 200) / 2

    **median = 197**

    The median value is more resonable because it it more proximate to the other values in the column.


    So , we prefer to use the median to fill the missing values because it produces a reasonable value to fill with.

    - The key difference between usign **median** and **mean** :

        **MEAN**

        - Every value influences it
                
        - Extreme values can pull it strongly
                
        - Sensitive to outliers


        **MEDIAN**

        - Looks at the middle of the distribution
                
        - Extreme values have much less influence
                
        - Robust to outliers


**That's the main reason we often prefer median imputation.**




The end of the explantion of "why do we use median exactly to fill in the missing values"
---





