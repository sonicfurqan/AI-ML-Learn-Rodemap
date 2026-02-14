# Titanic Survival Prediction: Logistic Regression & RFE

This project implements a binary classification pipeline to predict passenger survival on the Titanic using the classic Kaggle dataset. It focuses on data preprocessing, feature engineering based on exploratory data analysis (EDA), and automated feature selection.

---

## Technical Workflow

### 1. Data Cleaning & Imputation

Standardization of column headers to lowercase and snake_case for programmatic accessibility.

* **Missing Values:** * `age`: Imputed with the median (28.0) to preserve central tendency.
* `embarked`: Imputed with the mode ('S').
* `cabin`: Dropped due to a missingness threshold exceeding 70%.
* `fare`: Rows with null values in the test set were removed to maintain model input integrity.



### 2. Feature Engineering

Derived features created to capture non-linear relationships:

* **is_alone**: Boolean flag (1 if `sibsp` + `parch` == 0) to identify solo travelers.
* **is_minor**: Boolean flag (1 if `age` < 18) based on KDE plots showing higher survival rates for children.
* **One-Hot Encoding**: Categorical variables (`pclass`, `embarked`, `sex`) converted to dummy variables for compatibility with Logistic Regression.

### 3. Exploratory Data Analysis (EDA) Insights

* **Age:** Kernel Density Estimate (KDE) plots reveal a distinct survival spike for passengers under 16 years old.
* **Fare:** Mortality is heavily concentrated in the low-fare distribution, correlating with lower socio-economic status (Pclass 3).

### 4. Recursive Feature Elimination (RFE)

The model utilizes **Logistic Regression** as the base estimator. RFE is applied to iteratively rank and select the 8 most statistically significant features, reducing model complexity and preventing overfitting.

### 5. Evaluation Metrics

Performance is validated using a confusion matrix on a 20% test split, extracting:

* **True Negatives (TN)**
* **False Positives (FP)**
* **False Negatives (FN)**
* **True Positives (TP)**

---

## Key Learnings

* **Feature Selection Matters:** Raw data contains noise; using RFE ensures the model focuses on variables with the highest predictive power (e.g., gender and class) rather than redundant metrics.
* **Domain-Driven Engineering:** Visualizing distributions (KDE) allowed for the creation of `is_minor`, which captures a specific survival trend that raw age values might dilute.
* **Pipeline Consistency:** Preprocessing steps (imputation, encoding, dropping columns) must be applied identically to both training and testing datasets to prevent shape mismatch or data leakage.
* **Categorical Handling:** Logistic Regression requires numerical input; dummy variables are essential but require dropping the original categorical columns to avoid multicollinearity.

---

## Dependencies

* `numpy`
* `pandas`
* `seaborn`
* `matplotlib`
* `scikit-learn`