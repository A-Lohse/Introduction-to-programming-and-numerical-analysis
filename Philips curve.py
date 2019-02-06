
#The Philips curve is given by u = u**n - alpha(pi - pi**e)
    #Here u represents the unemployment, u*n the natural unemployment, pi the rate of inflation and pi**e the expectet rate of inflation. Alfha is a paramter that 
    # determines how unemployment reacts to surprise inflation 
    # the Philips curve represent the trade-off between inflation and unemployment, and if solved by deriving the "loss function", and solving this for 0 
    # essentially minimissing the "loss" to society 

import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

#edit it need to take only natural unemployment, expected inflation and alpha as input, and output Inflation and unemployment
def philipC(NatUnEm,Ex_inflation,alpha=False):
    if alpha == False:
        sys.exit("Error: You have to provide an alpha value")
    #UnEm1 = NatUnEm - alpha*(Ex_inflation + ((UnEm-NatUnEm)/alpha)-Ex_inflation) 
    #My rather bad math tells me that unemployment must be given by 
    #solution = return the value og inflation, when unem = 0 and the value of unem when inflation = 0 
    Inflation = 0.5
    UnEm = NatUnEm + (Ex_inflation - Inflation)/alpha
   # NatUnEm1 = UnEm + alpha*(Inflation-Ex_inflation)
    Unemployment = 0.5
    Inflation = Ex_inflation - alpha*(Unemployment - NatUnEm)
    #Ex_inflation1 = (UnEm-NatUnEm)/alpha - Inflation
       #Delete this
        #UnEm1 = (NatUnEm-1) - (((-alpha)*(Ex_inflation-1))-(Ex_inflation)-1)/2
        #Inflation1 = (Ex_inflation-1) + ((NatUnEm-1) -((((-alpha)*(Ex_inflation-1))-(Ex_inflation-1))/2)-(NatUnEm-1))/(alpha)

    return(UnEm,Inflation,Ex_inflation)



def plotting (x,y):
    #I am defining a function that i use in the "phillipsplot function"
    plt.plot(x,y)
    plt.xlabel("Unemployment")
    plt.ylabel("Inflation")
    plt.xlim(0,(int(x[0])+1))
    plt.ylim(0,(int(y[1])+1))
    plt.show()

def update(val):
    Ex_inflation = val
    return(Ex_inflation)

def philipsPlot (x,clear=False):
    if type(x)== list or type(x) == tuple:
        Inflation = list([0.2,x[0]])
        Unemployment = list([x[1],0.2])
        Ex_inflation = x[2]
    else: sys.exit("Error: The input is not a list or a tuple")
    #trying to make a slider where expected infation can be chosen
    test = plt.axes([0.25,0.1,0.65,0.03],facecolor="lightgoldenrodyellow")
    uEx_inflation = wig.Slider(test, label="Expected inflation",valmin=0.0,valmax=10,valinit=2,valstep=0.5)
    uEx_inflation.on_changed(update)
    if clear == False: 
        plotting(Unemployment,Inflation)
    else:
        plt.clf()
        plt.close()
        plotting(Unemployment,Inflation)

x = philipC(NatUnEm=2,Ex_inflation=4,alpha=0.3)

philipsPlot(x=x, clear=False)


