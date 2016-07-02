from tools.solve import get_sfd, get_bmd, get_support_reactions
from tools.takeinput import set_input, validate_input
from tools.plot import plotter
from tools.report import solve_reactions, solve_sfd, solve_bmd
from termcolor import colored
import sys

def main():

    try:
        values = set_input(sys.argv)
        if(validate_input(values)):
            loads = []
            moments = []
            positions = []
            span = values.get('span')
            position = 0
            reactions = get_support_reactions(values)
            if(len(reactions)==2):
                reaction1 = reactions[0]
                reaction2 = reactions[1]
            if(len(reactions)==1):
                reaction = reactions[0]
            while (position<=float(span)):
                load = 0
                moment = 0
                if(len(reactions)==2):
                    if(position>=float(reaction1[2])):
                        load += float(reaction1[1])
                    if(position<=float(reaction1[2])):
                        moment += float(reaction1[1])*(float(reaction1[2])-position)
                    if(position>=float(reaction2[2])):
                        load += float(reaction2[1])
                    if(position<=float(reaction2[2])):
                        moment += float(reaction2[1])*(float(reaction2[2])-position)
                elif(len(reactions)==1):
                    if(position>=float(reaction[2])):
                        load = get_sfd(values, float(values.get('span')))
                    if(position<=float(reaction[2])):
                        moment = float(reaction[1])
                loads.append(load-get_sfd(values, position))
                moments.append(moment-get_bmd(values, position))
                positions.append(position)
                position+=float(span)/100
            solve_reactions(values)
            solve_sfd(values)
            plotter(loads, positions, 'Shear force')
            solve_bmd(values)
            plotter(moments, positions, 'Bending Moment')
    except:
        print(colored('Please give a valid input! Try again', 'red'))
