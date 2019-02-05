
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
    #solution = return the value og inflation, when unem = 0 and the value of unem when inflation = 0 
    UnEm = NatUnEm - ((-alpha*Ex_inflation)-Ex_inflation)/2
   # NatUnEm1 = UnEm + alpha*(Inflation-Ex_inflation)
    Inflation = Ex_inflation + (NatUnEm -(((-alpha*Ex_inflation)-Ex_inflation)/2)-NatUnEm)/alpha
    #Ex_inflation1 = (UnEm-NatUnEm)/alpha - Inflation
    UnEm1 = (NatUnEm-1) - (((-alpha)*(Ex_inflation-1))-(Ex_inflation)-1)/2
    Inflation1 = (Ex_inflation-1) + ((NatUnEm-1) -((((-alpha)*(Ex_inflation-1))-(Ex_inflation-1))/2)-(NatUnEm-1))/(alpha)

    return(Inflation,UnEm,Inflation1,UnEm1)



def plotting (x,y):
    #I am defining a function that i use in the "phillipsplot function"
    plt.plot(x,y)
    plt.xlabel("Unemployment")
    plt.ylabel("Inflation")
    plt.xlim(0,(int(x[0])+4))
    plt.ylim(0,(int(y[1])+4))
    plt.show()

def philipsPlot (x,clear=False):
    if type(x)== list or type(x) == tuple:
        Inflation = list([x[2],x[0]])
        Unemployment = list([x[3],x[1]])
    else: sys.exit("Error: The input is not a list or a tuple")
    if clear == False: 
        plotting(Unemployment,Inflation)
    else:
        plt.clf()
        plt.close()
        plotting(Unemployment,Inflation)

x = philipC(NatUnEm=2,Ex_inflation=4,alpha=0.3)
philipsPlot(x=x,clear=True)