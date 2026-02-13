# Building Permits: Data Cleaning & Preprocessing Pipeline

This project demonstrates a comprehensive data science workflow for cleaning, transforming, and analyzing raw building permit data. It covers everything from initial encoding detection to advanced fuzzy string matching.

---

## 🛠 Project Workflow

### 1. Encoding Detection
To avoid `UnicodeDecodeError`, we use `charset_normalizer` to detect the file's character encoding before loading it into a Pandas DataFrame.
* **Tool**: `charset_normalizer`
* **Goal**: Identify if the file is UTF-8, Windows-1252, or another format.

### 2. Missing Data Analysis
We quantify the "completeness" of the dataset by calculating the percentage of missing values.
* **Technique**: `isnull().sum()` to find nulls per column.
* **Remediation**: 
    * **Dropping**: Removing columns with at least one null (`axis=1`).
    * **Imputation**: Using `.bfill()` (backfilling) to propagate next-valid values, followed by `.fillna(0)` to catch remaining gaps.



### 3. Scaling vs. Normalization
This step prepares numerical data for statistical analysis or machine learning models.

* **Scaling (Min-Max)**: Changes the **range** of your data (e.g., to 0-1) while keeping the distribution shape identical.
* **Normalization (Box-Cox)**: Changes the **shape** of the distribution to make it look like a Normal (Gaussian) distribution.



### 4. Date Parsing
Dates stored as strings are converted into Python `datetime` objects to allow for time-based calculations.
* **Logic**: Converting formats like `MM/DD/YYYY` into standardized objects.
* **Visualization**: Using `sns.displot` with `kde=True` to overlay histograms and density lines to compare "Issued" vs "Completed" permit trends.

### 5. Cleaning Text Inconsistency
Categorical data (like neighborhood names) often contains typos or inconsistent casing.
* **Normalization**: Applying `.str.lower()` and `.str.strip()`.
* **Fuzzy Matching**: Using the `fuzzywuzzy` library to detect strings with high similarity (Levenshtein distance) and merging duplicates.

---

## 🚀 Getting Started

### Prerequisites
You will need Python installed along with the following libraries:
```bash
pip install pandas numpy charset-normalizer fuzzywuzzy mlxtend seaborn scipy matplotlib
```

### Function - Purpose

1. pd.to_datetime(),Converts strings to date objects
2. stats.boxcox(),Normalizes skewed data
3. minmax_scaling(),Rescales data to a fixed range (0 to 1)
4. fuzzywuzzy.process,Identifies similar text strings