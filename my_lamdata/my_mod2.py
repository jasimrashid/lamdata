# my_lambdata/my_mod.py
# Returns the product of the argument and 100
def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100


class MachineLearningData():

    def __init__(self, df, size):
        self.df = df
        self.size = size

    def train_val_test_split(self):
        """
        Input: Pandas Dataframe and size(ratio of train-test and train-val split)
        
        Function first splits dataframe into training and test sets, and further splits the training set into training and validation sets.

        Output: Three dataframes, reprsenting training, validation & test sets
        """
        from sklearn.model_selection import train_test_split
        train, test = train_test_split(self.df, train_size=1-self.size, test_size=self.size, random_state=42)
        train, val = train_test_split(train, train_size=1-self.size, test_size=self.size, random_state=42)
        return train, val, test


# Contingency table + Chi-squared report function: takes two categorical variables, outputs a contingency table and corresponding Chi-squared test
class Categorical_feature_pair():

    def __init__(self, feat1, feat2):
        self.feat1 = feat1
        self.feat2 = feat2


    
    def contingency_tbl_chi_square(self):
        """
        Input: Param feat1 & feat 2  are DataFrames containing string objects, i.e. are categorical variables
        
        Function creates a contingency table from feat1 and feat2, and performs a Chi-squared test using the contingency table as input

        Output: Contingency table, chi-squared, p-value and degreees of freedom
        """

        import pandas as pd
        contingency_table = pd.crosstab(self.feat1, self.feat2, margins = True)
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

    # Functionally
    # contingency_tbl_chi_square(titanic['class'],titanic['sex'])

    # With classes  
    feats = Categorical_feature_pair(titanic['class'],titanic['sex'])
    feats.contingency_tbl_chi_square()

    dataset = MachineLearningData(titanic, .2)
    print(dataset.train_val_test_split())

