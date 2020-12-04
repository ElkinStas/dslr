import csv
import pandas as pd
import math
import sys

def percentile(ordered_list_of_values, percent):
    if not ordered_list_of_values:
        return None
    k = (len(ordered_list_of_values) - 1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return ordered_list_of_values[int(k)]
    d0 = ordered_list_of_values[int(f)] * (c - k)
    d1 = ordered_list_of_values[int(c)] * (k - f)
    return d0 + d1


def describe(name_of_file):
    list_of_features = ['Index', 'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination',
                        'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions',
                        'Care of Magical Creatures', 'Charms', 'Flying']
    list_of_count = []
    list_of_mean = []
    list_of_std = []
    list_of_minimum = []
    list_of_25 = []
    list_of_50 = []
    list_of_75 = []
    list_of_maximum = []

    for target_value in list_of_features:
        with open(name_of_file) as csvfile:
            d_reader = csv.DictReader(csvfile)

            # get fieldnames from DictReader object and store in list
            headers = d_reader.fieldnames
            summ = 0
            count = 0
            minimum = 0
            maximum = 0
            ordered_data_list = []
            for line in d_reader:
                try:
                    summ += float(line[target_value])
                    count += 1
                    ordered_data_list.append(float(line[target_value]))
                    if float(line[target_value]) < minimum:
                        minimum = float(line[target_value])
                    if float(line[target_value]) > maximum:
                        maximum = float(line[target_value])
                except:
                    pass
        mean = summ / (float(count))
        ordered_data_list = sorted(ordered_data_list)

        with open(name_of_file) as csvfile:
            d_reader = csv.DictReader(csvfile)
            std = 0
            for line in d_reader:
                try:
                    std += (float(line[target_value]) - mean) ** 2
                except:
                    pass
            std = math.sqrt(std / float(count - 1))

        list_of_count.append(count)
        list_of_mean.append(mean)
        list_of_std.append(std)
        list_of_minimum.append(minimum)
        list_of_25.append(percentile(ordered_data_list, 0.25))
        list_of_50.append(percentile(ordered_data_list, 0.50))
        list_of_75.append(percentile(ordered_data_list, 0.75))
        list_of_maximum.append(maximum)

    df = pd.DataFrame({"count": list_of_count, "mean": list_of_mean, "std": list_of_std, "min": list_of_minimum,
                       "25%": list_of_25, "50%": list_of_50, "75%": list_of_75, "max": list_of_maximum},
                      index=list_of_features)
    df_orig = df.T
    return (df_orig)

def main():
    print(describe(sys.argv[1]))


if __name__ == '__main__':
    main()






















