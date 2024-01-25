import matplotlib.pyplot as mp
import numpy as np
x=np.array([70,10,30,59,53])
y=np.array([10,50,80,15,18])
volume=[100,400,600,800,900]
colours=["red","green","blue","pink","black"]
mp.scatter(x,y,s=volume,c=colours,label="Example",cmap="nipy_spectral",alpha=0.5)
mp.colorbar()
mp.legend()
mp.show()