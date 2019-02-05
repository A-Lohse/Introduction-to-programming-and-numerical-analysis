
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
    return(Inflation,UnEm)


def plotting (x,y):
    #I am defining a function that i use in the "phillipsplot function"
    plt.plot(x,y)
    plt.xlabel("Unemployment")
    plt.ylabel("Inflation")
    plt.show()

def philipsPlot (x,clear=false):
    if type(x)== list or type(x) == tuple:
        Inflation = list(0,x[0])
        Unemployment = list(x[1],0)
    else: sys.exit("Error: The input is not a list or a tuple")
    if clear == False: 
        plotting(Inflation,Unemployment)
    else:
        plt.clf()
        plotting(Inflation, Unemployment)

x = philipC(NatUnEm=2,Ex_inflation=4,alpha=0.3)