E = 70          #GPs Elastizitätsmodul
v = 0.23        #Poisson-Zahl
h = 0.003       #m Glasdicke
p = 2500        #kg/m³ Dichte
g = 9.81        #m/s² Erdbeschleunigung
a = 1           #m Länge
b = 1           #m Breite

q = p * g * h
D = E*h**3/(12*(1-v**2))


#PDE: D*laplace²(w_g) = q         wobei w_g die krümmung durch erdbeschleunigung beschreibt


