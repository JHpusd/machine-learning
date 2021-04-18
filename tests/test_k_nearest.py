import pandas as pd
import numpy as np
import sys
sys.path.append('src')
from k_nearest import *
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

print(knn.classify(observation))
'''
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
