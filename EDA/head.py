import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def isnull_in_data(train, test):
    print("Train data missed values:\n")
    print(train.isnull().sum())
    print("-----------------------------------")
    print("Test data missed values:\n")
    print(test.isnull().sum())

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

train = pd.read_parquet('../data/train_after_test.parquet')
test = pd.read_parquet('../data/test_after_test.parquet')

print(train.shape)
print("-----------------------------------")
print(train.corrwith(train['target']).sort_values())
print("-----------------------------------")
plt.figure(figsize=(50,40))
sns.heatmap(train.corr(), annot=True)
plt.show()
print("-----------------------------------")
print(isnull_in_data(train, test))
print("-----------------------------------")
print(train.describe())
print("-----------------------------------")
print(train.head())
#print(train.describe(include=['O']))
#print(test.describe(include=['O']))

