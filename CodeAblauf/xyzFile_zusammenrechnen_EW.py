import numpy as np
import matplotlib.pyplot as plt

#Maße in MILLIMETER
# l = 1100
# b = 360
# t = 3.6
# step = 40
# filename_MW = f"{t}mm_messwerte.xyz"
# filename_GRAV = f"{t}mm_gravitation.xyz"



def plotten(l,b,t,step,filename_MW,filename_GRAV):

    data_MW = np.loadtxt(filename_MW)

    data_GRAV = np.loadtxt(filename_GRAV)

    #startwerte/messwerte
    array100 = np.full(1600,100)
    x_MW = data_MW[:,0]
    y_MW = data_MW[:,1]
    z_MW = data_MW[:,2] - array100
    #gravitationswerte
    x_GRAV = data_GRAV[:,0]
    y_GRAV = data_GRAV[:,1]
    z_GRAV = data_GRAV[:,2]
    #endwerte
    x_EW = x_GRAV
    y_EW = y_GRAV
    z_EW = z_MW - z_GRAV

    np.set_printoptions(threshold=np.inf)

    filename_EW = f"{t}mm_endwerte.xyz"
    with open(filename_EW, "w") as f:
        for i in range(len(x_EW)):
            x, y, w = x_EW[i],y_EW[i],z_EW[i]
            f.write(f"{x:.6f}\t{y:.6f}\t{w:.6e}\n")


    # Raster erzeugen
    #%matplotlib ipympl
    X = np.unique(x_GRAV)
    Y = np.unique(y_GRAV)

    X, Y = np.meshgrid(X, Y)
    Z_MW=z_MW.reshape(len(Y), len(X))
    Z_GRAV=z_GRAV.reshape(len(Y), len(X))
    Z_EW=z_EW.reshape(len(Y), len(X))

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X, Y,Z_MW,color="red")          # startwerte
    # ax.plot_surface(X, Y,Z_GRAV,color="blue")       # gravitation
    # ax.plot_surface(X, Y,Z_EW,color="green")        # endwerte
    ax.view_init(elev=10, azim=-75)

    fig2, ax2 = plt.subplots()
    #y_mid = round(len(Y)/2)
    y_mid = round(step/2)

    ax2.plot(X[y_mid,:], Z_MW[y_mid,:],   'r', label='Startwerte')
    # ax2.plot(X[y_mid,:], Z_GRAV[y_mid,:], 'b', label='Gravitation')
    # ax2.plot(X[y_mid,:], Z_EW[y_mid,:],   'g', label='Endwerte')
    ax2.legend()
    ax2.grid(True,alpha=0.5) #,which="major",alpha=0.2)

    #TODO höchster Wert abhängig von Auflagerort
    # print(f"Länge={l}mm, Breite={b}mm, Dicke={t}mm")
    # print('\nHöchster Wert:')

    # interessanterIndex = 0 #round(step/2)
    # print(' startwert:  ', z_EW[interessanterIndex])
    # print(' gravitation:', round(z_GRAV[interessanterIndex],4))
    # print(' endwert:    ', round(z_EW[interessanterIndex],4))
    # print("SOLLWERT 0.015\n")
    # print(' Endwert - Startwert:    ',z_EW[interessanterIndex] - z_MW[interessanterIndex])
    # print(' prozentuelle Änderung:    ', round(((100/z_MW[interessanterIndex]) * z_EW[interessanterIndex]),2),'%')

    plt.show()

