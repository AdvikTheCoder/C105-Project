import math
import plotly.express as px
import csv
import pandas as pd
with open('data123.csv', newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)
data=fileData[0]
def findMean(data):
    n=len(data)
    total=0
    for x in data:
        total=total+int(x)
    mean=total/n
    return mean
squaredList=[]
for number in data:
    a=int(number)-int(findMean(data))
    a=a**2
    squaredList.append(a)
sum=0
for i in squaredList:
    sum=sum+i
n=len(data)
result=sum/n-1
sd=math.sqrt(result)
print(sd)
