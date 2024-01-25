import matplotlib.pyplot as ma
x=[3,4,5,6,7]
y=[8,6,5,4,2]           
ma.xlim(1,10)           #set the limit of the x axis
ma.ylim(1,10)           #set the limit of the y axis
ma.xticks([3,4,5])  
ma.yticks([5,6,7])    #to see the output of xlim and ylim comment the xtricts and ytrics code
ma.plot(x,y)
ma.show()