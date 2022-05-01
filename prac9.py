import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-pastel')
fig,ax=plt.subplots()

x=np.linspace(0,2*np.pi,400)
y=np.sin(x**2)+np.cos(x)
ax.plot(x,y)
ax.set_title('Simple plot')
plt.show()

fig1,ax1=plt.subplots(2,2)
x1=np.arange(1,5)
ax1[0][0].plot(x1,x1**x1,'r')
ax1[0][0].set_title('Square')
ax1[0][1].plot(x1,np.sqrt(x1),'y')
ax1[0][1].set_title('Square root')
ax1[1][0].plot(x1,np.exp(x1))
ax1[1][0].set_title('Exp')
ax1[1][1].plot(x1,np.log10(x1),'g')
ax1[1][1].set_title('Log')
plt.show()