import sys
sys.path.append('src')
from dataframe import DataFrame

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}
'''
df1 = DataFrame(data_dict, ['Pete', 'John', 'Sarah'])

print("Testing class DataFrame ...")

assert df1.data_dict == {'Pete': [1, 0, 1, 0],'John': [2, 1, 0, 2],'Sarah': [3, 1, 4, 0]}
assert df1.columns == ['Pete', 'John', 'Sarah']
assert df1.to_array() == [[1, 2, 3], [0, 1, 1], [1, 0, 4], [0, 2, 0]]

df2 = df1.select_columns(['Sarah', 'Pete'])
assert df2.to_array() == [[3, 1], [1, 0], [4, 1], [0, 0]]
assert df2.columns == ['Sarah', 'Pete']

df3 = df1.select_rows([1, 3])
assert df3.to_array() == [[0, 1, 1], [0, 2, 0]]
print("PASSED")

print("Testing method 'apply'...")

def lambda_x(x):
    return 7 * x

df2 = df1.apply('John', lambda_x)
assert df2.data_dict == { 'Pete': [1, 0, 1, 0],
    'John': [14, 7, 0, 14],
    'Sarah': [3, 1, 4, 0]
}
print("PASSED")

print("Testing classmethod 'from_array' and new selection methods...")
columns = ['firstname', 'lastname', 'age']
arr = [['Kevin', 'Fray', 5],['Charles', 'Trapp', 17],[
    'Anna', 'Smith', 13],['Sylvia', 'Mendez', 9]]

df = DataFrame.from_array(arr, columns)

assert df.select_rows_where(lambda row: len(row['firstname']) >= len(row['lastname']) and row['age'] > 10).to_array() == [['Charles', 'Trapp', 17]]

assert df.order_by('age', True).to_array() == [['Kevin', 'Fray', 5],[
    'Sylvia', 'Mendez', 9],['Anna', 'Smith', 13],['Charles', 'Trapp', 17]]
assert df.order_by('firstname', False).to_array() == [
    ['Sylvia', 'Mendez', 9],['Kevin', 'Fray', 5],[
        'Charles', 'Trapp', 17],['Anna', 'Smith', 13]]
print("PASSED")
'''
path_to_datasets = '/home/runner/machine-learning/datasets/'
filename = 'airtravel.csv' 
filepath = path_to_datasets + filename
df = DataFrame.from_csv(filepath, True)

print("Testing from_csv method for dataframe...")
assert df.to_array() == [['"Month"', '"1958"', '"1959"', '"1960"'],[
    '"JAN"', '340', '360', '417'],[
        '"FEB"', '318', '342', '391'],[
            '"MAR"', '362', '406', '419'],[
                '"APR"', '348', '396', '461'],[
                    '"MAY"', '363', '420', '472'],[
                        '"JUN"', '435', '472', '535'],[
                            '"JUL"', '491', '548', '622'],[
                                '"AUG"', '505', '559', '606'],[
                                    '"SEP"', '404', '463', '508'],[
                                        '"OCT"', '359', '407', '461'],[
                                            '"NOV"', '310', '362', '390'],[
                                                '"DEC"', '337', '405', '432']]
print("PASSED")
