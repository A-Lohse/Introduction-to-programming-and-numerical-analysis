
#The Philips curve is given by u = u**n - alpha(pi - pi**e)
    #Here u represents the unemployment, u*n the natural unemployment, pi the rate of inflation and pi**e the expectet rate of inflation. Alfha is a paramter that 
    # determines how unemployment reacts to surprise inflation 
    # the Philips curve represent the trade-off between inflation and unemployment, and if solved by deriving the "loss function", and solving this for 0 
    # essentially minimissing the "loss" to society 

import numpy as np
import sys
import matplotlib.pyplot as plt

def philipC(UnEm,NatUnEm,Inflation,Ex_inflation,alpha=False):
    if alpha == False:
        sys.exit("Error: You have to provide an alpha value")
    UnEm1 = NatUnEm - alpha*(Inflation-Ex_inflation) 
    NatUnEm1 = UnEm + alpha*(Inflation-Ex_inflation)
    Inflation1 = Ex_inflation + (UnEm-NatUnEm)/alpha
    Ex_inflation1 = (UnEm-NatUnEm)/alpha - Inflation
   
    all_vars = list([UnEm1,NatUnEm1,Inflation1,Ex_inflation1,alpha])
    return(Inflation1,UnEm1,NatUnEm1,Ex_inflation1)

x = philipC(UnEm=2,NatUnEm=2,Inflation=0.2,Ex_inflation=0.1,alpha=0.3)
inflation = x[0]
Unemployment = x[1]

x = list([0,inflation])
y = list([Unemployment,0])

plt.scatter(y,x)
plt.show()
