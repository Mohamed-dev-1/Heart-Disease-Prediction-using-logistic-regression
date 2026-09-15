## This File has Explanation of some important concepts we had faced them during the project :


**1/ Fill missing values with "median" ?**

**Note : fortunately all the columns values are `int` and `float` so we have no `str`, we're working with numbers only**


---

here is the story from the beginning :

i checked for any missing values in the data frame and found this :

male                 0 \
age                  0 \
education          **105**      <- \
currentSmoker        0 \
cigsPerDay          **29**      <- \
BPMeds              **53**      <- \
prevalentStroke      0 \
prevalentHyp         0 \
diabetes             0 \
totChol             **50**      <- \
sysBP                0 \
diaBP                0 \
BMI                 **19**      <- \
heartRate            **1**      <- \
glucose            **388**      <- \
TenYearCHD           0 



* The question now is : **How to fill those missing values ? and with what ?**

* The answer is : **we can fill those empty cells by the median of the column's values**


But , **Why with median exactly ?**

<h3>Let's understand why using **median** exactly for this project ?</h3>


Suppose we have:

Age:

45 \
52 \
38 \
**Nan** \
49 \
61 

-> we have **1 missing value**

The model does not know what to do with **`Nan`**, so we need to replace it with some reasonable value. [This is called **value imputation** (إسناد القيمة) ]

in **imputation** we can use : **"mean"** , **"median"** , **"mode"** , or more advanced methods ...

But for our project , we're using the "**median**"

* **What is the median ?**

    - The **median is simply the middle value after sorting the data** , example:

    we have : 10, 20, **30**, 40, 50

    => The median (middle value) is : 30

    and if we have an even number of values like: 10, 20, 30, 40

    the middle 2 values are 20 and 30, then :

        median = (20 + 30) / 2

        median = 25


* Why not just use the mean (the average of all the column values) ?


Imagine we have people's cholesterol values:

    180
    190
    195
    200
    205
    210

**All the values are close to each other**.

   - **using the mean** : 

    mean = (180 + 190 + 195 + 200 + 205 + 210) / 6

    mean = 196.6

   - **using the median** :

    median = (195 + 200) / 2

    median = 197

So, Either **using the median or the mean , the results would be similar for both**:

- because as we've said : **all the values are close to each other**.

But imagine we have this data :

    180
    190
    195
    200
    205
    800
   
   Pay close attention that : **not all the numbers are close to each other due to 800 , it is an extreme value among the other values**.

   - **using the mean** : 

    mean = (180 + 190 + 195 + 200 + 205 + 800) / 6

    mean = 295

   **The value 800 is an extreme value , So it took the `mean` value way too far comparing to the other values of the column**.


   - **using the median** :

    median = (195 + 200) / 2

    median = 197

   **The median value is more reasonable** because **it is more proximate to the majority of the other values in the column**.


  So , we prefer to use **the median** to fill the missing values because the median produces a reasonable value (a close value to the other values of the same column) to fill with.

    - The key difference between using median and mean :

        * MEAN :

        - Every value influences it
                
        - Extreme values can pull it strongly
                
        - Sensitive to outliers


        * MEDIAN :

        - Looks at the middle of the distribution
                
        - Extreme values have much less influence
                
        - Robust to outliers


**So the main reason we often prefer median imputation simply is : that the median produces a value close to the other values of that same column.**




The end of the explantion of "why do we use median exactly to fill in the missing values"
---


**2/ Why do we use `random_state = 42` in : `X_train, ... , y_test = train_test_split(x, y, test_size = 0.25 , random_state=42)` ?**

we've said that the `train_test_split()` method :

   - Gets the features "x" and the target "y" as parameters + the "test_size" + "random_state"

   - Then the method shuffles the rows randomly and split the shuffled rows into 2 separate non-overlapping groups (training and testing)

   now, **the data shuffling and splitting is random , and that will cause a problem**, let's figure it out :

   ---

   * If we keep that random shuffling we will not be able to ensure that our model is actually performing good , **we can prove that by avoiding to use "random_state=number"** and **the model accuracy will not be stable at all** : 82% in test 1 , 79% in test 2 , 90 % in test 3 , why ? **simply because the data splitting and shuffling is random**.
   * **The main problem** of random shuffling and splitting is that :

        - **In run 1 The model Can get easy data to test** on (to predict) by luck (because the shuffling and splitting was random).
        - **In run 2 the model can get harder data to test** on (to predict) also by luck (because the shuffling and splitting was random).
     
  So , let's say we got 90% accuracy in run 1 and 79% in run 2 , the accuracy difference (90% vs 79%) tells us nothing about our model's improvement, it's just noise from which rows got picked (easy rows to predict in run 1 and harder rows to predict in run 2 , all by luck).

So , setting "random_state=number" is like defining a splitting and shuffling pattern or rule ,so the same split pattern happens every single time before training and testing our model to avoid getting random data splitting and shuffling , This makes results reproducible: if performance changes, it's because of your actual changes to the model, not random luck in the split.

   - Without random_state: accuracy goes from 79% to 85%. Did our model actually improved? We can't tell , maybe the split just got easier this time.
   - With random_state=42: **The shuffling and splitting pattern is the same every time** then the test set is identical every run. So if accuracy goes from 79% to 85%, we know for certain it's because our model actually got better, not because the model got easy rows to predict.
    

* How does `random_state=42` work?

     - It gives the random process (the shuffling and splitting pattern generator) a fixed seed (starting point).

        **random_state=42** , means: **"Use the same starting point for the random process every time."**

        Therefore:

        Run 1 -> Same split
        Run 2 -> Same split
        Run 3 -> Same split

        So the results are reproducible.


    * **Why exactly the number 42 in `random_state` ?**

     - There is nothing special about the number 42 , we can use :
       - `random_state=1` or
       - `random_state=2` or
       - `random_state=100`

       They are all valid.

     - The important thing is to use the same fixed number if you want the same split every time 


* Here how it works approximately :

    1- random_state=42
        
        2- Start the "random-number" generator
            
        3- Generator produces a sequence of "random" numbers
            
        4- train_test_split() uses those generated random numbers to shuffle/select the rows
            
        5- every time we use `random_state=42` we got the Same random numbers
            ↓
        6- Same shuffle and Same split
    
    Note : we've said that **train_test_split() uses those generated random numbers to shuffle/select the rows** ,

  * **the question is : how could we know if those random numbers generated by the random-number generator will not select easy rows to test on ?**
 
    - the answer is : **random_state=number doesn't promise to select hard or easy rows.**
    - It's entirely possible that seed 42 for example produce a test set that's a bit easier (or harder) than average, it doesn't know anything about "easy" or "hard" rows, it's just a fixed shuffling pattern. 

   That's a real limitation, and it's the reason why more rigorous approaches exist , here is a glance about those approaches :

    - **Cross-validation (e.g. k-fold)**: instead of one fixed split, the data is split into k different folds, and the model is trained/tested k times, once per fold, then scores are averaged. This way, every row gets to be in the test set at least once, so one lucky/unlucky split can't skew your conclusion.
    - **Multiple random states**: some people even repeat the whole train/test process with several different seeds (starting points) and average the results, to check that performance isn't just an artifact of one particular split.
    - **Stratified splitting**: for classification, stratify=y is often used so the class proportions (e.g. 60% class A, 40% class B) are preserved in both train and test, reducing (not eliminating) the chance of a skewed split.

---

