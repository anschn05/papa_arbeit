import numpy as np
from math import sqrt


def Analyse_EW(filename_EW):

    data_EW = np.loadtxt(filename_EW)

    x_EW = data_EW[:,0]
    y_EW = data_EW[:,1]
    z_EW = data_EW[:,2]

    # step wird aus Messwerte-File entnommen
    step_square = len(data_EW[:,0])
    if sqrt(step_square)%1 != 0:
        raise ValueError("the Length of the *.xyz-File is not suitable, it should be step*step")

    step = int(sqrt(step_square))

    # Laenge/Breite wird aus Messwerte-File entnommen
    l = int(data_EW[-1,0])   #achtung: -1 steht hier für die letzte Zeile, 0 für den x eintrag, 1 für den y eintrag
    b = int(data_EW[-1,1])

    Min = z_EW[0]       # Wert wirds unmoeglich
    Max = z_EW[0]      # Wert wirds unmoeglich
    for i in range(step):
        if z_EW[i] > Max:
            Max = z_EW[i]
        if z_EW[i] < Min:
            Min = z_EW[i]
        continue

    MaxDifferenz = Max - Min

    print(MaxDifferenz)

    return MaxDifferenz