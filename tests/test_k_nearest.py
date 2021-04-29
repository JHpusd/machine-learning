import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as knearestclass
import sys
sys.path.append('src')
from k_nearest import *
import matplotlib.pyplot as plt
'''
np_data = np.array([
    ['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
    ['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
    ['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
    ['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
    ['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
    ['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
    ['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
    ['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
    ['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
    ['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
    ['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
    ['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
    ['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ]])
cols = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour']
df = pd.DataFrame(np_data, columns=cols)

knn = KNearestNeighborsClassifier(k=5)
knn.fit(df, 'Cookie Type')
observation = {
    'Portion Eggs': 0.10,
    'Portion Butter': 0.15,
    'Portion Sugar': 0.30,
    'Portion Flour': 0.45}

# print(knn.classify(observation))

np_data = np.array([
    ['A', 0],
    ['A', 1],
    ['B', 2],
    ['B', 3]])
cols = ['letter', 'number']
df = pd.DataFrame(np_data, columns=cols)

knn = KNearestNeighborsClassifier(k=4)
knn.fit(df, 'letter')
observation = {
    'number': 1.6}
assert knn.classify(observation) == 'B'
print("Success")
'''
# using sklearn knn
df = pd.DataFrame(
    [['Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
['Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
['Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
['Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
['Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
['Sugar'       ,     0.02     ,       0.08     ,      0.45     ,     0.45      ],
['Sugar'       ,     0.10     ,       0.15     ,      0.35     ,     0.40      ],
['Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
['Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
['Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
['Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
['Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
['Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
['Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ],
['Shortbread'  ,     0.05     ,       0.12     ,      0.28     ,     0.55      ],
['Shortbread'  ,     0.14     ,       0.27     ,      0.31     ,     0.28      ],
['Shortbread'  ,     0.15     ,       0.23     ,      0.30     ,     0.32      ],
['Shortbread'  ,     0.20     ,       0.10     ,      0.30     ,     0.40      ]],
    columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour' ]
    )

def leave_one_out_true_false(knn, df, row_index):
    x_df = df[[col for col in df.columns if col != 'Cookie Type']]
    y_df = df['Cookie Type']

    classification = df['Cookie Type'].iloc[[row_index]].to_numpy().tolist()[0]
    values = x_df.iloc[[row_index]].to_numpy().tolist()[0]

    train_df = x_df.drop([row_index])
    train = train_df.reset_index(drop=True).to_numpy().tolist()
    test_df = y_df.drop([row_index])
    test = test_df.reset_index(drop=True).to_numpy().tolist()

    dummy_knn = knn.fit(train, test)
    result_classification = dummy_knn.predict([values])
    if result_classification == classification:
        return True
    return False

def leave_one_out_accuracy(knn, df):
    df_arr = df.to_numpy().tolist()
    correct = 0
    for row_index in range(len(df_arr)):
        if leave_one_out_true_false(knn, df, row_index):
            correct += 1
    return correct / len(df_arr)

k_vals = [k for k in range(1, 19)]
accuracies = []

for k_val in k_vals:
    knn = knearestclass(n_neighbors=k_val)
    accuracies.append(leave_one_out_accuracy(knn, df))

plt.style.use('bmh')
plt.plot(k_vals, accuracies)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.xticks(k_vals)
plt.title('Leave One Out Cross Validation')
plt.savefig('leave_one_out_accuracy.png')
