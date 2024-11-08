import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data=pd.read_csv("titanic.csv")

print(data["Sex"].value_counts())


male=data["Sex"].value_counts()["male"]
female=data["Sex"].value_counts()["female"]

plt.bar(["Male","Females"],[male,female],color='b')
plt.show()


malefare=data[data["Sex"]=="male"]["Fare"].mean()
print(malefare)

femalefare=data[data["Sex"]=="female"]["Fare"].mean()
print(femalefare)

plt.bar(["Male","Females"],[malefare,femalefare],color='b')
plt.show()


class1=data["Pclass"].value_counts()[1]
class2=data["Pclass"].value_counts()[2]
class3=data["Pclass"].value_counts()[3]

plt.bar(["1st Class","2nd Class","3rd Class"],[class1,class2,class3],color='b')
plt.show()



