import numpy as np
import pandas as pd

from sklearn.model_selection import ShuffleSplit

data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis = 1)