import sys
import pandas as pd
import numpy as np
import utils


def train_of_classificator(training_data, m_norma):

    w1 = np.array([[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]])
    w2 = np.array([[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]])
    w3 = np.array([[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]])
    w4 = np.array([[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]])
    b1 = 0.0
    b2 = 0.0
    b3 = 0.0
    b4 = 0.0

    learning_rate = 0.01
    Hat = utils.Sorting_Hat(10, 1)

    for epoch in range(3):
        for index, row in training_data.iterrows():
            fit1 = (row['Herbology'] - training_data['Herbology'].mean()) / training_data['Herbology'].std()
            fit2 = (row['Muggle Studies'] - training_data['Muggle Studies'].mean()) / training_data['Muggle Studies'].std()
            fit3 = (row['Charms'] - training_data['Charms'].mean()) / training_data['Charms'].std()
            fit4 = (row['Divination'] - training_data['Divination'].mean()) / training_data['Divination'].std()
            fit5 = (row['Defense Against the Dark Arts'] - training_data['Defense Against the Dark Arts'].mean()) / training_data[
                'Defense Against the Dark Arts'].std()
            fit6 = (row['Ancient Runes'] - training_data['Ancient Runes'].mean()) / training_data['Ancient Runes'].std()
            fit7 = (row['History of Magic'] - training_data['History of Magic'].mean()) / training_data['History of Magic'].std()
            fit8 = (row['Flying'] - training_data['Flying'].mean()) / training_data['Flying'].std()
            fit9 = (row['Transfiguration'] - training_data['Transfiguration'].mean()) / training_data['Transfiguration'].std()
            fit10 = (row['Potions'] - training_data['Potions'].mean()) / training_data['Potions'].std()

            if row['Hogwarts House'] == 'Ravenclaw':
                x1 = []
                t = 1
                x1 = [fit1, fit2, fit3, fit4, fit5, fit6, fit7, fit8, fit9, fit10]
                x1 = np.array(x1)
                Yhat = Hat(x1, w1, b1)
                delta = Yhat - t
                x1 = x1.reshape(1, -1)
                w1 = w1 - learning_rate * (x1.T.dot(delta)) / m_norma
                b1 = b1 - learning_rate * (delta) / m_norma

            if row['Hogwarts House'] == 'Gryffindor':
                x2 = []
                t = 1
                x2 = [fit1, fit2, fit3, fit4, fit5, fit6, fit7, fit8, fit9, fit10]
                x2 = np.array(x2)
                Yhat = Hat(x2, w2, b2)
                delta = Yhat - t
                x2 = x2.reshape(1, -1)
                w2 = w2 - learning_rate * (x2.T.dot(delta)) / m_norma
                b2 = b2 - learning_rate * (delta) / m_norma

            if row['Hogwarts House'] == 'Slytherin':
                x3 = []
                t = 1
                x3 = [fit1, fit2, fit3, fit4, fit5, fit6, fit7, fit8, fit9, fit10]
                x3 = np.array(x3)
                Yhat = Hat(x3, w3, b3)
                delta = Yhat - t
                x3 = x3.reshape(1, -1)
                w3 = w3 - learning_rate * (x3.T.dot(delta)) / m_norma
                b3 = b3 - learning_rate * (delta) / m_norma

            if row['Hogwarts House'] == 'Hufflepuff':
                x4 = []
                t = 1
                x4 = [fit1, fit2, fit3, fit4, fit5, fit6, fit7, fit8, fit9, fit10]
                x4 = np.array(x4)
                Yhat = Hat(x4, w4, b4)
                delta = Yhat - t
                x4 = x4.reshape(1, -1)
                w4 = w4 - learning_rate * (x4.T.dot(delta)) / m_norma
                b4 = b4 - learning_rate * (delta) / m_norma

    with open('weights_for_prediction.csv', 'w') as file:
        file.write('Weights,bias\n')
        file.write(str(w1.T).replace('\n','').strip('[]') + ',' + str(b1).strip('[]') + '\n')
        file.write(str(w2.T).replace('\n','').strip('[]') + ',' + str(b2).strip('[]') + '\n')
        file.write(str(w3.T).replace('\n','').strip('[]') + ',' + str(b3).strip('[]') + '\n')
        file.write(str(w4.T).replace('\n','').strip('[]') + ',' + str(b4).strip('[]') + '\n')


try:
    data_to_train = pd.read_csv(sys.argv[1])
    data_to_train2 = data_to_train
    data_to_train = data_to_train.dropna()
    train_of_classificator(data_to_train, len(data_to_train.index))

except:
    print('There is no data! Try once again with data')