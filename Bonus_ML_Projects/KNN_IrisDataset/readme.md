# Iris Species Classification using K-Nearest Neighbors (KNN)

This project implements a **K-Nearest Neighbors (KNN)** classifier to predict the variety of Iris flowers based on physical measurements. It includes data preprocessing, normalization, and an iterative process to find the optimal value of  for maximum accuracy.

---

## 🛠️ Implementation Steps

### 1. Data Encoding and Preparation

The `variety` column (target variable) contains categorical strings (e.g., *Setosa*, *Versicolor*). These are converted into numerical labels using **Label Encoding**.

* **Features ():** Sepal length, Sepal width, Petal length, Petal width.
* **Target ():** Encoded species categories.

### 2. Train-Test Split

The dataset is split into 80% training data and 20% testing data. This ensures the model is evaluated on "unseen" data to check for overfitting.

### 3. Data Normalization

Standardization is applied using `StandardScaler`. This is a crucial step for KNN because the algorithm calculates the distance between points (Euclidean distance).

* **Formula:** 
* **Effect:** Scales all features so they have a mean of 0 and a standard deviation of 1, preventing features with larger numerical ranges from dominating the distance calculation.

### 4. KNN Training & Optimization

The model is initially trained with . Subsequently, a loop iterates through  values from 1 to 119 to identify the **"Best K"**—the value that yields the highest accuracy on the test set.

---

## 📈 Key Learnings

### Why Normalize?

KNN is a **distance-based algorithm**. If one feature (like Sepal Length) ranges from 1–10 and another (like Petal Area) ranges from 100–1000, the distance calculation would be almost entirely driven by the larger numbers. Normalization puts them on an equal playing field.

### The Role of 'K'

* **Small K (e.g., K=1):** The model is sensitive to noise and outliers. This often leads to **Overfitting**, where the model learns the training data perfectly but fails on new data.
* **Large K (e.g., K=100):** The model becomes too "blunt." It considers too many neighbors, leading to **Underfitting**, where it ignores local patterns in the data.

### Evaluation Metrics

We use `accuracy_score` to compare the predicted species () against the actual labels ().

> **Note:** In this project, the best  value is determined by the highest accuracy achieved on the test set, ensuring the model generalizes well to new samples.

---
 