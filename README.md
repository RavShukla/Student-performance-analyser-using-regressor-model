# 🎓 Student Performance Analyzer using Regression Model

## 📌 Project Overview

The Student Performance Analyzer is a Machine Learning project that predicts student academic performance using regression algorithms. The model analyzes factors such as study time, attendance, family background, lifestyle habits, parental education, and school support to estimate student performance.

This project helps in understanding how different social, educational, and personal factors affect academic results and enables data-driven educational analysis.

The dataset used in this project was collected from Kaggle and other independent educational data sources.

---

# 🚀 Features

- 📊 Student performance prediction using regression models
- 🧠 Machine Learning-based analysis
- 🔄 Data preprocessing and feature encoding
- 📈 Correlation and performance analysis
- 🧮 Numerical and categorical feature handling
- ⚡ Clean and beginner-friendly implementation

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# 📂 Dataset Information

The dataset contains various student-related attributes such as:

- Academic background
- Study habits
- Family support
- Health and lifestyle
- Internet access
- Attendance
- Extracurricular activities

The target variable is the student's academic performance score.

---

# 🔄 Data Preprocessing

Before training the model, the dataset was cleaned and transformed into a machine-learning-friendly format.

## ✅ One-Hot Encoding

Categorical (non-numeric) features were converted into numerical form using One-Hot Encoding because machine learning algorithms can only process numerical data.

Encoding was performed using:

```python
X = pd.get_dummies(X, drop_first=True)
```

The parameter `drop_first=True` removes one category from each feature to avoid redundancy and multicollinearity.

---

# 📘 Encoded Features Explanation

## 🔹 Gender

- `sex_M = 1` → Male
- `sex_M = 0` → Female

---

## 🔹 Address Type

- `address_U = 1` → Urban
- `address_U = 0` → Rural

---

## 🔹 Family Size

- `famsize_LE3 = 1` → Family size ≤ 3
- `famsize_LE3 = 0` → Family size > 3

---

## 🔹 Parent Status

- `Pstatus_T = 1` → Parents living together
- `Pstatus_T = 0` → Parents apart

---

## 🔹 Mother’s Job (Mjob)

Encoded columns:

- `Mjob_health`
- `Mjob_services`
- `Mjob_teacher`
- `Mjob_other`

If all are `0`, the category is interpreted as `at_home`.

---

## 🔹 Father’s Job (Fjob)

Encoded columns:

- `Fjob_health`
- `Fjob_services`
- `Fjob_teacher`
- `Fjob_other`

If all are `0`, the category is interpreted as `at_home`.

---

## 🔹 Support Features

- `schoolsup_yes` → Extra school support
- `famsup_yes` → Family support
- `paid_yes` → Paid classes

---

## 🔹 Activities and Background

- `activities_yes` → Participates in extracurricular activities
- `nursery_yes` → Attended nursery school
- `higher_yes` → Wants higher education
- `internet_yes` → Has internet access
- `romantic_yes` → In a romantic relationship

---

# 📊 Numerical Features Used

The following features were already numerical and required no encoding:

- age
- Medu
- Fedu
- traveltime
- studytime
- failures
- famrel
- freetime
- goout
- Dalc
- Walc
- health
- absences

---

# 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Encoding
4. Train-Test Split
5. Model Training
6. Prediction
7. Performance Evaluation

---

# 📈 Model Objective

The main goal of this project is to predict student performance accurately and analyze the impact of educational, social, and lifestyle factors on academic success.

---

# ⚠️ Important Note

Because `drop_first=True` was used during encoding, one category from each categorical feature is removed and treated as the base/reference category.

Example:

If all job-related encoded columns are `0`, the job category is interpreted as `at_home`.

---

# ✅ Conclusion

One-Hot Encoding successfully transformed categorical variables into numerical form, making the dataset suitable for machine learning algorithms.

The regression model helps analyze student behavior and academic trends effectively while providing valuable insights into factors affecting student performance.

---

# 👨‍💻 Author

Gaurav

---
