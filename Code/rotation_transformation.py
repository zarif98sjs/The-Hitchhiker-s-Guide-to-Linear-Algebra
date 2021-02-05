import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-40,120,3)
num = len(X)
Y = np.sin(X)
# print(X)
# print(Y)
plt.figure(1 , figsize=(12,8))

plt.grid(color='grey',linewidth=.5,dashes=[10,2,2,2,2,2])
plt.plot(X,Y)
plt.scatter(X,Y,s=25,color = 'blue')

theta = np.radians(90)
c, s = np.cos(theta), np.sin(theta)
R = np.array(((c, -s), (s, c)))

co = np.zeros((2,num))
co[0,:] = X
co[1,:] = Y

t = np.matmul(R,co)
plt.figure(2 , figsize=(12,8))
plt.grid(color='grey',linewidth=.5,dashes=[10,2,2,2,2,2])
plt.scatter(t[0,:],t[1,:],s=25,color = 'blue')
plt.plot(t[0,:],t[1,:])