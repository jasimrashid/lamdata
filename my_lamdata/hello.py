from pandas import DataFrame

from my_lamdata.my_mod import enlarge

print("HELLO")

print(enlarge(8))

df = DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())

# print("-----------------")
# x = 5
# print("NUMBER", x)
# print("ENLARGED NUMBER", enlarge(x)) # invoking our function!!
