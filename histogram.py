import pandas as pd
import matplotlib.pyplot as plt


def histogram_visual_separate(ax, d, house_name, color_of_house):

    h = d[d["Hogwarts House"] == house_name]
    scores = h.loc[:, "Care of Magical Creatures"]
    x = (scores - scores.mean()) / scores.std()
    #x = (scores - scores.min()) / (scores.max() - scores.min())
    ax.hist(x.values.flatten(), bins=40, rwidth=0.8, color=color_of_house)
    ax.set_title(house_name)

def histogram_all_in_one(ax, d, house_name, color_of_house):

    h = d[d["Hogwarts House"] == house_name]
    scores = h.loc[:, "Care of Magical Creatures"]
    x = (scores - scores.mean()) / scores.std()
    #x = (scores - scores.min()) / (scores.max() - scores.min())
    ax.hist(x.values.flatten(), bins=40, rwidth=0.8, color=color_of_house)
    ax.set_title('All houses')

my_data = pd.read_csv('datasets/dataset_train.csv')
gav = my_data.groupby(['Hogwarts House'])

fig, axs = plt.subplots(2,2, sharey=True, tight_layout=True)
histogram_visual_separate(axs[0][0],my_data, "Gryffindor", 'red')
histogram_visual_separate(axs[0][1],my_data, "Ravenclaw",'blue')
histogram_visual_separate(axs[1][0], my_data, "Slytherin", 'green')
histogram_visual_separate(axs[1][1],my_data, "Hufflepuff", 'yellow')
plt.show(block=False)
plt.pause(50)
plt.close()

fig, axs = plt.subplots(1,1, sharey=True, tight_layout=True)
histogram_all_in_one(axs,my_data, "Hufflepuff", 'yellow')
histogram_all_in_one(axs,my_data, "Ravenclaw",'blue')
histogram_all_in_one(axs,my_data, "Gryffindor", 'red')
histogram_all_in_one(axs, my_data, "Slytherin", 'green')

plt.show(block=False)
plt.pause(50)
plt.close()