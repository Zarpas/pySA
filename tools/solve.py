def get_sfd(input_values, x):
    ''' Take input and position on the bar and gets the resulting sfd.

        :param input_values: Dict containing all the values given at input.

        :param x: position along the length of the bar.

    '''

    sfd = 0
    udls = input_values.get('UDLs')
    for i in range(len(udls)):
        udl = udls[i]
        if (udl[1]<=x and min(x,udl[2])<=x):
            sfd += udl[0]*(min(x,udl[2])-udl[1])
    
    point_loads = input_values.get('point_loads')
    for i in range(len(point_loads)):
        point_load = point_loads[i]
        if (point_load[1]<=x):
            sfd += point_load[0]

    return sfd

def get_bmd(input_values, x): 
    ''' Take input and position on the bar and gets the resulting bmd.

        :param input_values: Dict containing all the values given at input.

        :param x: position along the length of the bar.

    '''

    bmd = 0
    udls = input_values.get('UDLs')
    for i in range(len(udls)):
        udl = udls[i]
        if (max(x,udl[1])>=x and udl[2]>=x):
            bmd += udl[0]*(udl[2]-max(x, udl[1]))*((udl[2]+max(x, udl[1]))/2 -x)
    
    point_loads = input_values.get('point_loads')
    for i in range(len(point_loads)):
        point_load = point_loads[i]
        if (point_load[1]>=x):
            bmd += point_load[0]*(point_load[1]-x)

    return bmd
