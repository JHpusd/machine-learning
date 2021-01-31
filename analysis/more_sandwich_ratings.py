import sys
sys.path.append('src')
from linear_regressor import *
from matrix import *
from dataframe import *
from logistic_regressor import *

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0],
    [5, 5, [],                0],
    [5, 5, ['mayo'],          0],
    [5, 5, ['jelly'],         0],
    [5, 5, ['mayo', 'jelly'], 0]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)

df = df.create_dummy_variables('condiments')

no_dv_cols = [col_name for col_name in df.columns]
no_dv_cols.remove('rating')

for a in range(len(no_dv_cols)):
    for b in range(len(no_dv_cols)):
        if a >= b:
            continue
        df = df.create_interaction_terms(no_dv_cols[a], no_dv_cols[b])

regressor = LinearRegressor(df, 'rating')
# print(regressor.coefficients)

no_zero_dict = {key:df.data_dict[key] for key in df.data_dict}
no_zero_dict['rating'] = [val if val != 0 else 0.1 for val in no_zero_dict['rating']]
no_zero_df = DataFrame(no_zero_dict, df.columns)

log_reg = LogisticRegressor(no_zero_df, 'rating', 10)
# print(log_reg.coefficients)

print(regressor.predict({
    'beef': 8,
    'pb': 0,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 0,
    'beef * mayo': 8,
    'beef * jelly': 0,
    'pb * mayo': 0,
    'pb * jelly': 0,
    'mayo * jelly': 0
}))
print(log_reg.predict({
    'beef': 8,
    'pb': 0,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 0,
    'beef * mayo': 8,
    'beef * jelly': 0,
    'pb * mayo': 0,
    'pb * jelly': 0,
    'mayo * jelly': 0
}))

print(regressor.predict({
    'beef': 0,
    'pb': 4,
    'mayo': 0,
    'jelly': 1,
    'beef * pb': 0,
    'beef * mayo': 0,
    'beef * jelly': 0,
    'pb * mayo': 0,
    'pb * jelly': 4,
    'mayo * jelly': 0
}))
print(log_reg.predict({
    'beef': 0,
    'pb': 4,
    'mayo': 0,
    'jelly': 1,
    'beef * pb': 0,
    'beef * mayo': 0,
    'beef * jelly': 0,
    'pb * mayo': 0,
    'pb * jelly': 4,
    'mayo * jelly': 0
}))

print(regressor.predict({
    'beef': 0,
    'pb': 4,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 0,
    'beef * mayo': 0,
    'beef * jelly': 0,
    'pb * mayo': 4,
    'pb * jelly': 0,
    'mayo * jelly': 0
}))
print(log_reg.predict({
    'beef': 0,
    'pb': 4,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 0,
    'beef * mayo': 0,
    'beef * jelly': 0,
    'pb * mayo': 4,
    'pb * jelly': 0,
    'mayo * jelly': 0
}))

print(regressor.predict({
    'beef': 8,
    'pb': 4,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 32,
    'beef * mayo': 8,
    'beef * jelly': 0,
    'pb * mayo': 4,
    'pb * jelly': 0,
    'mayo * jelly': 0
}))
print(log_reg.predict({
    'beef': 8,
    'pb': 4,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 32,
    'beef * mayo': 8,
    'beef * jelly': 0,
    'pb * mayo': 4,
    'pb * jelly': 0,
    'mayo * jelly': 0
}))

print(regressor.predict({
    'beef': 8,
    'pb': 0,
    'mayo': 1,
    'jelly': 1,
    'beef * pb': 0,
    'beef * mayo': 8,
    'beef * jelly': 8,
    'pb * mayo': 0,
    'pb * jelly': 0,
    'mayo * jelly': 1
}))
print(log_reg.predict({
    'beef': 8,
    'pb': 0,
    'mayo': 1,
    'jelly': 1,
    'beef * pb': 0,
    'beef * mayo': 8,
    'beef * jelly': 8,
    'pb * mayo': 0,
    'pb * jelly': 0,
    'mayo * jelly': 1
}))

