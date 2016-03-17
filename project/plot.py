try:
    import numpy as np
    import matplotlib.pyplot as plotting
except ImportError as error_message:
    print (error_message)
    exit(0)


def plotter(breakpoints,position):
    ''' It is simple SFD plotter which is very very basic

        :param breakpoints - These are the points where in the SFD
                             f'(x)=0

        :param positions - Position along the bar where a breakpoint occurs
   '''
    
    plt.title('Shear force diagram')
    plt.xlabel('Position along length of the member ->')
    plt.ylabel('Shear force ->')
    
    plotting.scatter(dates,values)
    plotting.plot(dates,values)
    plotting.show()

