def get_input(param_name):
    ''' Takes input from the user '''

    interact = 'Please enter the value of the parameter, ' + param_name + ':'
    param = input(interact)
    return param


def set_input():

    input_values = {}

    span = get_input('span')
    input_values.update({str(span):span})

    no_of_supports = int(get_input('no of supports'))
    supports = []
    for i in range(no_of_supports):
        print('FOR SUPPORT '+str(i+1))
        support = [get_input('support type'),
                   int(get_input('support postion'))]
        supports.append(support)
    input_values.update({str(supports):supports})

    no_of_UDLs = int(get_input('no of UDLs'))
    UDLs = []
    for i in range(no_of_UDLs):
        print('FOR UDL ' + str(i+1))
        UDL = [int(get_input('UDL value')),
               int(get_input('UDL start')), int(get_input('UDL end'))]
        UDLs.append(UDL)
    input_values.update({str(UDLs):UDLs})


    no_of_point_loads = int(get_input('no of point loads'))
    point_loads = []
    for i in range(no_of_point_loads):
        print('FOR POINT LOAD '+str(i+1))
        point_load = [int(get_input('Point Load value')),
                      int(get_input('Point Load position'))]
        point_loads.append(point_load)
    input_values.update({str(point_loads):point_loads})

    return input_values
