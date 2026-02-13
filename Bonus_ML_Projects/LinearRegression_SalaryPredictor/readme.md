# Linear Regression Learning Projects

This repository contains practical implementations of **Linear Regression** using Python and `scikit-learn`. It covers both **Simple Linear Regression** (single variable) and **Multiple Linear Regression** (multiple variables) to predict continuous outcomes.

## 📂 Projects Overview

### 1. Salary Predictor (Simple Linear Regression)
* **Goal:** Predict an employee's salary based on their years of experience.
* **Dataset:** `Salary_Data.csv`
* **Features:** `YearsExperience` (Independent Variable)
* **Target:** `Salary` (Dependent Variable)

### 2. Housing Price Predictor (Multiple Linear Regression)
* **Goal:** Predict real estate prices based on multiple property features.
* **Dataset:** `housing.csv`
* **Features:** `Area Income`, `House Age`, `Number of Rooms`
* **Target:** `Price`

---

## 🧠 Concepts Learned & Explained

### 1. Simple vs. Multiple Linear Regression
* **Simple Linear Regression:** Modeled the relationship between a single feature ($X$) and the target ($Y$) using the equation:
    $$Y = mX + c$$
    * *Code:* `model.fit(x_train, y_train)` using only `YearsExperience`.
* **Multiple Linear Regression:** Modeled the relationship between multiple features ($X_1, X_2, X_3$) and the target ($Y$):
    $$Y = b_0 + b_1X_1 + b_2X_2 + b_3X_3$$
    * *Code:* Predicting Price using `Area Income`, `House Age`, and `Number of Rooms`.

### 2. Data Preprocessing
* **Train-Test Split:**
    * Used `train_test_split(X, Y, test_size=0.2)` to divide data into Training (80%) and Testing (20%) sets.
    * *Why?* To prevent **overfitting**. We train on one set and validate on unseen data to ensure the model generalizes well.
* **Reshaping:**
    * Used `.reshape(-1, 1)` for single-feature inputs because `scikit-learn` expects a 2D array for the feature matrix $X$.
* **Data Cleaning:**
    * Converted data types using `.astype('int')` to ensure numerical consistency.
    * Dropped irrelevant columns (e.g., `Address`) that do not contribute to numerical prediction.

### 3. Model Parameters (The "Learning" Part)
* **Coefficient (Slope/Weight):** stored in `model.coef_`.
    * *Explanation:* Represents the change in the target variable for a 1-unit increase in the feature.
    * *Example:* A coefficient of `9449` for `YearsExperience` means for every 1 year added, the salary increases by ~$9,449.
* **Intercept (Bias):** stored in `model.intercept_`.
    * *Explanation:* The baseline value of the target when all features are 0.
    * *Example:* An intercept of `25792` implies a starting base salary of ~$25,792 even with 0 years of experience.

### 4. Evaluation Metrics
We evaluated the model's performance using four key metrics:

| Metric | Code Implementation | Explanation |
| :--- | :--- | :--- |
| **R² Score** | `r2_score(y_test, y_pred)` | Represents the **variance explained** by the model. $1.0$ is a perfect fit; $0.0$ is a baseline model. |
| **MAE** | `mean_absolute_error` | The average absolute difference between predicted and actual values. E.g., "The model is off by ~$45k on average." |
| **MSE** | `mean_squared_error` | Squaring the errors penalizes **large outliers** more heavily than small errors. |
| **RMSE** | `np.sqrt(mse)` | The square root of MSE. It brings the error unit back to the original unit (e.g., Dollars), making it easier to interpret than MSE. |

---

## 🛠️ Technologies & Libraries

* **Python 3.x**
* **Pandas:** Data manipulation, cleaning, and `.read_csv`.
* **NumPy:** Numerical operations and array reshaping.
* **Matplotlib:** Visualization (Scatter plots and Regression Lines).
* **Scikit-Learn:** Model training (`LinearRegression`) and metrics (`mean_absolute_error`, `r2_score`).
 