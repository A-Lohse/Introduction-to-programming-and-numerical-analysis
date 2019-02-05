
#The Philips curve is given by u = u**n - alpha(pi - pi**e)
    #Here u represents the unemployment, u*n the natural unemployment, pi the rate of inflation and pi**e the expectet rate of inflation. Alfha is a paramter that 
    # determines how unemployment reacts to surprise inflation 
    # the Philips curve represent the trade-off between inflation and unemployment, and if solved by deriving the "loss function", and solving this for 0 
    # essentially minimissing the "loss" to society 

import numpy as np
import sys
import matplotlib.pyplot as plt

#edit it need to take only natural unemployment, expected inflation and alpha as input, and output Inflation and unemployment
def philipC(NatUnEm,Ex_inflation,alpha=False):
    if alpha == False:
        sys.exit("Error: You have to provide an alpha value")
    #UnEm1 = NatUnEm - alpha*(Ex_inflation + ((UnEm-NatUnEm)/alpha)-Ex_inflation) 
    #My rather bad math tells me that unemployment must be given by 
    UnEm = NatUnEm - ((-alpha*Ex_inflation)-Ex_inflation)/2
   # NatUnEm1 = UnEm + alpha*(Inflation-Ex_inflation)
    Inflation = Ex_inflation + (NatUnEm -(((-alpha*Ex_inflation)-Ex_inflation)/2)-NatUnEm)/alpha
    #Ex_inflation1 = (UnEm-NatUnEm)/alpha - Inflation
   
    all_vars = list([UnEm, Inflation])
    return(Inflation,UnEm)

x = philipC(NatUnEm=2,Ex_inflation=4,alpha=0.3)
inflation = x[0]
Unemployment = x[1]
Natural_Unemployment = x[2]
Expectet_Inflation = x[3]

x = list([0,inflation])
y = list([Unemployment,0])

plt.scatter(y,x)
plt.show()
print(inflation,Unemployment)