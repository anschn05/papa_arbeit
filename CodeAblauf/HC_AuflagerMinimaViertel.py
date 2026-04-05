import numpy as np
from math import sqrt

np.set_printoptions(threshold=np.inf)

def AuflagerMinima_viertel(t,tol,filename_MW):
    #t = 3.6
    #tol = 10e-4

    # filename_MW = f"{t}mm_messwerte.xyz"
    data = np.loadtxt(filename_MW)

    x_MW = data[:,0]
    y_MW = data[:,1]
    z_MW = data[:,2]

    step_square = len(z_MW)
    step = int(sqrt(step_square))

    l = int(x_MW[-1])
    b = int(y_MW[-1])
    #print(l,b)


    # step = 6
    # step_square = step**2
    # matrix = [[i+(step-j-1)*step for i in range(step)] for j in range(step)]
    # mat = np.array(matrix)
    # print(mat)

    # vierteln unser Gebiet in A = [0,l/2]x[0,b/2], B = [0,l/2]x[b/2,b], C = [l/2,l]x[0,b/2], D = [l/2,l]x[b/2,b]

    indexA = []
    indexB = []
    indexC = []
    indexD = []
    
    for i in range(step_square):
        if i < step*int((step+1)/2):
            if i%step < step/2:
                indexA.append(i)
            else: 
                indexB.append(i)
        else:
        #elif i >= step*int(step/2+1):
            if i%step <step/2:
                indexC.append(i)
            else:
                indexD.append(i)

    # suchen das minimum in jedem viertel
    minA = z_MW[indexA[0]]
    minB = z_MW[indexB[0]]
    minC = z_MW[indexC[0]]
    minD = z_MW[indexD[0]]

    for i in indexA:
        if z_MW[i] < minA:
            minA = z_MW[i]

    for i in indexB:
        if z_MW[i] < minB:
            minB = z_MW[i]

    for i in indexC:
        if z_MW[i] < minC:
            minC = z_MW[i]

    for i in indexD:
        if z_MW[i] < minD:
            minD = z_MW[i]

    #nun suchen 'verwandte' Punkte
    auflagerPunkte = [(0,0)]

    for i in indexA:
        if z_MW[i] < minA + tol:
            auflagerPunkte.append((float(x_MW[i]),float(y_MW[i])))

    for i in indexB:
        if z_MW[i] < minB + tol:
            auflagerPunkte.append((float(x_MW[i]),float(y_MW[i])))

    for i in indexC:
        if z_MW[i] < minC + tol:
            auflagerPunkte.append((float(x_MW[i]),float(y_MW[i])))

    for i in indexD:
        if z_MW[i] < minD + tol:
            auflagerPunkte.append((float(x_MW[i]),float(y_MW[i])))

    return auflagerPunkte



def AuflagerMinima(t,tol,filename_MW):
    #t = 3.6
    #tol = 10e-4

    #filename_MW = f"{t}mm_messwerte.xyz"
    data = np.loadtxt(filename_MW)

    x_MW = data[:,0]
    y_MW = data[:,1]
    z_MW = data[:,2]

    step_square = len(z_MW)     # anzahl an punkten
    step = int(sqrt(step_square))

    l = int(x_MW[-1])
    b = int(y_MW[-1])
    #print(l,b)


    Min = z_MW[0]
    #MinIndex = 0

    for i in range(step_square):
        if z_MW[i] < Min:
            Min = z_MW[i]
            #MinIndex = i

    #nun suchen wir 'verwandte' Punkte
    auflagerPunkte = [(0,0)]        # damit der Typ des arrays klar ist, '(0,0)' wird danach wieder geloescht


    for i in range(step_square):
        if z_MW[i] < Min + tol:
            auflagerPunkte.append((float(x_MW[i]),float(y_MW[i])))

    auflagerPunkte.pop(0)

    return auflagerPunkte
    

def AuflagerMaxima(t,tol,filename_MW):
    #t = 3.6
    #tol = 10e-4

    #filename_MW = f"{t}mm_messwerte.xyz"
    data = np.loadtxt(filename_MW)

    x_MW = data[:,0]
    y_MW = data[:,1]
    z_MW = data[:,2]

    step_square = len(z_MW)     # anzahl an punkten
    step = int(sqrt(step_square))

    l = int(x_MW[-1])
    b = int(y_MW[-1])
    #print(l,b)


    Max = z_MW[0]
    #MinIndex = 0

    for i in range(step_square):
        if z_MW[i] > Max:
            Max = z_MW[i]
            #MinIndex = i

    #nun suchen wir 'verwandte' Punkte
    auflagerPunkte = [(0,0)]        # damit der Typ des arrays klar ist, '(0,0)' wird danach wieder geloescht


    for i in range(step_square):
        if z_MW[i] > Max - tol:
            auflagerPunkte.append((float(x_MW[i]),float(y_MW[i])))

    auflagerPunkte.pop(0)

    return auflagerPunkte
    