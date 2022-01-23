import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv


df = pd.read_csv("medium_data.csv")
data = df["publication"].tolist()



def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean



mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)


std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)


print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)


z_score = (mean_of_sample1 - mean)/std_deviation
print("The z score is = ",z_score)