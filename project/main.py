from solve import get_sfd
from takeinput import set_input
from plot import plotter

values = set_input()
stress_points = []
positions = []
span = values.get('span')
position = 0

while (position<=span):
    stress_points.append(get_sfd(values, position))
    positions.append(position)
    position+=1

plotter(stress_points, positions, 'SFD')
