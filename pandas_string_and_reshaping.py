import pandas as pd


# ============================================
# Pandas String Operations and Data Reshaping
# ============================================

# ============================================
# String Operations
# ============================================

# Create a DataFrame containing student names
df1 = pd.DataFrame({
    "name": ["Ali", "Ahmed", "Nader", "Abdallah", "Hala"]
})

print("Original Names:")
print(df1)

print("#" * 50)


# Convert names to uppercase
df1["upper"] = df1["name"].str.upper()

print("Uppercase Names:")
print(df1)

print("#" * 50)


# Convert names to lowercase
df1["lower"] = df1["name"].str.lower()

print("Lowercase Names:")
print(df1)

print("#" * 50)


# ============================================
# String Contains
# ============================================

# Create a DataFrame containing email-like values
df2 = pd.DataFrame({
    "gmail": [
        "Ali@gmail.com",
        "Ahmed@gmail.com",
        "Nader",
        "Abdallah",
        "Hala"
    ]
})

# Check whether each value contains "@gmail.com"
df2["is_gmail"] = df2["gmail"].str.contains("@gmail.com")

print("Gmail Check:")
print(df2)

print("#" * 50)


# ============================================
# Melt
# ============================================

# Create a DataFrame containing student marks
df3 = pd.DataFrame({
    "Student": ["A", "B"],
    "Math": [90, 95],
    "Science": [93, 89]
})

print("Original Student Data:")
print(df3)

print("#" * 50)


# Convert the DataFrame from wide format to long format
df3_melted = pd.melt(
    df3,
    id_vars="Student",
    value_vars=["Math", "Science"],
    var_name="Subject",
    value_name="Marks",
    ignore_index=False
)

print("Melted DataFrame:")
print(df3_melted)

print("#" * 50)


# ============================================
# Pivot
# ============================================

# Convert the melted DataFrame back to a wider format
df3_pivot = df3_melted.pivot(
    index="Student",
    columns="Subject",
    values="Marks"
)

print("Pivot DataFrame:")
print(df3_pivot)

print("#" * 50)


# ============================================
# Pivot Table
# ============================================

# Create a pivot table using the mean aggregation function
df_pivot_table = df3_melted.pivot_table(
    index="Student",
    columns="Subject",
    values="Marks",
    aggfunc="mean"
)

print("Pivot Table:")
print(df_pivot_table)

print("#" * 50)


# ============================================
# Stack
# ============================================

# Set Student as the index and stack the columns
df3_stack = df3.set_index("Student").stack()

print("Stacked DataFrame:")
print(df3_stack)

print("#" * 50)


# ============================================
# Unstack
# ============================================

# Convert the stacked data back to columns
df3_unstack = df3_stack.unstack()

print("Unstacked DataFrame:")
print(df3_unstack)