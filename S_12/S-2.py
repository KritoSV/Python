# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" 
# в зоне минимального значения переменной "population" 
# и сохраните это значение в переменную max_households_in_min_population.
# Используйте модуль pandas.

# ЭТАНОЛ
import pandas as pd

df = pd.read_csv('california_housing_train.csv')
# Найти минимальное значение 'population'
min_population = df['population'].min()

# Отфильтровать строки с минимальным значением 'population' и найти максимальное значение 'households'
max_households_in_min_population = df[df['population'] == min_population]['households'].max()

# Решение 1

import pandas as pd

df = pd.read_csv('california_housing_train.csv')

# Фильтрация строк с минимальным значением 'population'
filtered_df = df[df['population'] == df['population'].min()]

# Найти максимальное значение 'households' в отфильтрованном DataFrame
max_households_in_min_population = filtered_df['households'].max()
max_households_in_min_population
