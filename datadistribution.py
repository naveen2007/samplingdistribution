import pandas as pd 
import csv 
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import statistics 
import random

df = pd.read_csv('../csv/temp.csv')
data = df['temp'].tolist()
fig = ff.create_distplot([data],['temp'],show_hist = False)
## fig.show()

dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    print(i)
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
std = statistics.stdev(dataset)
print(mean)
print(std)

def random_setofmean(counter):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],['temp'],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0.1],mode = 'lines', name = 'MEAN'))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        setofmean = random_setofmean(100)
        mean_list.append(setofmean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print('mean of sampling distribution', mean)
setup()  

population_mean = statistics.mean(data)
print('population mean', population_mean)

    