import numpy as np
import utils
import pandas as pd
from PIL import Image
import time

def weights_change(weights1, weights2):
    weight = weights1
    weight_ar = []
    for el in weight.split():
        weight_ar.append(el)
    return np.array(weight_ar, float).T, weights2

def prediction(list_to_predict, data_choose, weights):
    with open('datasets/houses.csv', 'w') as file:
        file.write('Index,Hogwarts House\n')
        faculties = ['Ravenclaw', 'Gryffindor', 'Slytherin', 'Hufflepuff']
        Hat = utils.Sorting_Hat(10,1)
        weight1, bias1 = weights_change(weights.iloc[0][0], weights.iloc[0][1])
        weight2, bias2 = weights_change(weights.iloc[1][0], weights.iloc[1][1])
        weight3, bias3 = weights_change(weights.iloc[2][0], weights.iloc[2][1])
        weight4, bias4 = weights_change(weights.iloc[3][0], weights.iloc[3][1])


        x = []
        fit1 = (list_to_predict[0][0] - data_choose['Herbology'].mean()) / data_choose['Herbology'].std()
        fit2 = (list_to_predict[0][3] - data_choose['Muggle Studies'].mean()) / data_choose['Muggle Studies'].std()
        fit3 = (list_to_predict[0][9] - data_choose['Charms'].mean()) / data_choose['Charms'].std()
        fit4 = (list_to_predict[0][2] - data_choose['Divination'].mean()) / data_choose['Divination'].std()
        fit5 = (list_to_predict[0][1] - data_choose['Defense Against the Dark Arts'].mean()) / data_choose['Defense Against the Dark Arts'].std()
        fit6 = (list_to_predict[0][5] - data_choose['Ancient Runes'].mean()) / data_choose['Ancient Runes'].std()
        fit7 = (list_to_predict[0][6] - data_choose['History of Magic'].mean()) / data_choose['History of Magic'].std()
        fit8 = (list_to_predict[0][10] - data_choose['Flying'].mean()) / data_choose['Flying'].std()
        fit9 = (list_to_predict[0][7] - data_choose['Transfiguration'].mean()) / data_choose['Transfiguration'].std()
        fit10 = (list_to_predict[0][8] - data_choose['Potions'].mean()) / data_choose['Potions'].std()
        x = [fit1, fit2, fit3, fit4, fit5, fit6, fit7, fit8, fit9, fit10]
        x = np.array(x)
        predict= [Hat(x, weight1, bias1), Hat(x, weight2, bias2), Hat(x, weight3, bias3), Hat(x, weight4, bias4)]

        print(f'Your faculty is {faculties[predict.index(max(predict))]} !!!')
        image = Image.open(f'images_who_are_you/{faculties[predict.index(max(predict))]}.jpg')
        image.show()


weights = pd.read_csv('weights_for_prediction.csv')
data_to_choose = pd.read_csv('datasets/dataset_train.csv')
mass_of_values = []
print('So, let me guess... Which faculty is best for you? Lets test you!')
val = input('Arithmancy: from 0 to 10: ')
val_true = data_to_choose['Arithmancy'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Astronomy: from 0 to 10: ')
val_true = data_to_choose['Astronomy'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Herbology: from 0 to 10: ')
val_true = data_to_choose['Herbology'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Defense Against the Dark Arts: from 0 to 10 :')
val_true = data_to_choose['Defense Against the Dark Arts'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Divination: from 0 to 10: ')
val_true = data_to_choose['Divination'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Muggle Studies: from 0 to 10: ')
val_true = data_to_choose['Muggle Studies'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Ancient Runes: from 0 to 10: ')
val_true = data_to_choose['Ancient Runes'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('History of Magic: from 0 to 10: ')
val_true = data_to_choose['History of Magic'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Transfiguration: from 0 to 10: ')
val_true = data_to_choose['Transfiguration'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Potions: from 0 to 10: ')
val_true = data_to_choose['Potions'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Care of Magical Creatures: from 0 to 10: ')
val_true = data_to_choose['Care of Magical Creatures'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Charms: from 0 to 10: ')
val_true = data_to_choose['Charms'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
val = input('Flying: from 0 to 10: ')
val_true = data_to_choose['Flying'].describe(percentiles=[float(val)/10])[4]
mass_of_values.append(val_true)
print("Hmmmmm... I'm thinking")
time.sleep(3)
print("Steel thinking...")
time.sleep(5)
print("...Maybe you should go to the factory? ...")
time.sleep(7)
mass_of_values = pd.DataFrame(mass_of_values)
prediction(mass_of_values, data_to_choose, weights)
