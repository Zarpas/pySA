from takeinput import get_support_value

def get_sfd(input_values, x):
    ''' Take input and position on the bar and gets the resulting sfd.

        :param input_values: Dict containing all the values given at input.

        :param x: position along the length of the bar.

    '''

    sfd = 0
    udls = input_values.get('UDLs')
    for i in range(len(udls)):
        udl = udls[i]
        if (float(udl[1])<=x and min(x,float(udl[2]))<=x):
            sfd += float(udl[0])*(min(x,float(udl[2]))-float(udl[1]))
    
    point_loads = input_values.get('point_loads')
    for i in range(len(point_loads)):
        point_load = point_loads[i]
        if(float(point_load[1])<=float(x)):
            sfd += float(point_load[0])

    return sfd

def get_bmd(input_values, x): 
    ''' 
        Take input and position on the bar and gets the resulting bmd.

        :param input_values: Dict containing all the values given at input.

        :param x: position along the length of the bar.

    '''

    bmd = 0
    udls = input_values.get('UDLs')
    for i in range(len(udls)):
        udl = udls[i]
        if (max(x,float(udl[1]))>=x and float(udl[2])>=x):
            bmd += float(udl[0])*(float(udl[2])-max(x, float(udl[1])))*((float(udl[2])+max(x, float(udl[1])))/2 -x)
    
    point_loads = input_values.get('point_loads')
    for i in range(len(point_loads)):
        point_load = point_loads[i]
        if (float(point_load[1])>=x):
            bmd += float(point_load[0])*(float(point_load[1])-x)

    return bmd

def get_support_reactions(input_values):

    supports = input_values.get('supports')
    total_force = get_sfd(input_values, input_values.get('span'))
    if(get_support_value(supports)==2):
        support1 = supports[0]
        support2 = supports[1]
        support2[1] = float(get_bmd(input_values, support1[2]))/(support2[2]-support1[2])
        support1[1] = total_force - support2[1]
        return support1, support2
    elif(get_support_value(supports)==3):
        support = supports[0]
        support[1] = get_bmd(input_values, support[2])
    return support
