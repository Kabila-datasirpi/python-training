import matplotlib.pyplot as mat
x=[-6,-3,0,3,6]
y=[-4,-2,0,2,4]

mat.plot(x,y ,color="red", linestyle="dashed", marker='o', markersize=6 ,markerfacecolor="blue", markeredgecolor="blue")

mat.grid()
mat.show()