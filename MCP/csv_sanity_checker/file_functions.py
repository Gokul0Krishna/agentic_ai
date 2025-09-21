import pandas as pd
# import matplotlib.pyplot as plt

class File():
    def __init__(self,file_location):
        self.df= pd.read_csv(file_location)
    
    def isnull(self):
        "retuns no. of null values in the dataframe "
        a=self.df.isna().sum()
        if a.sum()==0:
            return a.abs()
        else:
            return False
        
    def discribe_df(self):
        "returns df's discription and correlation and shape"
        x = self.df.corr()
        y = self.df.describe()
        z = self.df.shape
        return f'correlation of dependent on indepandent {x.iloc[:,-1]},information about the table{y},shape of table{z}'
    