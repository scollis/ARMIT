import matplotlib.pyplot as plt
import datetime as dt

def generic_plot(arm_obj,**kwargs):
    '''Function used to plot up data from the X-ARRAY dataset passed
       to it along with the corresponding features
       Keywords:
       xvariable - Variable names for the x-axis.  Defaults to time if none
       yvariable - Variable names for the y-axis.  Required

       plot_number - which panel the variable should be on,starting with 1
       axis - Define which axis the variable should be plotted on
       psym - Plotting symbol to use for each variable.  Defaults to line
       imagename - sub name for the plot... ie sgpmetE13.b1.subname.20180101.png

       issues: The git repo was corrupted with Justin's commit after Ken's. 
       Somehow some lines of code added by Ken were removed with Justin's commit.
       Most of those are back but some issues remain. 

       Adding a datastream-variable to the object works for data values and dimension
       name, but the attributes are not added with add_ds_var(). Because of this 
       the yaxis does not have a value because no units.

       For over plotting the failing qc issues with knowing when a variable's 
       qc is qc_variable vs datastream-qc_variable. 

 
     '''

    #Look for required variabels
    try:
        variable = kwargs['variable']
        if not isinstance(variable, (list, tuple)): variable = [variable]
    except:
        raise ValueError('variable not defined')

    ydata = arm_obj[variable].to_array()[0]
    xdim = list(arm_obj[variable].dims)
    xdata = arm_obj[xdim[0]]

    print(ydata.shape,xdata.shape)

    nps = len(variable)
    fig, axs = plt.subplots(nps,1,figsize=(10,2*nps))
    for i, var in enumerate(variable):
        axs.plot(xdata,ydata)
 
