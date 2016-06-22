from solve import get_sfd, get_bmd, get_support_reactions
from takeinput import set_input, validate_input
from plot import plotter
from report import printfile

def main():

    values = set_input()
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
        while (position<=span):
            load = 0
            moment = 0
            if(len(reactions)==2):
                if(position<=reaction1[2]):
                    load += reaction1[1]
                    moment += reaction1[1]*(reaction1[2]-position)
                if(position<=reaction2[2]):
                    load += reaction2[1]
                    moment += reaction2[1]*(reaction2[2]-position)
            elif(len(reactions)==1):
                if(position<=reaction[2]):
                    moment = reaction[1]
            loads.append(load-get_sfd(values, position))
            moments.append(moment-get_bmd(values, position))
            positions.append(position)
            position+=float(span)/100

        sfd = open('../notes/sfd.txt')
        bmd = open('../notes/bmd.txt')

        printfile(sfd)
        plotter(loads, positions, 'Shear force')
        printfile(bmd)
        plotter(moments, positions, 'Bending Moment')

main()
