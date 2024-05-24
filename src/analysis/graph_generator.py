import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

class VisualizationCreator:

    def __init__(self,df):
        '''
        The class has functions, which are responsible for creating graphs.
        '''
        self.df = df

    def categorical_box(self,col):
        cate = pd.DataFrame(self.df[col].value_counts())
        x = cate.index
        y = cate['count']
        plt.bar(x, y)
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.title(f'Quantity for {col}')
        plt.show()