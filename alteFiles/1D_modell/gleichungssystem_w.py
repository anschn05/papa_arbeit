import sympy as sp
import numpy as np

def solve_constants(a,b,q,E,I):
    # Variablen
    #a, b, q, E, I, x = sp.symbols('a b q E I x')
    x = sp.symbols('x')

    c1A, c2A = sp.symbols('c1A c2A')
    c1B, c2B = sp.symbols('c1B c2B')
    c1C, c2C = sp.symbols('c1C c2C')

    # Durchbiegungsfunktionen
    wA = q/(24*E*I) * ((a+x)**4 + c1A*x + c2A)
    wB = q/(24*E*I) * (x**4 + 12*a**2*x**2 - 24*b*x**2 + c1B*x + c2B)
    wC = q/(24*E*I) * ((a-x)**4 + c1C*x + c2C)

    # Ableitungen
    wA_p = sp.diff(wA, x)
    wB_p = sp.diff(wB, x)
    wC_p = sp.diff(wC, x)

    # Gleichungen
    eq1 = sp.Eq(wA.subs(x, -b), 0)          # w(-b)=0
    eq2 = sp.Eq(wC.subs(x,  b), 0)          # w(b)=0

    eq3 = sp.Eq(wA.subs(x, -b), wB.subs(x, -b))   # w stetig bei -b
    eq4 = sp.Eq(wA_p.subs(x, -b), wB_p.subs(x, -b)) # w' stetig bei -b

    eq5 = sp.Eq(wB.subs(x,  b), wC.subs(x,  b))   # w stetig bei b
    eq6 = sp.Eq(wB_p.subs(x,  b), wC_p.subs(x,  b)) # w' stetig bei b

    # Gleichungssystem lösen
    solution = sp.solve([eq1, eq2, eq3, eq4, eq5, eq6],
                        [c1A, c2A, c1B, c2B, c1C, c2C])

    #print(solution)
    return solution

