from termcolor import colored

def get_input(param_name):
    ''' Takes input from the user '''

    interact = colored('Please enter the value of the parameter', 'green') + ', ' + colored(param_name, 'red') + ':'
    param = input(interact)
    return param


def set_input(args):
    ''' Returns a dict input_values containing all input values '''

    input_values = argshandler(args)
    keys = input_values.keys()

    if 'span' not in keys:
        span = int(get_input('span'))	
        input_values.update({'span':span})

    if 'supports' not in keys:
        no_of_supports = int(get_input('no of supports'))
        supports = []
        for i in range(no_of_supports):
            print('FOR SUPPORT '+str(i+1))
            support = [get_input('support type'),
                       0,
                       int(get_input('support position'))]
            supports.append(support)
        input_values.update({'supports':supports})

    if 'UDLs' not in keys:
        no_of_UDLs = int(get_input('no of UDLs'))
        UDLs = []
        for i in range(no_of_UDLs):
            print('FOR UDL ' + str(i+1))
            UDL = [int(get_input('UDL value')),
                   int(get_input('UDL start')), int(get_input('UDL end'))]
            UDLs.append(UDL)
        input_values.update({'UDLs':UDLs})

    if 'point_loads' not in keys:
        no_of_point_loads = int(get_input('no of point loads'))
        point_loads = []
        for i in range(no_of_point_loads):
            print('FOR POINT LOAD '+str(i+1))
            point_load = [int(get_input('point load value')),
                          int(get_input('point load position'))]
            point_loads.append(point_load)
        input_values.update({'point_loads':point_loads})

    return input_values

def get_support_value(supports):
    ''' Returns the total support value '''

    support_value = 0
    for support in supports:
        if(support[0]=='pin'):
            support_value +=1
        elif(support[0]=='fixed'):
            support_value +=3

    return support_value

def validate_input(input_values):
    ''' Validates input based on support input '''

    supports = input_values.get('supports')
    if(len(supports)>2):
        return False
    for support in supports:
        if(not support[0]==('pin' or 'fixed')):
            return False
    support_value = get_support_value(supports)
    if(not support_value==(2 or 3)):
        return False
    return True

def argshandler(args):

    input_values = {}
    for arg in args:
        if '-l=' in arg:
            input_values.update({'span':int(arg[3:])})
        elif '-s=' in arg:
            input_values.update({'supports':listconvert(arg[3:])})
        elif '-p=' in arg:
            input_values.update({'point_loads':listconvert(arg[3:])})
        elif '-u=' in arg:
            input_values.update({'UDLs':listconvert(arg[3:])})
        elif '-f=' in arg:
            input_values.update(fileconvert(arg[3:]))

    return input_values

def listconvert(string):

    bracket_count = 0
    input_list = []
    list_element = []
    element = ''
    for piece in string:
        if piece == '[':
            bracket_count+=1
        elif piece == ']':
            bracket_count-=1
        elif bracket_count == 1 and not piece==',':
            element += piece
        elif bracket_count ==1 and piece ==',':
            list_element.append(element)
            element =''
        if bracket_count == 0 and not piece==',':
            list_element.append(element)
            input_list.append(list_element)
            element = ''
            list_element = []
            
    return input_list

def fileconvert(textfile):

    input_values = {}
    f = open(textfile, 'r')
    lines = f.readlines()
    for line in lines:
        if 'span=' in line:
            input_values.update({'span':line.strip('span=')[:-1]})
        elif 'point_loads=' in line:
            input_values.update({'point_loads':listconvert(line.strip('point_loads=')[:-1])})
        elif 'UDLs=' in line:
            input_values.update({'UDLs':listconvert(line.strip('UDLs=')[:-1])})
        elif 'supports=' in line:
            input_values.update({'supports':listconvert(line.strip('supports=')[:-1])})

    return input_values
