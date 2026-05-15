import numpy as np
from math import sqrt

"""
15.5
der Code definiert auf versch. Arten die Auflager

AuflagerViertel gelöscht!!!
"""
np.set_printoptions(threshold=np.inf)


def AuflagerMaxMin(t,tol,filename_MW,Vorzeichen="Max"):
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

    if Vorzeichen == "Min":
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

    elif Vorzeichen == "Max":
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
    

# alte Funktionen, mittlerweile mithilfe von AuflagerMaxMin kombiniert: 
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
    