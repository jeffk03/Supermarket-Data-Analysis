import matplotlib.pyplot as plt
import seaborn as sns 

class VisualizationCreator:

    def __init__(self,df):
        '''
        The class has functions, which are responsible for creating graphs.
        '''
        self.df = df