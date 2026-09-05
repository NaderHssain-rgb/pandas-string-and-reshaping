# Pandas String and Reshaping

A beginner-friendly Pandas practice project covering string operations and different techniques for reshaping and transforming DataFrames.

## 📌 Project Overview

This project demonstrates several useful Pandas operations for working with text data and changing the structure of DataFrames.

The practice covers:

* String operations with `.str`
* Converting strings to uppercase
* Converting strings to lowercase
* Searching for text with `str.contains()`
* Reshaping data with `melt()`
* Reshaping data with `pivot()`
* Creating pivot tables with `pivot_table()`
* Converting columns into rows with `stack()`
* Converting stacked data back with `unstack()`

## 🛠️ Technologies Used

* Python
* Pandas

## 📂 Project Structure

```text
pandas-string-and-reshaping/
│
├── pandas_string_and_reshaping.py
├── requirements.txt
└── README.md
```

## 📚 Topics Covered

### 1. String Operations

Pandas provides the `.str` accessor for performing string operations on Series.

Example:

```python
df["name"].str.upper()
```

This converts text values to uppercase.

Another example:

```python
df["name"].str.lower()
```

This converts text values to lowercase.

### 2. `str.contains()`

The `str.contains()` method checks whether a string contains a specific pattern.

Example:

```python
df["gmail"].str.contains("@gmail.com")
```

The result is a Boolean Series containing `True` or `False`.

### 3. `melt()`

The `melt()` function converts a DataFrame from wide format to long format.

Example:

```python
pd.melt(
    df,
    id_vars="Student",
    value_vars=["Math", "Science"],
    var_name="Subject",
    value_name="Marks"
)
```

This is useful when data needs to be transformed into a structure that is easier to analyze.

### 4. `pivot()`

The `pivot()` method reshapes long-format data into a wider format.

Example:

```python
df.pivot(
    index="Student",
    columns="Subject",
    values="Marks"
)
```

It uses existing combinations of index and column values to reorganize the DataFrame.

### 5. `pivot_table()`

`pivot_table()` is similar to `pivot()`, but it supports aggregation functions.

Example:

```python
df.pivot_table(
    index="Student",
    columns="Subject",
    values="Marks",
    aggfunc="mean"
)
```

The `mean` function calculates the average when aggregation is required.

### 6. `stack()`

The `stack()` method moves columns into the index, creating a more hierarchical or long-format structure.

Example:

```python
df.set_index("Student").stack()
```

### 7. `unstack()`

The `unstack()` method performs the reverse type of reshaping by moving index levels back into columns.

Example:

```python
df.stack().unstack()
```

## 🔄 Data Reshaping Concept

A simple way to understand the main reshaping operations:

```text
Wide Data
   │
   │ melt()
   ▼
Long Data
   │
   │ pivot()
   ▼
Wide Data
```

And:

```text
Columns
   │
   │ stack()
   ▼
Index
   │
   │ unstack()
   ▼
Columns
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pandas-string-and-reshaping.git
```

### 2. Open the project folder

```bash
cd pandas-string-and-reshaping
```

### 3. Install the required library

```bash
pip install -r requirements.txt
```

### 4. Run the Python file

```bash
python pandas_string_and_reshaping.py
```

## 📖 What I Learned

Through this project, I practiced:

* Working with strings inside Pandas DataFrames
* Using the `.str` accessor
* Searching for patterns with `contains()`
* Converting wide data to long data
* Converting long data back to wide data
* Understanding `pivot()` and `pivot_table()`
* Using aggregation with `pivot_table()`
* Understanding `stack()` and `unstack()`
* Reshaping DataFrames for data analysis

## 🔮 Future Improvements

Possible improvements include:

* Working with real-world datasets
* Using regular expressions with string operations
* Handling missing values during reshaping
* Using multiple aggregation functions
* Combining reshaping with `groupby()`
* Exporting reshaped DataFrames to Excel and CSV
* Creating visualizations from the transformed data

## 👨‍💻 Author

Nader

## ⭐ Purpose

This repository is part of my Python and Data Analysis learning journey.

The goal is to practice Pandas step by step and build a strong foundation for future Data Analysis and Machine Learning projects.
