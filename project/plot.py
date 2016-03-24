try:
    import numpy as np
    import matplotlib.pyplot as plotting
except ImportError as error_message:
    print(error_message)
    exit(0)


def plotter(breakpoints, positions, diagram):
    ''' It is simple SFD plotter which is very very basic

        :param breakpoints - These are the points where in the SFD
                             f'(x)=0

        :param positions - Position along the bar where a breakpoint occurs

        :param diagram - The type of diagram(SFD or BMD)
   '''

    plotting.title(diagram + 'diagram')
    plotting.xlabel('Position along length of the member ->')
    plotting.ylabel(diagram + ' ->')

    plotting.scatter(positions, breakpoints)
    plotting.plot(positions, breakpoints)
    plotting.show()
