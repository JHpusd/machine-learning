import sys
sys.path.append('src')
from dataframe import DataFrame
sys.path.append('kaggle/titanic')
from parse_line import *

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

# getting surname
name_index = df.columns.index('Name')
surnames = []
for name in df.data_dict['Name']:
    surnames.append(name.split(',')[0][1:])
del df.data_dict['Name']
df.data_dict['Surname'] = surnames
df.columns[name_index] = 'Surname'

# splitting cabin type and cabin number
cabin_index = df.columns.index('Cabin')
cabin_type = []
cabin_num = []
for cabin in df.data_dict['Cabin']:
    if ' ' in cabin:
        cabin = cabin.split(' ')[0]
    char = ''
    num = ''
    for i in cabin:
        try:
            int(i)
            num += i
        except ValueError:
            char += i
    cabin_type.append(char)
    cabin_num.append(num)
del df.data_dict['Cabin']
df.data_dict['CabinType'] = cabin_type
df.data_dict['CabinNumber'] = cabin_num
df.change_col_type('CabinNumber', int)
df.columns[cabin_index] = 'CabinType'
df.columns.insert(cabin_index+1, 'CabinNumber')

# splitting ticket type and ticket number
ticket_index = df.columns.index('Ticket')
ticket_type = []
ticket_num = []
for ticket in df.data_dict['Ticket']:
    split = ticket.split(' ')
    if len(split) > 1:
        if len(split) == 3:
            ticket_type.append(str(split[0]) + str(split[1]))
            ticket_num.append(split[2])
            continue
        ticket_type.append(split[0])
        ticket_num.append(split[1])
    else:
        var = split[0]
        try:
            int(var)
            ticket_type.append(None)
            ticket_num.append(var)
        except ValueError:
            ticket_type.append(var)
            ticket_num.append(None)
del df.data_dict['Ticket']
df.data_dict['TicketType'] = ticket_type
df.data_dict['TicketNumber'] = ticket_num
df.change_col_type('TicketNumber', int)
df.columns[ticket_index] = 'TicketType'
df.columns.insert(ticket_index+1, 'TicketNumber')

# implementing sql methods
'''
pclass = df.group_by("Pclass")
print(pclass.aggregate("Survived", "avg").select(["Pclass", "Survived"]).to_array())
print(pclass.aggregate("Survived", "count").select(["Pclass", "Survived"]).to_array())

sex = df.group_by("Sex")
print(sex.aggregate("Survived", "avg").select(["Sex", "Survived"]).to_array())
print(sex.aggregate("Survived", "count").select(["Sex", "Survived"]).to_array())
'''

