import pandas as pd
from pandas import DataFrame, read_excel, read_csv, merge

df1 = read_csv("download/13030_BPR-00000177_20181111010214.csv",delimiter = ";")
df2 = read_csv("download/test_20181115_232308.csv", delimiter = ",")

#print("heads for df2")
#print(df2.head())

#print("heads for df1")
#print(df1.head())

#print("index")
#print(df2.index)
#print("columns")
#print(df2.columns)

#print("transpose")
#print(df2.T)
#print("sort)")
#print(df2.sort_index(axis=1, ascending=False))

print("write to excel")
df2.to_excel('download/foo.xlsx', sheet_name='stef')

print("merge")
#not yet tested, code just writtten then Visual Studio closed !
df3 = df1.merge(df2, how='inner', left_on='Subscription: SubscriptionId',right_on='Subscription.Id')

cols = df3.columns.tolist()
print(cols)

print("re order column")
myorder=[1,2,3,4,5,30,6,29,7,28,8,27,9,26,10,25,11,24,12,23,13,22,14,21,15,20,16,19,17,18,]
cols = [ cols[i] for i in myorder]

print(cols)
df3 = df3[cols]



df3.to_excel('download/result.xlsx', sheet_name='stef')
#print(df3.head())