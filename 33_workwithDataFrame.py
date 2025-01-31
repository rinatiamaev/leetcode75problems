# Display the First Three Rows

# DataFrame: employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+
# Write a solution to display the first 3 rows of this DataFrame.

 

# Example 1:

# Input:
# DataFrame employees
# +-------------+-----------+-----------------------+--------+
# | employee_id | name      | department            | salary |
# +-------------+-----------+-----------------------+--------+
# | 3           | Bob       | Operations            | 48675  |
# | 90          | Alice     | Sales                 | 11096  |
# | 9           | Tatiana   | Engineering           | 33805  |
# | 60          | Annabelle | InformationTechnology | 37678  |
# | 49          | Jonathan  | HumanResources        | 23793  |
# | 43          | Khaled    | Administration        | 40454  |
# +-------------+-----------+-----------------------+--------+
# Output:
# +-------------+---------+-------------+--------+
# | employee_id | name    | department  | salary |
# +-------------+---------+-------------+--------+
# | 3           | Bob     | Operations  | 48675  |
# | 90          | Alice   | Sales       | 11096  |
# | 9           | Tatiana | Engineering | 33805  |
# +-------------+---------+-------------+--------+
# Explanation: 
# Only the first 3 rows are displayed.

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.head(3)
    return df

# Select Data
# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# Write a solution to select the name and age of the student with student_id = 101.

# The result format is in the following example.

 

# Example 1:
# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 101        | Ulysses | 13  |
# | 53         | William | 10  |
# | 128        | Henry   | 6   |
# | 3          | Henry   | 11  |
# +------------+---------+-----+
# Output:
# +---------+-----+
# | name    | age | 
# +---------+-----+
# | Ulysses | 13  |
# +---------+-----+
# Explanation:
# Student Ulysses has student_id = 101, we select the name and age.

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = students.loc[students["student_id"] == 101, ["name", "age"]]
    return df

#Create a New Column Create a New Column

# DataFrame employees
# +-------------+--------+
# | Column Name | Type.  |
# +-------------+--------+
# | name        | object |
# | salary      | int.   |
# +-------------+--------+
# A company plans to provide its employees with a bonus.

# Write a solution to create a new column name bonus that contains the doubled values of the salary column.

# The result format is in the following example.

 

# Example 1:

# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Piper   | 4548   |
# | Grace   | 28150  |
# | Georgia | 1103   |
# | Willow  | 6593   |
# | Finn    | 74576  |
# | Thomas  | 24433  |
# +---------+--------+
# Output:
# +---------+--------+--------+
# | name    | salary | bonus  |
# +---------+--------+--------+
# | Piper   | 4548   | 9096   |
# | Grace   | 28150  | 56300  |
# | Georgia | 1103   | 2206   |
# | Willow  | 6593   | 13186  |
# | Finn    | 74576  | 149152 |
# | Thomas  | 24433  | 48866  |
# +---------+--------+--------+
# Explanation: 
# # A new column bonus is created by doubling the value in the column salary.

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees

# Drop Duplicate Rows

# DataFrame customers
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | customer_id | int    |
# | name        | object |
# | email       | object |
# +-------------+--------+
# There are some duplicate rows in the DataFrame based on the email column.

# Write a solution to remove these duplicate rows and keep only the first occurrence.

# The result format is in the following example.

 

# Example 1:
# Input:
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 5           | Finn    | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+
# Output:  
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+
# Explanation:
# Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.


import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    new_cust = customers.drop_duplicates(subset=["email"])
    return new_cust

#  Drop Missing Data
# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# There are some rows having missing values in the name column.

# Write a solution to remove the rows with missing values.

# The result format is in the following example.

 

# Example 1:

# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 217        | None    | 19  |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# +------------+---------+-----+
# Output:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 779        | Georgia | 20  | 
# | 849        | Willow  | 14  | 
# +------------+---------+-----+
# Explanation: 
# Student with id 217 havs empty value in the name column, so it will be removed.

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    newDF = students.dropna()
    return newDF 