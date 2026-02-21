## Support Vector Machine (SVM) Overview

The Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression. In the context of binary classification, the algorithm identifies the **Optimal Hyperplane** that separates data points of different classes with the maximum margin.

### Core Mechanics

* **Hyperplane:** A decision boundary that segregates the feature space. For  features, the hyperplane is an  dimensional subspace.
* **Support Vectors:** The data points located closest to the decision boundary. These points are critical; removing them would change the position of the hyperplane.
* **Margin:** The distance between the hyperplane and the nearest support vectors from either class. SVM maximizes this distance to improve generalization.
* **Kernel Trick:** For non-linearly separable data, SVM uses kernel functions to project data into a higher-dimensional space where a linear separation becomes possible.

---

### Implementation Process

1. **Data Preparation:** The Scikit-learn `load_breast_cancer` dataset is converted into a structured DataFrame. Features (measurements) are isolated from the target (malignant vs. benign).
2. **Splitting:** `train_test_split` reserves 20% of the data to validate model performance on unseen inputs.
3. **Optimization:** The `SVC` model fits the training data by solving a constrained quadratic optimization problem to find the weights that maximize the margin.
4. **Prediction:** The model assigns classes based on which side of the hyperplane the test points fall.

---

### Performance Metrics

The success of an SVM model is evaluated via a **Confusion Matrix**, which categorizes predictions into four states:

| Metric | Definition |
| --- | --- |
| **True Negative (TN)** | Correctly predicted the negative class. |
| **True Positive (TP)** | Correctly predicted the positive class. |
| **False Positive (FP)** | Incorrectly predicted positive (Type I error). |
| **False Negative (FN)** | Incorrectly predicted negative (Type II error). |

The **Classification Report** further derives:

* **Precision:**  (Accuracy of positive predictions)
* **Recall:**  (Ability to find all positive instances)
* **F1-Score:** Harmonic mean of Precision and Recall.