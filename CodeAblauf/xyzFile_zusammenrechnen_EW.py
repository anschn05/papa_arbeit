import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv
pv.set_jupyter_backend(None)


#Maße in MILLIMETER
# l = 1100
# b = 360
# t = 3.6
# step = 40
# filename_MW = f"{t}mm_messwerte.xyz"
# filename_GRAV = f"{t}mm_gravitation.xyz"



def plotten(l,b,t,step,filename_MW,filename_GRAV,Vorzeichen):

    data_MW = np.loadtxt(filename_MW)

    data_GRAV = np.loadtxt(filename_GRAV)

    if Vorzeichen == "Max":
    #startwerte/messwerte
        # array100 = np.full(1600,100)
        # x_MW = data_MW[:,0]
        # y_MW = data_MW[:,1]
        z_MW = -(data_MW[:,2])
    if Vorzeichen == "Min":
        #startwerte/messwerte
        # x_MW = data_MW[:,0]
        # y_MW = data_MW[:,1]
        z_MW = (data_MW[:,2])

    #gravitationswerte
    x_GRAV = data_GRAV[:,0]
    y_GRAV = data_GRAV[:,1]
    z_GRAV = data_GRAV[:,2]
    #endwerte
    x_EW = x_GRAV
    y_EW = y_GRAV
    z_EW = z_MW + z_GRAV



    np.set_printoptions(threshold=np.inf)

    filename_EW = f"{t}mm_endwerte.xyz"
    with open(filename_EW, "w") as f:
        for i in range(len(x_EW)):
            x, y, w = x_EW[i],y_EW[i],z_EW[i]
            f.write(f"{x:.6f}\t{y:.6f}\t{w:.6e}\n")


    # Raster erzeugen
    #%matplotlib ipympl
    X_unique = np.unique(x_GRAV)
    Y_unique = np.unique(y_GRAV)

    X, Y = np.meshgrid(X_unique, Y_unique)

    Z_MW = z_MW.reshape(len(Y), len(X))
    Z_GRAV = z_GRAV.reshape(len(Y), len(X))
    Z_EW = z_EW.reshape(len(Y), len(X))

    # 3D PLOT ---- PyVista
    grid_MW = pv.StructuredGrid(X, Y, Z_MW)
    grid_GRAV = pv.StructuredGrid(X, Y, Z_GRAV)
    grid_EW = pv.StructuredGrid(X, Y, Z_EW)

    plotter = pv.Plotter()
    plotter.set_scale(1, 1, 7)  # Y-Achse gestaucht

    plotter.add_mesh(grid_MW, color="red", opacity=0.9, label="Startwerte")
    plotter.add_mesh(grid_GRAV, color="blue", opacity=0.9, label="Gravitation")
    plotter.add_mesh(grid_EW, color="green", opacity=0.9, label="Endwerte")

    plotter.add_axes()
    plotter.add_legend()

    plotter.show(jupyter_backend=None)

    # 3D PLOT ---- matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X, Y,Z_MW,color="red")          # startwerte
    ax.plot_surface(X, Y,Z_GRAV,color="blue")       # gravitation
    ax.plot_surface(X, Y,Z_EW,color="green")        # endwerte
    ax.view_init(elev=10, azim=-75)

    # 2D PLOT entlang x achse
    figY, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(20,5))
    #fig1, ax1 = plt.subplots()
    ax1.set_title("x=0")

    ax1.plot(X[0,:], Z_MW[0,:],   'r', label='Startwerte')
    ax1.plot(X[0,:], Z_GRAV[0,:], 'b', label='Gravitation')
    ax1.plot(X[0,:], Z_EW[0,:],   'g', label='Endwerte')
    ax1.legend()
    ax1.grid(True,alpha=0.5) #,which="major",alpha=0.2)

    #fig2, ax2 = plt.subplots()
    ax2.set_title("x=mitte")

    #y_mid = round(len(Y)/2)
    y_mid = round(step/2)

    ax2.plot(X[y_mid,:], Z_MW[y_mid,:],   'r', label='Startwerte')
    ax2.plot(X[y_mid,:], Z_GRAV[y_mid,:], 'b', label='Gravitation')
    ax2.plot(X[y_mid,:], Z_EW[y_mid,:],   'g', label='Endwerte')
    ax2.legend()
    ax2.grid(True,alpha=0.5) #,which="major",alpha=0.2)

    #fig3, ax3 = plt.subplots()
    ax3.set_title("x=l (ende/hinten)")

    ax3.plot(X[-1,:], Z_MW[-1,:],   'r', label='Startwerte')
    ax3.plot(X[-1,:], Z_GRAV[-1,:], 'b', label='Gravitation')
    ax3.plot(X[-1,:], Z_EW[-1,:],   'g', label='Endwerte')
    ax3.legend()
    ax3.grid(True,alpha=0.5) #,which="major",alpha=0.2)



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

    return filename_EW