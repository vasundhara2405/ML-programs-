import matplotlib.pyplot as plt
import numpy as np


#plot for sine wave
A=np.array([[7,8,1],[4,7,1],[1,3,5]])
print("\n****Plot for sine ****\n")
plt.plot(A,np.sin(A))
plt.xlabel('X')
plt.ylabel('SIN X')
plt.title('Plot of sin(x)')
plt.legend(['1st row','2nd row','3rd row'])
plt.grid()

plt.show()
print("\n****Plot for cosine ****\n")
plt.plot(A,np.cos(A))
plt.xlabel('X')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of cos(x)')
plt.legend(['1st row','2nd row','3rd row'])
plt.grid()
plt.show()


#sine and cosine wave
print("\n****Plot for sine and cosine ****\n")
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin(x) and cos(x)')
plt.legend(['sin(x)','cos[x]'])
plt.show()


#Histogram
print("\n****Plot for Histogram ****\n")
mu=165  #mean
sigma=5 #stddev
sample=250
np.random.seed(0)
height=np.random.normal(mu,sigma,sample).astype(int)
plt.hist(height,bins=10)
plt.title('Plot for Histogram')
plt.xlabel('Height')
plt.show()