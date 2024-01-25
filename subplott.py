import matplotlib.pyplot as mp
x=[1,2,3,4,5]
y=[10,30,40,50,60]
y1=[25,35,45,65,55]

mp.subplot(1,2,1)
mp.plot(x,y)
mp.subplot(1,2,2)
mp.plot(x,y1)
mp.show()