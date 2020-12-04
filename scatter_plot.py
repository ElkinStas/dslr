import pandas as pd

import matplotlib.pyplot as plt

my_data = pd.read_csv('datasets/dataset_train.csv')
plt.scatter(my_data['Astronomy'], my_data['Defense Against the Dark Arts'], edgecolors='red')
plt.xlabel('astronomy')
plt.ylabel('defense_dark_arts')
plt.show()