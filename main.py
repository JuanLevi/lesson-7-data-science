import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



x=[1,2,4,5,6,8,9]
y=[2,4,6,8,9,15,18]
'''
plt.plot(x,y) #light blue line connect dots
plt.show()


plt.plot(x,y,"ro") #red dots
plt.show()


plt.plot(x,y,"g^") #green traingles
plt.show()


plt.plot(x,y,"r--") #red dasehd line
plt.show()


plt.plot(x,y,"b--") #blue dashed line
plt.show()


plt.plot(x,y,"b-") #solid blue line
plt.show()



plt.plot(x,y,"r--",label="Y=X+2")

plt.axis([0,10,0,19])#range

plt.xlabel("X")
plt.ylabel("Y")
plt.title("XY graph")
plt.legend()
plt.show()
'''
plt.figure(figsize=(12,7))
x=np.arange(0,5,0.5)

y1=5*x+2
plt.plot(x,y1,label="Y=5X+2")

y2=x**2
plt.plot(x,y2,"r--",label="Y=X^2")

y3=x**3
plt.plot(x,y3,"b--",label="Y=X^3")



plt.xlabel("X")
plt.ylabel("Y")
plt.title("XY graph")
plt.grid(True)

plt.axhline(0,color="black",linewidth=2)
plt.axvline(0,color="black",linewidth=2)


plt.legend()
plt.show()



#bar graph

plt.bar(["Male","Females"],[7,13],color='b')
plt.bar(["Male","Females"],[7,13],color='g')
plt.show()




#### HISTOGRAMS #####

ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages,bins,histtype="bar",rwidth=0.8)
plt.xlabel("Ages")
plt.ylabel("Amount")
plt.title("Histogram")
plt.show()



x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6]) #
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])


plt.scatter(x,y,label="Age vs Speed",color="Black",s=50)
plt.xlabel("Ages")
plt.ylabel("SPeed")
plt.title("Cataplot")
plt.show()


# pie chart

values=[2,4,5,9]
name=["15y","20y","25y","30y"]
colors=["r","g","c","b"]

plt.pie(values,labels=name,colors=colors)
plt.title("Pie chart")
plt.show()


# stack plot
eating=[3,4,2,3,2]
sleeping=[8,7,9,8,7]
playing=[2,3,6,2,4]
studying=[2,3,4,3,2]
days=["Mon","Tue","Wed","Thu","Fri"]

plt.plot([],[],color="r",label="Eating")
plt.plot([],[],color="b",label="Sleeping")
plt.plot([],[],color="g",label="Playing")
plt.plot([],[],color="y",label="Studying")

plt.stackplot(days,eating,sleeping,playing,studying,colors=["r",'b','g','y'])
plt.xlabel("Days of the week")
plt.ylabel("Activities")
plt.title("Stack plot")
plt.legend()
plt.show()



# sub plots

t=np.array([2,4,6,8,9,15,18])

t1=t*5

t2=t-3
t3=t/2




graph1=np.exp(-t)*np.cos(2*np.pi*t)
graph2=np.exp(-t1)*np.cos(2*np.pi*t1)
graph3=np.exp(-t2)*np.cos(2*np.pi*t2)
graph4=np.exp(-t3)*np.cos(2*np.pi*t3)

plt.figure()
plt.subplot(221)
plt.plot(t,graph1,"bo")

plt.subplot(222)
plt.plot(t1,graph2,"ro")

plt.subplot(223)
plt.plot(t2,graph3,"go")

plt.subplot(224)
plt.plot(t3,graph4,"co")

plt.show()









