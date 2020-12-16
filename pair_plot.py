import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    my_data = pd.read_csv('datasets/dataset_train.csv')
    x = my_data.loc[:, 'Hogwarts House':'Flying']

    sns.pairplot(data = x, hue = 'Hogwarts House')
    plt.show()

if __name__ == '__main__':
    main()

