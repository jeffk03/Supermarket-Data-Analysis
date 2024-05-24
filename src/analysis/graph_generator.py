import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

class VisualizationCreator:

    def __init__(self,df):
        '''
        The class has functions, which are responsible for creating graphs.
        '''
        self.df = df
    
    def p(self):
        print('teste')

    def categorical_box(self,col):
        cate = pd.DataFrame(self.df[col].value_counts())
        x = cate.index
        y = cate.iloc[:,0]
        plt.bar(x, y)
        plt.xlabel(col,rotation=45, ha='right')
        plt.ylabel('Count')
        plt.title(f'Quantity for {col}')
        for i, v in enumerate(y):  # Adiciona os valores dentro do gráfico
            plt.text(i, v + 0.1, str(v), ha='center'
        plt.show()