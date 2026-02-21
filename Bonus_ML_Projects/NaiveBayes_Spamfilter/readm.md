## Spam Classification via Naive Bayes and TF-IDF

This project implements a text classification pipeline to identify spam messages using Bayesian probability and Scikit-Learn.

---

### Core Learning Objectives

#### 1. Bayesian Probability Foundations

The manual implementation demonstrates the **Naive Bayes** approach by calculating individual word "spamicity" based on historical frequency.

* **Prior Probability:** The baseline likelihood of an email being spam  or ham  before analyzing its content.
* **Likelihood:** The probability of a specific word appearing given the class (e.g., ).
* **Laplace Smoothing:** The code uses `(emails_with_spam + 1) / (total_spam + 2)`. This  (additive smoothing) prevents a probability of zero if a word from the test set was never seen during training, which would otherwise nullify the entire calculation.

#### 2. Feature Engineering: TF-IDF

While the manual steps use raw word counts, the Scikit-Learn implementation utilizes **Term Frequency-Inverse Document Frequency (TF-IDF)**.

* **TF (Term Frequency):** Measures how frequently a term occurs in a document.
* **IDF (Inverse Document Frequency):** Reduces the weight of terms that appear very frequently across all documents (like "the", "is"), ensuring unique, meaningful words have higher influence.

#### 3. Scikit-Learn Pipeline Architecture

The `Pipeline` object encapsulates the entire workflow:

1. **Vectorizer:** Transforms raw text strings into numerical TF-IDF vectors.
2. **Classifier:** Applies the `MultinomialNB` algorithm to these vectors.

* **Benefit:** Ensures that the same transformations applied to the training data are consistently applied to the test data, preventing data leakage.

---

### Implementation Summary

| Component | Description |
| --- | --- |
| **Data Split** | 80/20 train-test split using `train_test_split`. |
| **Preprocessing** | Basic normalization (lowercasing) via a custom `process` function. |
| **Model** | `MultinomialNB`, ideal for discrete features like word counts or TF-IDF scores. |
| **Evaluation** | Utilizes a **Confusion Matrix** to track four key outcomes: |

* **True Positives (TP):** Spam correctly identified as spam.
* **True Negatives (TN):** Normal mail (ham) correctly identified as ham.
* **False Positives (FP):** Ham mistakenly flagged as spam (Type I Error).
* **False Negatives (FN):** Spam that reached the inbox (Type II Error).

---

### Operational Results

The model's performance is quantified by comparing `y_test` (actual labels) against `predictions`. The resulting confusion matrix provides a granular view of model reliability beyond simple accuracy scores.