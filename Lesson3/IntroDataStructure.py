import numpy as np
import pandas as pd

s = pd.Series(np.random.rand(5), index = ['a', 'b', 'c', 'd', 'e'])
# print(s)

d = {'a' : 2, 'b' : 0, 'c' : 1}

print(pd.Series(d))

print(pd.Series(d, index = ['b', 'c', 'd', 'a']))

dic = {'one' : pd.Series([1., 2., 3.,], index = ['a', 'b', 'c']), 'two' : pd.Series([4., 5., 6., 7.,], index = ['a', 'b', 'c', 'd'])}

df = pd.DataFrame(dic)

print(df)

df = pd.DataFrame(dic, index = ['b', 'd', 'a'])

print (df)

index = pd.date_range('1/1/2000', periods=8)
print(index)

df = pd.DataFrame(np.random.randn(8,3), index = index, columns = ['A', 'B', 'C'])
print(df)

wp = pd.Panel(np.random.randn(2, 5, 4), items = ['item1', 'item2'],)
