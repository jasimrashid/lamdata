# lamdata

## Installation

Run these commands on Terminal:

```
pip install seaborn
pip install sklearn
....
...
```




## Usage

Go figure it out!
```

from pandas import DataFrame
from my_lamdata.my_mod import enlarge
from my_lamdata.my_mod import train_val_test_split
from my_lamdata.my_mod import contingency_tbl_chi_square


# x = 5
# print("NUMBER", x)
# print("ENLARGED NUMBER", enlarge(x)) # invoking our function!!


import seaborn as sns

iris = sns.load_dataset('iris')
train, val, test = train_val_test_split(iris, .2)
print(iris.shape)
print(train.shape,"\n",val.shape,"\n",test.shape)
print(val)
print()

titanic = sns.load_dataset('titanic')
contingency_tbl_chi_square(titanic['class'],titanic['sex'])

```






