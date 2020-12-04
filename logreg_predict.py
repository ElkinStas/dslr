import sys
import pandas as pd
import numpy as np
import utils


def weights_change(weights1, weights2):
    weight = weights1
    weight_ar = []
    for el in weight.split():
        weight_ar.append(el)
    return np.array(weight_ar, float).T, weights2


def prediction(list_to_predict, weights):
    with open('datasets/houses.csv', 'w') as file:
        file.write('Index,Hogwarts House\n')
        faculties = ['Ravenclaw', 'Gryffindor', 'Slytherin', 'Hufflepuff']
        Hat = utils.Sorting_Hat(10,1)
        weight1, bias1 = weights_change(weights.iloc[0][0], weights.iloc[0][1])
        weight2, bias2 = weights_change(weights.iloc[1][0], weights.iloc[1][1])
        weight3, bias3 = weights_change(weights.iloc[2][0], weights.iloc[2][1])
        weight4, bias4 = weights_change(weights.iloc[3][0], weights.iloc[3][1])

        for index, row in list_to_predict.iterrows():
            x = []
            fit1 = (row['Herbology'] - list_to_predict['Herbology'].mean()) / list_to_predict['Herbology'].std()
            fit2 = (row['Muggle Studies'] - list_to_predict['Muggle Studies'].mean()) / list_to_predict[
                'Muggle Studies'].std()
            fit3 = (row['Charms'] - list_to_predict['Charms'].mean()) / list_to_predict['Charms'].std()
            fit4 = (row['Divination'] - list_to_predict['Divination'].mean()) / list_to_predict['Divination'].std()
            fit5 = (row['Defense Against the Dark Arts'] - list_to_predict['Defense Against the Dark Arts'].mean()) / \
                   list_to_predict[
                       'Defense Against the Dark Arts'].std()
            fit6 = (row['Ancient Runes'] - list_to_predict['Ancient Runes'].mean()) / list_to_predict['Ancient Runes'].std()
            fit7 = (row['History of Magic'] - list_to_predict['History of Magic'].mean()) / list_to_predict[
                'History of Magic'].std()
            fit8 = (row['Flying'] - list_to_predict['Flying'].mean()) / list_to_predict['Flying'].std()
            fit9 = (row['Transfiguration'] - list_to_predict['Transfiguration'].mean()) / list_to_predict[
                'Transfiguration'].std()
            fit10 = (row['Potions'] - list_to_predict['Potions'].mean()) / list_to_predict['Potions'].std()
            x = [fit1, fit2, fit3, fit4, fit5, fit6, fit7, fit8, fit9, fit10]
            x = np.array(x)
            predict= [Hat(x, weight1, bias1), Hat(x, weight2, bias2), Hat(x, weight3, bias3), Hat(x, weight4, bias4)]

            file.write(str(index) + ',' + str(faculties[predict.index(max(predict))]) + '\n')

try:

    weights = pd.read_csv(sys.argv[1])
    list_to_predict = pd.read_csv(sys.argv[2])
    list_to_predict = list_to_predict.fillna(list_to_predict.mean())
    prediction(list_to_predict, weights)

except:
    print('Just remember - first is weights and second is data. So you should try once again')

