import sys
from naive_bayes import *

data = {'Scam':[0,1,1,0,0,1,0,0,1,0],'Errors':[0,1,1,0,0,1,1,0,1,0],'Links':[0,1,1,0,1,1,0,1,0,1]}

nb = NaiveBayes(data)

predict_data = {'Errors':[0,1,1,0], 'Links':[0,1,0,1]}

print(nb.predict(predict_data))