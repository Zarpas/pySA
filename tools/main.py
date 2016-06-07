from tools.solve import get_sfd,get_bmd
from tools.takeinput import set_input
from tools.plot import plotter


def main():
    values = set_input()
    loads = []
    moments = []
    positions = []
    span = values.get('span')
    position = 0

    while (position<=span):
        loads.append(get_sfd(values, position))
        moments.append(get_bmd(values, position))
        positions.append(position)
        position+=float(span)/100

    plotter(loads, positions, 'Shear force')
    plotter(moments, positions, 'Bending Moment')
