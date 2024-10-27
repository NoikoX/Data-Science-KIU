import pandas as pd
import numpy as np

# :DD
def task1(df):
    combinations = df.groupby(['Category1', 'Category2', 'Category3']).size().reset_index(name='Count')
    result = combinations[combinations['Count'] >= 10]
    return result

def task2(df):
    missing_percentage = df.isna().mean()
    top_3_columns = missing_percentage.nlargest(3).index
    df_cleaned = df.dropna(subset=top_3_columns)
    return df_cleaned

#  we not use mode :DD
def task3(df):
    most_frequent = df.apply(lambda x: x.value_counts().idxmax()) # i hope that works correct
    return most_frequent

#hree I find who worked 5 days in a row
def task4(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by=['Employee ID', 'Date'])
    df['consecutive'] = df.groupby('Employee ID')['Date'].diff().dt.days.eq(1).groupby(df['Employee ID']).cumsum()
    consecutive_employees = df[df.groupby('Employee ID')['consecutive'].transform('size') >= 5]
    return consecutive_employees

# justt resample to monthly and first quarter only :
def task5(df):
    df.index = pd.to_datetime(df.index)
    df_q1 = df[df.index.month.isin([1, 2, 3])].resample('ME').sum()
    return df_q1


def task6(df, column):
    threshold = df[column].quantile(0.95)
    df_filtered = df[df[column] <= threshold]
    return df_filtered

def task7(df, window):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date').sort_index()
    rolling_avg = df['Value'].rolling(window=window, min_periods=1).mean()
    return rolling_avg

# cumulative sum exceed threshold
def task8(df, column, threshold):
    df['cumsum'] = df[column].cumsum()
    first_exceed = df[df['cumsum'] > threshold].iloc[0]
    return first_exceed

def task9(df):
    max_values = df.loc[df.groupby('Category')['Value'].idxmax()]
    return max_values

def task10(df, column):
    json_df = pd.json_normalize(df[column])
    df_flattened = df.drop(columns=[column]).join(json_df)
    return df_flattened

# heree are generated random dataframess
df1 = pd.DataFrame({
    'Category1': ['A', 'B', 'A', 'A', 'C', 'B', 'A', 'A', 'B', 'C', 'A', 'B', 'A'],
    'Category2': ['X', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'X', 'X', 'Y', 'Y'],
    'Category3': ['Z', 'Z', 'Z', 'Z', 'Y', 'Z', 'Y', 'Z', 'Y', 'Y', 'Z', 'Z', 'Z']
})

df2 = pd.DataFrame({
    'A': [1, 2, None, None],
    'B': [None, None, 3, 4],
    'C': [5, None, None, 6],
    'D': [7, 8, 9, 10]
})

df3 = pd.DataFrame({
    'A': [1, 2, 2, 3, 4],
    'B': [2, 3, 3, 4, 5],
    'C': [1, 1, 2, 3, 3]
})

df4 = pd.DataFrame({
    'Employee ID': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
    'Date': pd.date_range('2023-01-01', periods=10, freq='D'),
    'Hours Worked': [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
})

df5 = pd.DataFrame({
    'Date': pd.date_range('2023-01-01', periods=10, freq='D'),
    'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}).set_index('Date')

df6 = pd.DataFrame({
    'Transaction ID': range(1, 101),
    'Value': np.random.rand(100) * 1000
})

df7 = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-03', '2023-01-06', '2023-01-10'],
    'Value': [10, 30, 20, 40]
})

df8 = pd.DataFrame({
    'Transaction ID': range(1, 101),
    'Value': np.random.rand(100) * 1000
})

df9 = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C'],
    'Value': [10, 20, 30, 25, 15]
})

df10 = pd.DataFrame({
    'ID': [1, 2],
    'Data': [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
})


print(task1(df1))
print(task2(df2))
print(task3(df3))
print(task4(df4))
print(task5(df5))
print(task6(df6, 'Value'))
print(task7(df7, window=2))
print(task8(df8, 'Value', 500))
print(task9(df9))
print(task10(df10, 'Data'))
