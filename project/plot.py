try:
    import numpy as np
    import matplotlib.pyplot as plotting
except ImportError as error_message:
    print(error_message)
    exit(0)


def plotter(stress_points, positions, diagram):
    ''' It is simple SFD and BMD plotter.

        :param stress_points - Stress at a position along the bar.

        :param positions - Position along the bar where a breakpoint occurs.

        :param diagram - The type of diagram(SFD or BMD).
   '''

    plotting.title(diagram + 'diagram')
    plotting.xlabel('Position along length of the member ->')
    plotting.ylabel(diagram + ' ->')

    plotting.scatter(positions, stress_points)
    plotting.plot(positions, stress_points)
    plotting.show()
