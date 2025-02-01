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