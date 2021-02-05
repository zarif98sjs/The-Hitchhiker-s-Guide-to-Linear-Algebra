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

R = np.identity(3)
right = 5 ; up = 10 ## change here
R[0][2] = h
R[1][2] = k
print(R)

co = np.zeros((3,num))
co[0,:] = X
co[1,:] = Y
co[2,:] = 1

t = np.matmul(R,co)
plt.figure(2 , figsize=(12,8))
plt.grid(color='grey',linewidth=.5,dashes=[10,2,2,2,2,2])
plt.scatter(t[0,:],t[1,:],s=25,color = 'blue')
plt.plot(t[0,:],t[1,:])