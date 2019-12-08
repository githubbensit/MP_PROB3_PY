import numpy as np
import ast

dp = input('Create an array with two columns (i.e [x,y],[x,y],...):  ') 
vdp = ast.literal_eval(dp) 
n = np.asarray(vdp) 
print (n)

for i in range(len(n)):
    e = np.polyfit(n[:,0], n[:,1],i)
    r = np.polyval(e, n[:,0])
    s = np.linalg.norm(n[:,1] - r)
    a = [i,s]
    if i==0:
        x = a
        
    elif x[1] >= a[1]:
        y = a[0]       
coeff = np.polyfit(n[:,0],n[:,1],y)
print('The coefficients of the data points are: ',coeff)
    
    