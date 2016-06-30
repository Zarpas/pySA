def solve_sfd(input_values):

    print('SHEAR FORCE DIAGRAM\n')
    print('To draw a Shear Force Diagram, first solve the shear reactions at supports. Then from the left end of the beam, consider the sum of shear force acting upto that point. Plot the shear force corresponding to its position along the beam. Continue by taking small intervals along the beam till you reach the right end.\n')
    position = float(input_values.get('span'))/2
    print('For example, let us find Shear Force at '+str(position)+'\n')
    sfd = ''
    sfd_value = 0
    ploads = input_values.get('point_loads')
    udls = input_values.get('UDLs')
    supports = input_values.get('supports')
    for pload in ploads:
        if(pload[1]<=position):
            sfd+=str(pload[0])+' + '
            sfd_value += float(pload[0])
    for udl in udls:
        if (float(udl[1])<=position and min(position,float(udl[2]))<=position):
            sfd += str(udl[0])+'*'+'('+str(min(position,float(udl[2])))+'-'+str(udl[1])+')'+' + '
            sfd_value += float(udl[0])*(min(position,float(udl[2]))-float(udl[1]))
    for support in supports:
        if(support[0]=='pin' and support[2]<=position):
            sfd += str(-support[1])+' + '
            sfd_value -= support[1]
        
    print('Shear Force = '+sfd[:-3])
    print('Shear Force = '+str(sfd_value)+'\n')

def solve_bmd(input_values):

    print('BENDING MOMENT DIAGRAM\n')
    print('To draw a Bending Moment Diagram, first solve the moment reactions at supports. Then from the left end of the beam, consider few points at some interval till you reach the right end of the beam. Sum up the bending moments from the point to the right end of the beam. Plot the Bending Moment to its corresponding position on the beam.ou reach the right end.\n')
    position = float(input_values.get('span'))/2
    print('For example, let us find Bending Moment at '+str(position)+'\n')
    bmd=''
    bmd_value=0
    ploads = input_values.get('point_loads')
    udls = input_values.get('UDLs')
    supports = input_values.get('supports')
    for pload in ploads:
        if (pload[1]>=position):
            bmd += str(pload[0])+'*'+'('+str(pload[1])+'-'+str(position)+')'+' + '
            bmd_value += float(pload[0])*(float(pload[1])-position)
    for udl in udls:
        if (max(position,float(udl[1]))>=position and float(udl[2])>=position):
             pass
             bmd += str(udl[0])+'*'+'('+str(udl[2])+'-'+str(max(position, float(udl[1])))+')'+'*'+'('+'('+str(udl[2])+'+'+str(max(position, float(udl[1])))+')/2'+'-'+str(position)+')'+' + '
             bmd_value += float(udl[0])*(float(udl[2])-max(position, float(udl[1])))*((float(udl[2])+max(position, float(udl[1])))/2 -position)
    for support in supports:
        if(support[0]=='fixed' and support[2]>=position):
            bmd += str(support[1])+' + '
            bmd_value += support[1]
        if(support[0]=='pin' and support[2]>=position):
            bmd += str(support[1])+'*'+'('+str(support[2])+'-'+str(position)+')'+' + '
            bmd_value = support[1]*(support[2]-position) - bmd_value

    print('Bending Moment = '+bmd[:-3])
    print('Bending Moment = '+str(bmd_value)+'\n')

def solve_reactions(input_values):

    print('SOLVING SUPPORT REACTIONS\n')
    reactions = input_values.get('supports')
    if(len(reactions)==1):
        print("R1 =")
    elif(len(reactions)==2):
        ploads = input_values.get('point_loads')
        udls = input_values.get('UDLs')
        line1 = ''
        line2 = ''
        value1 = 0
        value2 = 0
        for pload in ploads:
            line1+=str(pload[0]) + ' + '
            value1+=pload[0]
            line2+= str(pload[0])+'*'+'('+str(pload[1])+'-'+str(reactions[0][2])+')'+' + '
            value2+= pload[0]*(pload[1]-reactions[0][2])
        for udl in udls:
            line1+=str(udl[0])+'*'+'('+str(udl[2])+'-'+str(udl[1])+')'+' + '
            value1+=udl[0]*(udl[2]-udl[1])
            line2+=str(udl[0])+'*'+'('+str(udl[2])+'-'+str(udl[1])+')'+'*'+'('+'('+str(udl[1])+'+'+str(udl[2])+')/2'+'-'+str(reactions[0][2])+')'+' + '
            value2+=udl[0]*(udl[2]-udl[1])*(float((udl[1]+udl[2]))/2-reactions[0][2])
        print('R1 + R2 = '+line1[:-3])
        print('R1 + R2 = '+str(value1)+' -> Equation1')
        print('')
        print('R2'+'*'+'('+str(reactions[1][2])+'-'+str(reactions[0][2])+')'+' = '+line2[:-3]+' -> Equation2')
        print('R2'+' = '+str(float(value2)/(reactions[1][2]-reactions[0][2]))+' -> From Equation2')
        print('')
        print('Using Equation1')
        print('R1'+' = '+str(value1)+'-'+'R2')
        print('Therefore, '+'R1'+' = '+str(value1-(float(value2)/(reactions[1][2]-reactions[0][2]))))
        print('')
