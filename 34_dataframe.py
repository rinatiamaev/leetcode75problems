# Reshape Data: Concatenate 

# DataFrame df1
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# DataFrame df2
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# Write a solution to concatenate these two DataFrames vertically into one DataFrame.

# The result format is in the following example.

 

# Example 1:

# Input:
# df1
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 1          | Mason   | 8   |
# | 2          | Ava     | 6   |
# | 3          | Taylor  | 15  |
# | 4          | Georgia | 17  |
# +------------+---------+-----+
# df2
# +------------+------+-----+
# | student_id | name | age |
# +------------+------+-----+
# | 5          | Leo  | 7   |
# | 6          | Alex | 7   |
# +------------+------+-----+
# Output:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 1          | Mason   | 8   |
# | 2          | Ava     | 6   |
# | 3          | Taylor  | 15  |
# | 4          | Georgia | 17  |
# | 5          | Leo     | 7   |
# | 6          | Alex    | 7   |
# +------------+---------+-----+
# Explanation:
# The two DataFramess are stacked vertically, and their rows are combined.

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:

    vertical_concat = pd.concat([df1, df2], axis=0)   
    # horizontal_concat = pd.concat([df1, df2], axis=1)
    print(vertical_concat)

    return(vertical_concat)

# columns = ["student_id", "age"]
student_data1 = pd.DataFrame([[1, 15], [2, 11], [3, 11], [4, 20]], columns = ["student_id", "age"])
student_data2 = pd.DataFrame([[5, 12], [6, 11], [7, 9], [8, 20]], columns = ["student_id", "age"])

concatenateTables(student_data1, student_data2)

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivoted_df = weather.pivot(index='month', columns='city', values='temperature')
    return pivoted_df

data = {
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville',
             'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May',
              'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}

weather = pd.DataFrame(data)
result = pivotTable(weather)

# Print without the index
print(result)


# Reshape Data: Melt
# 
# DataFrame report
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | product     | object |
# | quarter_1   | int    |
# | quarter_2   | int    |
# | quarter_3   | int    |
# | quarter_4   | int    |
# +-------------+--------+
# Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.

# The result format is in the following example.

 

# Example 1:

# Input:
# +-------------+-----------+-----------+-----------+-----------+
# | product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
# +-------------+-----------+-----------+-----------+-----------+
# | Umbrella    | 417       | 224       | 379       | 611       |
# | SleepingBag | 800       | 936       | 93        | 875       |
# +-------------+-----------+-----------+-----------+-----------+
# Output:
# +-------------+-----------+-------+
# | product     | quarter   | sales |
# +-------------+-----------+-------+
# | Umbrella    | quarter_1 | 417   |
# | SleepingBag | quarter_1 | 800   |
# | Umbrella    | quarter_2 | 224   |
# | SleepingBag | quarter_2 | 936   |
# | Umbrella    | quarter_3 | 379   |
# | SleepingBag | quarter_3 | 93    |
# | Umbrella    | quarter_4 | 611   |
# | SleepingBag | quarter_4 | 875   |
# +-------------+-----------+-------+
# Explanation:
# The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.

def meltTable(report: pd.DataFrame) -> pd.DataFrame:

    reshaped_df = report.melt(id_vars=['product'], var_name='quarter', value_name='sales')

    
    return reshaped_df

# Method Chaining

# DataFrame animals
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | species     | object |
# | age         | int    |
# | weight      | int    |
# +-------------+--------+
# Write a solution to list the names of animals that weigh strictly more than 100 kilograms.

# Return the animals sorted by weight in descending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# DataFrame animals:
# +----------+---------+-----+--------+
# | name     | species | age | weight |
# +----------+---------+-----+--------+
# | Tatiana  | Snake   | 98  | 464    |
# | Khaled   | Giraffe | 50  | 41     |
# | Alex     | Leopard | 6   | 328    |
# | Jonathan | Monkey  | 45  | 463    |
# | Stefan   | Bear    | 100 | 50     |
# | Tommy    | Panda   | 26  | 349    |
# +----------+---------+-----+--------+
# Output: 
# +----------+
# | name     |
# +----------+
# | Tatiana  |
# | Jonathan |
# | Tommy    |
# | Alex     |
# +----------+
# Explanation: 
# All animals weighing more than 100 should be included in the results table.
# Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
# The results should be sorted in descending order of weight.
 

# In Pandas, method chaining enables us to perform operations on a DataFrame without breaking up each operation into a separate line or creating multiple temporary variables. 

# Can you complete this task in just one line of code using method chaining?


import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    
    return animals[animals["weight"] > 100].sort_values("weight", ascending=False)[["name"]]
    
animals = pd.DataFrame({
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
})

# Print the DataFrame
print(animals)
print(findHeavyAnimals(animals))