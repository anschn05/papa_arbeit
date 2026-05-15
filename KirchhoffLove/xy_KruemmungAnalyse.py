import numpy as np
from math import sqrt,sin,pi
import matplotlib.pyplot as plt

#betrachtet Kruemmung entlang xAchse
# l = 1100
# b = 360
# t = 3.6
# step = 40
"""
wollen längs der x/y-Achse, auf Höhe von y/2 bzw x/2, also egl b/2 und l/2, die Krümmung analysieren 

wir bilden also einen Array mit (x,z) bzw (y,z) Werten, machen ein Circle-Fitting und analysieren die krümmung 
abhängig davon ob der erhaltene Kreismittelpunkt oberhalb der platte oder unterhalb liegt
"""
def Auflager_gemessen(step,filename_MW,tol):
    """
    diese Funktion arbeitet mit tatsächlichen Messwerten, greift in Form von *.xyz-Files darauf zu 
    """

    # region: aus XYZ-File:
    #filename_MW = f"{t}mm_messwerte.xyz"
    data_messwerte = np.loadtxt(filename_MW)

    array100 = np.full(1600,100)

    x_MW = data_messwerte[:,0]
    y_MW = data_messwerte[:,1]
    z_MW = (data_messwerte[:,2] - array100) * (-1)

    stepMitte = round((step+1)/2)      # breite/2, auf mittlerer höhe

    # Daten in x-Richtung:
    xStart = step*(stepMitte-1)
    xWerte = x_MW[xStart : (xStart + step)]
    z_xWerte = z_MW[xStart : (xStart + step)]

    # Daten in y-Richtung:
    yMitte = round((step+1)/2)      # breite/2, auf mittlerer höhe
    yWerte = [y_MW[yMitte+i*step] for i in range(step)]        
    z_yWerte = [z_MW[yMitte+i*step] for i in range(step)]
    #endregion

    # region: selbstgenerierte Werte
    """
    def f(x):
        return -10*sin(2*pi*x/l)

    xWerte = np.linspace(0,l,step)
    z_xWerte = [f(x) for x in x_xWerte]

    yWerte = np.linspace(0,b,step)
    z_yWerte = [f(y) for y in x_yWerte]
    """
    #endregion

    # region: PLOTTEN der Werte auf Linie: 
    plt.figure()
    plt.title("x-Richtung")
    plt.plot(xWerte,z_xWerte,color='green')
    plt.show()

    plt.figure()
    plt.title("y-Richtung")
    plt.plot(yWerte,z_yWerte,color='red')
    plt.show()
    #endregion


    # region: CIRCLE FITTING ALGORITHM
    """
    RECHNUNG:
    - Gleichung:
        (x-x_c)²+(y-y_c)² = r²
            <=>
        x²+y²+Dx+Ey+F = r² 
    - umwandeln zu:
        Dx+Ey+F = -(x²+y²)
        -> also LGS bzgl (D,E,F)
    D = -2x_c
    E = -2y_c
    F = x_c² + y_c² -r²

    - erhalten Mittelpunkt und Radius eines Kreises:
    x_c = -D/2
    y_c = -E/2
    r = sqrt(F-(x_c²+y_c²))
    """
    # xACHSE
    """
    hab einfach alle Variablen aus den getrennten Krümmungscodes zum Zusammenlegen 
    mit einem x bzw y davor initialisiert, nicht schoen, aber funktioniert :)
    """
    xz_Array = [ [float(x),float(z)] for x,z in zip(xWerte,z_xWerte) ]      # (x,z) entlang der linie

    xA_mat = np.matrix([   [entry[0],entry[1],1] for entry in xz_Array    ])        #ist bereits transponierte Matrix
    xAT_mat = np.matrix.transpose(xA_mat)
    xb_vec = [-(x**2+z**2) for (x,z) in xz_Array]

    # zu lösen: (AT*A)x = AT*b <=> x = (AT*A)^(-1)*AT*b
    xAT_A_mat = xAT_mat * xA_mat
    xAT_A_invers = np.linalg.inv(xAT_A_mat)
    xResult = xAT_A_invers * xAT_mat @ xb_vec
    # print(result)        # x = [D,E,F]

    xD = xResult[0,0]
    xE = xResult[0,1]
    xF = xResult[0,2]
    # endregion

    X_xMittelpunkt = -xD/2
    Z_xMittelpunkt = -xE/2
    xRadius = sqrt( ( X_xMittelpunkt**2 + Z_xMittelpunkt**2 ) - xF )

    print(f"xAchse:\n Mittelpunkt = ({X_xMittelpunkt},{Z_xMittelpunkt})\n Radius = {xRadius}\n")


    # yACHSE
    yz_Array = [ [float(y),float(z)] for y,z in zip(yWerte,z_yWerte) ]      # (x,z) entlang der linie

    yA_mat = np.matrix([   [entry[0],entry[1],1] for entry in yz_Array    ])        #ist bereits transponierte Matrix
    yAT_mat = np.matrix.transpose(yA_mat)
    yb_vec = [-(x**2+z**2) for (x,z) in yz_Array]


    # zu lösen: (AT*A)x = AT*b <=> x = (AT*A)^(-1)*AT*b
    yAT_A_mat = yAT_mat * yA_mat
    yAT_A_invers = np.linalg.inv(yAT_A_mat)
    yResult = yAT_A_invers * yAT_mat @ yb_vec

    yD = yResult[0,0]
    yE = yResult[0,1]
    yF = yResult[0,2]
    # endregion

    X_yMittelpunkt = -yD/2
    Z_yMittelpunkt = -yE/2
    yRadius = sqrt( ( X_yMittelpunkt**2 + Z_yMittelpunkt**2 ) - yF )

    print(f"yAchse:\n Mittelpunkt = ({X_yMittelpunkt},{Z_yMittelpunkt})\n Radius = {yRadius}\n")

    # daraus analysieren, ob positiv oder negativ gekrümmt
    #tol = 10e-11        # bei sinus-kurve ab 10e-12 meinte negativ gekrümmt, also ab dieser toleranz falsch

    # xACHSE
    KruemmungResult = [0,0]
    if Z_xMittelpunkt >= tol:           # positiv gekrümmt
        KruemmungResult[0] = 1
    elif Z_xMittelpunkt <= -tol:        # negativ gekrümmt
        KruemmungResult[0] = -1
    else:                               # keine Aussage möglich
        KruemmungResult[0] = 0 # bleibt null

    # yACHSE
    if Z_yMittelpunkt >= tol:           # positiv gekrümmt
        KruemmungResult[1] = 1
    elif Z_yMittelpunkt <= -tol:        # negativ gekrümmt
        KruemmungResult[1] = -1
    else:                               # keine Aussage möglich
        KruemmungResult[1] = 0 # bleibt null

    print(KruemmungResult)

    return KruemmungResult


def Auflager_generiert(l,b,step,tol):
    """
    diese Funktion generiert sich selbst Werte, anhand einer Funktion 'f'
    """

    # region: aus XYZ-File:
    #filename_MW = f"{t}mm_messwerte.xyz"
    # data_messwerte = np.loadtxt(filename_MW)

    # array100 = np.full(1600,100)

    # x_MW = data_messwerte[:,0]
    # y_MW = data_messwerte[:,1]
    # z_MW = data_messwerte[:,2] - array100

    # stepMitte = round((step+1)/2)      # breite/2, auf mittlerer höhe

    # # Daten in x-Richtung:
    # xStart = step*(stepMitte-1)
    # xWerte = x_MW[xStart : (xStart + step)]
    # z_xWerte = z_MW[xStart : (xStart + step)]

    # # Daten in y-Richtung:
    # yMitte = round((step+1)/2)      # breite/2, auf mittlerer höhe
    # yWerte = [y_MW[yMitte+i*step] for i in range(step)]        
    # z_yWerte = [z_MW[yMitte+i*step] for i in range(step)]
    #endregion

    # region: selbstgenerierte Werte
    
    def f(x):
        return -10*sin(2*pi*x/l)

    xWerte = np.linspace(0,l,step)
    z_xWerte = [f(x) for x in xWerte]

    yWerte = np.linspace(0,b,step)
    z_yWerte = [f(y) for y in yWerte]
    
    #endregion

    # region: PLOTTEN der Werte auf Linie: 
    plt.figure()
    plt.title("x-Richtung")
    plt.plot(xWerte,z_xWerte,color='green')
    plt.show()

    plt.figure()
    plt.title("y-Richtung")
    plt.plot(yWerte,z_yWerte,color='red')
    plt.show()
    #endregion


    # region: CIRCLE FITTING ALGORITHM
    """
    RECHNUNG:
    - Gleichung:
        (x-x_c)²+(y-y_c)² = r²
            <=>
        x²+y²+Dx+Ey+F = r² 
    - umwandeln zu:
        Dx+Ey+F = -(x²+y²)
        -> also LGS bzgl (D,E,F)
    D = -2x_c
    E = -2y_c
    F = x_c² + y_c² -r²

    - erhalten Mittelpunkt und Radius eines Kreises:
    x_c = -D/2
    y_c = -E/2
    r = sqrt(F-(x_c²+y_c²))
    """
    # xACHSE
    """
    hab einfach alle Variablen aus den getrennten Krümmungscodes zum Zusammenlegen 
    mit einem x bzw y davor initialisiert, nicht schoen, aber funktioniert :)
    """
    xz_Array = [ [float(x),float(z)] for x,z in zip(xWerte,z_xWerte) ]      # (x,z) entlang der linie

    xA_mat = np.matrix([   [entry[0],entry[1],1] for entry in xz_Array    ])        #ist bereits transponierte Matrix
    xAT_mat = np.matrix.transpose(xA_mat)
    xb_vec = [-(x**2+z**2) for (x,z) in xz_Array]

    # zu lösen: (AT*A)x = AT*b <=> x = (AT*A)^(-1)*AT*b
    xAT_A_mat = xAT_mat * xA_mat
    xAT_A_invers = np.linalg.inv(xAT_A_mat)
    xResult = xAT_A_invers * xAT_mat @ xb_vec
    # print(result)        # x = [D,E,F]

    xD = xResult[0,0]
    xE = xResult[0,1]
    xF = xResult[0,2]
    # endregion

    X_xMittelpunkt = -xD/2
    Z_xMittelpunkt = -xE/2
    xRadius = sqrt( ( X_xMittelpunkt**2 + Z_xMittelpunkt**2 ) - xF )

    print(f"xAchse:\n Mittelpunkt = ({X_xMittelpunkt},{Z_xMittelpunkt})\n Radius = {xRadius}\n")


    # yACHSE
    yz_Array = [ [float(y),float(z)] for y,z in zip(yWerte,z_yWerte) ]      # (x,z) entlang der linie

    yA_mat = np.matrix([   [entry[0],entry[1],1] for entry in yz_Array    ])        #ist bereits transponierte Matrix
    yAT_mat = np.matrix.transpose(yA_mat)
    yb_vec = [-(x**2+z**2) for (x,z) in yz_Array]


    # zu lösen: (AT*A)x = AT*b <=> x = (AT*A)^(-1)*AT*b
    yAT_A_mat = yAT_mat * yA_mat
    yAT_A_invers = np.linalg.inv(yAT_A_mat)
    yResult = yAT_A_invers * yAT_mat @ yb_vec

    yD = yResult[0,0]
    yE = yResult[0,1]
    yF = yResult[0,2]
    # endregion

    X_yMittelpunkt = -yD/2
    Z_yMittelpunkt = -yE/2
    yRadius = sqrt( ( X_yMittelpunkt**2 + Z_yMittelpunkt**2 ) - yF )

    print(f"yAchse:\n Mittelpunkt = ({X_yMittelpunkt},{Z_yMittelpunkt})\n Radius = {yRadius}\n")

    # daraus analysieren, ob positiv oder negativ gekrümmt
    #tol = 10e-11        # bei sinus-kurve ab 10e-12 meinte negativ gekrümmt, also ab dieser toleranz falsch

    # xACHSE
    KruemmungResult = [0,0]
    if Z_xMittelpunkt >= tol:           # positiv gekrümmt
        print("positiv gekrümmt")
        KruemmungResult[0] = 1
    elif Z_xMittelpunkt <= -tol:
        print("negativ gekrümmt")       # negativ gekrümmt
        KruemmungResult[0] = -1
    else:
        print("keine Aussage möglich")  # keine Aussage möglich
        #KruemmungResult[0] = 0 # bleibt null

    # yACHSE
    if Z_yMittelpunkt >= tol:           # positiv gekrümmt
        print("positiv gekrümmt")
        KruemmungResult[1] = 1
    elif Z_yMittelpunkt <= -tol:
        print("negativ gekrümmt")       # negativ gekrümmt
        KruemmungResult[1] = -1
    else:
        print("keine Aussage möglich")  # keine Aussage möglich
        #KruemmungResult[1] = 0 # bleibt null

    print(KruemmungResult)

    return KruemmungResult