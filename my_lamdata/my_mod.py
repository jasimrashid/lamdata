# my_lambdata/my_mod.py

# this code breaks our ability to import enlarge from other files, if left in the global scope:
def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100



def train_val_test_split(df, size):


    """
    Input: Pandas Dataframe object and size(ratio of train-test and train-val split)
    
    Function first splits dataframe into training and test sets. Then splits training set into training and validation sets.

    Output: Three dataframes, reprsenting training, validation & test sets
    """
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(df, train_size=1-size, test_size=size, random_state=42)
    train, val = train_test_split(train, train_size=1-size, test_size=size, random_state=42)
    return train, val, test


# Contingency table + Chi-squared report function: takes two categorical variables, outputs a contingency table and corresponding Chi-squared test
def contingency_tbl_chi_square(feat1, feat2):
    """
    Input: Param feat1 & feat 2  are DataFrames containing string objects, i.e. are categorical variables
    
    Function creates a contingency table from feat1 and feat2, and performs a Chi-squared test using the contingency table as input

    Output: Contingency table, chi-squared, p-value and degreees of freedom
    """

    import pandas as pd
    contingency_table = pd.crosstab(feat1, feat2, margins = True)
    print("Contingency Table: \n", contingency_table,"\n")

    from scipy import stats
    chi_squared, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    print("Chi-squared: ", chi_squared, "p-value: ", p_value, "DoF: ", dof)




if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    # print("HELLO")
    # y = int(input("Please choose a number"))
    # print(y, enlarge(y))

    import seaborn as sns
    # iris = sns.load_dataset('iris')
    # train, val, test = train_val_test_split(iris, .2)
    # print(iris.shape)
    # print(train.shape,"\n",val.shape,"\n",test.shape)
    # print(val)

    titanic = sns.load_dataset('titanic')
    contingency_tbl_chi_square(titanic['class'],titanic['sex'])