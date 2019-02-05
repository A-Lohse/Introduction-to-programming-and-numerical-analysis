def philipsPlot(x,clear=False):
    if type(x) == list:
        Inflation = x[0]
        Unemployment = x[1]
        Inflation = list([0,inflation])
        Unemployment = list([Unemployment,0])
    else: 
        sys.exit("Error: The input is not a list")
    if clear == False:
        plotting(Inflaton,Unemployment)
    else: 
        plt.clf()
        plotting(Inflaiton,Unemployment)