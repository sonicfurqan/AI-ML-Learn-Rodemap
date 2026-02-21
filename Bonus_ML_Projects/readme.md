# Machine Learning Algorithm Mastery
- **Objective:** Master 11 core ML algorithms through implementation and project-based validation.
- **Inspired By:** [Video from Infinite Codes](https://www.youtube.com/watch?v=E0Hmnixke2g&t=139s)
- **Scoring Parameters** [Learn about model scoring](https://www.datasource.ai/en/data-science-articles/model-evaluation-metrics-in-machine-learning)


---

## Phase 1: Foundations & Regression

### 1. Linear Regression
- **Theory:** [A Beginner's Guide to Linear Regression](https://www.datasource.ai/en/data-science-articles/a-beginner-s-guide-to-linear-regression-in-python-with-scikit-learn)
- [Explanation of Linear Regression][https://www.youtube.com/watch?v=3bvM3NyMiE0]
- **Project:** Salary Predictor (Dataset: YearsExperience vs Salary)
- **Acceptance Criteria:**
  - Calculate and print Slope (Coefficient) and Intercept.
  - Plot data points with the Regression Line overlay.
  - Predict salary for 12 years of experience.

---

## Phase 2: Basic Classification

### 2. Logistic Regression
- **Theory:** [Titanic: Logistic Regression with Python](https://www.kaggle.com/code/mnassrib/titanic-logistic-regression-with-python)
- **Project:** Titanic Survivor Predictor (Dataset: Titanic)
- **Acceptance Criteria:**
  - Handle missing values in `Age`.
  - Encode `Sex` to numerical values.
  - Generate Confusion Matrix (TP, TN, FP, FN).

### 3. K-Nearest Neighbors (KNN)
- **Theory:** [KNN on Iris Dataset](https://medium.com/@timnik/k-nearest-neighbors-algorithm-on-iris-dataset-with-python-a6ac757c264b)
- **Project:** Iris Species Classifier (Dataset: Iris)
- **Acceptance Criteria:**
  - Split data 80/20 (Train/Test).
  - Compare accuracy of K=3 vs K=10.
  - Predict species for custom input `[5.1, 3.5, 1.4, 0.2]`.

### 4. Naive Bayes
- **Theory:** [Naive Bayes Spam Filter](https://medium.com/data-science/na%C3%AFve-bayes-spam-filter-from-scratch-12970ad3dae7)[Kaggle Link](https://www.kaggle.com/code/jeffysonar/spam-filter-using-naive-bayes-classifier/input)
- **Project:** SMS Spam Filter (Dataset: SMS Spam Collection)
- **Acceptance Criteria:**
  - Implement `CountVectorizer` (Bag of Words).
  - Use `MultinomialNB`.
  - Correctly classify "Win a free iPhone now!" as Spam.

### 5. Support Vector Machine (SVM)
- **Theory:** [Breast Cancer Classification using SVM](https://analyticseducator.com/Blog/Cancer-Classification-Support-Vector-Machines.html)
- **Project:** Tumor Classifier (Dataset: Breast Cancer Wisconsin)
- **Acceptance Criteria:**
  - Print Classification Report (Precision, Recall, F1).
  - Achieve >90% accuracy on test set.
  - Document the definition of "Margin" in code comments.

---

## Phase 3: Tree-Based & Ensemble Methods

### 6. Decision Trees
- **Theory:** [Loan Status Prediction](https://www.analyticsvidhya.com/blog/2022/05/loan-prediction-problem-from-scratch-to-end/)
- **Project:** Loan Approval System (Dataset: Loan Prediction)
- **Acceptance Criteria:**
  - Visualize tree structure (Graphviz/plot_tree).
  - Identify Root Node feature.
  - Limit tree depth to 3 and visualize.

### 7. Random Forest
- **Theory:** [Fraud Detection using Random Forest](https://www.kaggle.com/code/haiderkraheem/fraud-detection-using-random-forest-classifier)
- **Project:** Fraud Detector (Dataset: Credit Card Fraud)
- **Acceptance Criteria:**
  - Train `RandomForestClassifier` (n_estimators=100).
  - Compare accuracy against single Decision Tree.
  - Plot Feature Importance graph.

### 8. Boosting (XGBoost)
- **Theory:** [Churn Prediction with XGBoost](https://medium.com/@seun.ashaka/churn-prediction-with-xgboost-699da9086bae)
- **Project:** Customer Churn Predictor (Dataset: Telco Customer Churn)
- **Acceptance Criteria:**
  - Encode categorical variables.
  - Train `XGBClassifier`.
  - Achieve ROC-AUC score > 0.80.

---

## Phase 4: Neural Networks

### 9. Neural Networks
- **Theory:** [PyTorch CNN Tutorial](https://www.datacamp.com/tutorial/pytorch-cnn-tutorial) / [TensorFlow MNIST](https://www.tensorflow.org/tutorials/quickstart/beginner)
- **Project:** Digit Recognizer (Dataset: MNIST)
- **Acceptance Criteria:**
  - Architecture: Input -> Hidden Layer -> Output (10 nodes).
  - Train 5 epochs; track Loss decrease.
  - Visualize 5 test images with model predictions.

---

## Phase 5: Unsupervised Learning

### 10. K-Means Clustering
- **Theory:** [K-Means for Customer Segmentation](https://www.kaggle.com/code/ranasabrii/k-means-clustering-for-customer-segmentation)
- **Project:** Customer Segmentation (Dataset: Mall Customers)
- **Acceptance Criteria:**
  - Use Elbow Method to find optimal K.
  - Train with optimal K.
  - Plot clusters (Color by assignment).

### 11. Principal Component Analysis (PCA)
- **Theory:** [PCA for Data Visualization](https://builtin.com/machine-learning/pca-in-python)
- **Project:** Dataset Visualizer (Dataset: MNIST/Iris)
- **Acceptance Criteria:**
  - Standardize data (Mean=0, Var=1).
  - Reduce to 2 Principal Components.
  - Plot 2D scatter with label coloring.