import pandas as pd
import matplotlib.pyplot as plt

def main():
    my_data = pd.read_csv('datasets/dataset_train.csv')
    x = my_data.loc[:, 'Arithmancy':'Flying']

    pd.plotting.scatter_matrix(x, s=2, alpha=0.8)
    plt.show()

if __name__ == '__main__':
    main()

