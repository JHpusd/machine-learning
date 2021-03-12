import sys
sys.path.append('src')
from dataframe import DataFrame
sys.path.append('kaggle/titanic')
from parse_line import *

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

path_to_datasets = '/home/runner/machine-learning/datasets/'
filename = 'airtravel.csv' 
filepath = path_to_datasets + filename
df = DataFrame.from_csv(filepath, True)

print("Testing from_csv method for dataframe...")
assert df.columns == ['"Month"', '"1958"', '"1959"', '"1960"']
assert df.to_array() == [[
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

df = DataFrame.from_array(
    [[0, 0, 1], 
    [1, 0, 2], 
    [2, 0, 4], 
    [4, 0, 8], 
    [6, 0, 9], 
    [0, 2, 2], 
    [0, 4, 5], 
    [0, 6, 7], 
    [0, 8, 6],
    [2, 2, 0],
    [3, 4, 0]],
    columns = ['beef', 'pb', 'rating']
)
df = df.create_interaction_terms('beef', 'pb')

assert df.columns == ['beef', 'pb', 'rating', 'beef * pb']

assert df.to_array() ==  [[0, 0, 1, 0], 
    [1, 0, 2, 0], 
    [2, 0, 4, 0], 
    [4, 0, 8, 0], 
    [6, 0, 9, 0], 
    [0, 2, 2, 0], 
    [0, 4, 5, 0], 
    [0, 6, 7, 0], 
    [0, 8, 6, 0],
    [2, 2, 0, 4],
    [3, 4, 0, 12]]

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

assert df.columns == ['beef', 'pb', 'mayo', 'jelly', 'rating']
assert df.to_array() == [[0, 0, 0, 0, 1],
[0, 0, 1, 0, 1],
[0, 0, 0, 1, 4],
[0, 0, 1, 1, 0],
[5, 0, 0, 0, 4],
[5, 0, 1, 0, 8],
[5, 0, 0, 1, 1],
[5, 0, 1, 1, 0],
[0, 5, 0, 0, 5],
[0, 5, 1, 0, 0],
[0, 5, 0, 1, 9],
[0, 5, 1, 1, 0],
[5, 5, 0, 0, 0],
[5, 5, 1, 0, 0],
[5, 5, 0, 1, 0],
[5, 5, 1, 1, 0]]
'''
path_to_datasets = '/home/runner/machine-learning/kaggle/titanic/data/'
filename = 'knowns.csv' 
filepath = path_to_datasets + filename
data_types = {
    "PassengerId": int,
    "Survived": int,
    "Pclass": int,
    "Name": str,
    "Sex": str,
    "Age": float,
    "SibSp": int,
    "Parch": int,
    "Ticket": str,
    "Fare": float,
    "Cabin": str,
    "Embarked": str
}
df = DataFrame.from_csv(filepath, True, data_types, parse_line)
assert df.columns == [
    'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
        'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
assert df.to_array()[:3] == [
    [1, 0, 3, '"Braund, Mr. Owen Harris"', "male", 22, 1, 0, "A/5 21171", 7.25, "", "S"],
        [2, 1, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', "female", 38, 1, 0, "PC 17599", 71.2833, "C85", "C"],
            [3, 1, 3, '"Heikkinen, Miss. Laina"', "female", 26, 0, 0, "STON/O2. 3101282", 7.925, "", "S"]]