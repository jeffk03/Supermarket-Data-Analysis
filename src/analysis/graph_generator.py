import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde


class VisualizationCreator:

    def __init__(self,df):
        '''
        The class has functions, which are responsible for creating graphs.
        '''
        self.df = df
    
    def p(self):
        print('teste')

    def categorical_box(self,col,grid = True):
        cate = pd.DataFrame(self.df[col].value_counts())
        x = cate.index
        y = cate.iloc[:,0]
        plt.bar(x, y)
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.grid(grid)       
        plt.title(f'Quantity for {col}') 
        plt.show()

    def dist_plot(self,col,bins = 30):        
      """
      Gera um gráfico de distribuição para uma coluna específica de um DataFrame.
      """
      # Verifica se a coluna existe no DataFrame
      if col not in self.df.columns:
        raise ValueError(f"A coluna '{col}' não existe no DataFrame.")
      
      # Configura o estilo do seaborn
      sns.set(style='whitegrid')
      # Cria o gráfico de distribuição
      plt.figure(figsize=(10, 6))
      sns.histplot(self.df[col], kde=True, bins=bins, color='blue')

      # Calcula a KDE
      data = self.df[col].dropna()
      kde = gaussian_kde(data)
      x_range = np.linspace(data.min(), data.max(), 1000)
      kde_values = kde(x_range)

      # Plota a linha KDE
      plt.plot(x_range, kde_values, color='red', lw=2, label='KDE')

      # Título e rótulos
      plt.title(f'Distribuição da coluna: {col}', fontsize=16)
      plt.xlabel(col,fontsize =14)
      plt.ylabel('Frequência',fontsize = 14)

      # Exibir o gráfico
      plt.show()

       
    
    
    
  
    
