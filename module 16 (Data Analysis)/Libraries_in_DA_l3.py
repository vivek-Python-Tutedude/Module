"""
# Python Libraries - Simple Notes

## What is a Library?

A **library** is a collection of pre-written code that helps programmers perform tasks easily without writing everything from scratch.

---

# 1. Scientific Computing Libraries

These libraries are used for data analysis, mathematical calculations, and scientific computing.

## A) Pandas
- Used for data analysis and data manipulation.
- Works with tables called **DataFrames**.
- Can read and write CSV, Excel, JSON, etc.

### Import
```python
import pandas as pd
```

### Uses
- Read CSV/Excel files
- Clean data
- Filter data
- Analyze data

---

## B) NumPy
- Used for numerical and mathematical calculations.
- Works with arrays.
- Faster than normal Python lists.

### Import
```python
import numpy as np
```

### Uses
- Arrays
- Matrix operations
- Mathematical calculations

---

## C) SciPy
- Used for scientific and engineering calculations.
- Built on NumPy.
- Provides statistical and optimization functions.

### Import
```python
import scipy
```

### Uses
- Statistics
- Optimization
- Scientific calculations

---

# 2. Visualization Libraries

These libraries are used to create graphs and charts.

## A) Matplotlib
- Used to create graphs and charts.
- Most commonly used visualization library.

### Import
```python
import matplotlib.pyplot as plt
```

### Types of Charts
- Line Chart
- Bar Chart
- Pie Chart
- Histogram
- Scatter Plot

---

## B) Seaborn
- Used to create attractive statistical graphs.
- Built on Matplotlib.
- Requires less code than Matplotlib.

### Import
```python
import seaborn as sns
```

### Uses
- Statistical graphs
- Heatmaps
- Distribution plots
- Box plots

---

# 3. Algorithmic Libraries

These libraries are mainly used in Machine Learning and Statistics.

## A) Scikit-learn
- Used for Machine Learning.
- Provides ready-made ML algorithms.

### Import
```python
from sklearn import datasets
```

### Uses
- Classification
- Regression
- Clustering
- Model Evaluation

---

## B) Statsmodels
- Used for statistical analysis.
- Performs regression and hypothesis testing.

### Import
```python
import statsmodels.api as sm
```

### Uses
- Regression Analysis
- Time Series Analysis
- Statistical Tests

---

# Two Important Properties

## 1. File Format

A **file format** tells Python what type of file is being used.

### Examples
- `.csv` → Comma Separated Values
- `.xlsx` → Excel File
- `.json` → JSON File
- `.hdf` → Hierarchical Data Format

### Example
```
students.csv
employees.xlsx
data.json
```

---

## 2. File Path

A **file path** tells Python where the file is stored on the computer.

### Example
```
C:/Desktop/My Files/mydata.csv
```

### Parts of File Path
- **C:** → Drive
- **Desktop** → Folder
- **My Files** → Subfolder
- **mydata.csv** → File Name

---

# Quick Revision (Exam Notes)

## Scientific Computing Libraries
- **Pandas** → Data Analysis & Data Manipulation
- **NumPy** → Numerical Calculations & Arrays
- **SciPy** → Scientific & Mathematical Computing

## Visualization Libraries
- **Matplotlib** → Basic Graphs and Charts
- **Seaborn** → Attractive Statistical Graphs

## Algorithmic Libraries
- **Scikit-learn** → Machine Learning Algorithms
- **Statsmodels** → Statistical Analysis

## Important Properties
- **File Format** → Type of file (.csv, .xlsx, .json, .hdf)
- **File Path** → Location of the file in the computer

---

# One-Line Memory Trick

- **Pandas** → Analyze Data
- **NumPy** → Numbers & Arrays
- **SciPy** → Scientific Mathematics
- **Matplotlib** → Draw Graphs
- **Seaborn** → Beautiful Graphs
- **Scikit-learn** → Machine Learning
- **Statsmodels** → Statistics
- **File Format** → Type of File
- **File Path** → Location of File
"""