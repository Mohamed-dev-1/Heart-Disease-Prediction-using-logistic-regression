# Heart Disease Prediction Using Logistic Regression

A machine learning project that uses **Logistic Regression** to predict whether a person is at risk of developing **coronary heart disease (CHD) within 10 years**, based on health and lifestyle-related features.

> **Disclaimer:** This project is for educational purposes only and is not a medical diagnostic tool.

---

## Project Goal

The goal of this project is to train a machine learning model that answers:

> **Given a person's health and lifestyle characteristics, can we predict whether they belong to the 10-year CHD risk class 0 or 1?**

The target variable is:

* `0` -> No CHD within 10 years
* `1` -> CHD within 10 years

Since the target has two possible classes, this is a **binary classification problem**.

---

## Dataset

The project uses the **Framingham Heart Study dataset**.

The dataset contains information about patients such as:

* Age
* Gender
* Education
* Current smoking status
* Cigarettes smoked per day
* Blood pressure medication
* Prevalent stroke
* Hypertension
* Diabetes
* Total cholesterol
* Systolic blood pressure
* Diastolic blood pressure
* BMI
* Heart rate
* Glucose levels

### Target

```text
TenYearCHD
```

This is the value that our model tries to predict.

---

## Machine Learning Approach

The project follows a typical machine learning workflow:

```text
- Dataset
   
- Load the data
   
- Understand the data
   
- Explore the data
   
- Handle missing values
   
- Separate Features (X) and Target (y)
   
- Train / Test Split
   
- Feature Scaling
   
- Logistic Regression
   
- Make Predictions
   
- Evaluate the Model
   
- Improve the Model
```

---

## Why Logistic Regression?

Logistic Regression is suitable for this project because our target is binary:

```text
0 -> No CHD
1 -> CHD
```

Unlike Linear Regression, which predicts a continuous numerical value, Logistic Regression predicts the probability of belonging to a class.

Conceptually:

```text
Patient Features
       
Logistic Regression
       
Probability
       
Class 0 or Class 1
```

For example:

```text
Predicted probability = 0.82
        
Probability ≥ 0.5
        
Prediction = 1
```

---

## Model Evaluation

The model will be evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

These metrics will help us understand not only how many predictions were correct, but also **what types of mistakes the model makes**.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

## Project Structure

```text
heart-disease-prediction/
│
├── framingham.csv
├── heart_disease.ipynb
└── app.py
```

---

## Project Status

**In Progress**

Currently working through:

* [x] Load the dataset
* [x] Inspect the dataset
* [x] Identify missing values
* [x] Understand median imputation
* [x] Handle missing values correctly
* [x] Separate features and target
* [x] Train / test split
* [x] Feature scaling
* [x] Train Logistic Regression model
* [x] Make predictions
* [x] Evaluate the model
* [ ] Analyze the confusion matrix
* [ ] Improve the model

---

## Learning Objectives

This project is mainly focused on understanding the fundamentals of **binary classification** and Logistic Regression.

The main concepts being practiced are:

* Binary classification
* Logistic Regression
* Probability and classification thresholds
* Data preprocessing
* Missing-value imputation
* Train / test splitting
* Feature scaling
* Model training
* Model prediction
* Classification metrics
* Confusion matrices
* Data leakage
* Model evaluation

---

## Reference

This project follows the general workflow presented in the GeeksforGeeks tutorial:

**Heart Disease Prediction Using Logistic Regression**

The implementation is being developed step-by-step with an emphasis on understanding **why each step is performed**, rather than simply copying the code.
