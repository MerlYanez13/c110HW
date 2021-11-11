import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd 
import csv 
import random
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
def randomsetofmeans(counter):
    dataset=[]
    for i in range(0, counter):
        index=random.randint(0,len(data)-1)
        val=data[index]
        dataset.append(val)
    mean=statistics.mean(dataset)
    return mean 
def showfig(meanlist):
    mean=statistics.mean(meanlist)
    fig=ff.create_distplot([meanlist],["meanlist"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,10],mode="lines",name="mean"))
    fig.show()

def main():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmeans(25)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean=statistics.mean(meanlist)
    print("sampling mean: ",mean)
    sd=statistics.stdev(meanlist)
    print("sampling deviation: ", sd)
main()
populationmean=statistics.mean(data)
print("population mean: ", populationmean)
populationsd=statistics.stdev(data)
print("population deviation: ", populationsd)