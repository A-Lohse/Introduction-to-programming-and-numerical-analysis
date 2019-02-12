import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.widgets as wig
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

def philipC(NatUnEm,Ex_inflation,alpha=0):
    if alpha == False:
        sys.exit("Error: You have to provide an alpha value")
    Inflation = 0.2
    UnEm = NatUnEm + (Ex_inflation - Inflation)/alpha
    Unemployment = 0.2
    Inflation = Ex_inflation - alpha*(Unemployment - NatUnEm)


    return list([UnEm,Inflation,Ex_inflation])


def PCplot(NatUnEm,Ex_inflation,alpha=0):
    x = philipC(NatUnEm,Ex_inflation,alpha) 
    plt.plot([0.2,x[0]],[x[1],0.2])
    plt.xlabel("Unemployment")
    plt.ylabel("Inflation")
    plt.xlim(0,5)
    plt.ylim(0,8)

%matplotlib inline
exi_slider = widgets.IntSlider(min=0,max=10,value=2,step=0.5)
interact(PCplot, Ex_inflation =  widgets.FloatSlider(min=0,max=5,value=2,step=0.2) ,NatUnEm = 2, alpha = 2)