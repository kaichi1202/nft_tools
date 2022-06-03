import csv
import os

with open('./wallet-list.csv') as f:
  reader = csv.reader(f)
  l = [row for row in reader]

l_T = [list(x) for x in zip(*l)]

list = [i for i in l_T[2] if i != '' and i != 'walletAddress']

def addQuotation(str):
  return '\"' + str + '\"'

newList = map(addQuotation, list)

with open('./list.txt', 'w') as tf:
  tf.write('[' + ', '.join(newList) + ']')
