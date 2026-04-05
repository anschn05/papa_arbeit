# Berechnung der Verwerfung einer Glasplatte ohne dem Einfluss von Gravitation
## Kirchhoff-Love mit der Hellan-Herrmann-Johnson-Methode

[Dokumentation](https://anschn05.github.io/papa_arbeit/)

1. Begonnen mit Simulation der Kirchhoff-Love PDE für Glasplatte mit folgenden Parametern:

l = 1100 #mm Länge
b = 360 #mm Breite
t  = 4     #mm Dicke

E  = 70e6      #Glas ~ N'/mm² Elastizitätsmodul      
nu = 0.23       #dimensionslos, also bei m und mm gleich
rho = 2.5e-6   #kg/mm³ Dichte 
g = 9810     # Erdbeschleunigung mm/s²

q = rho * t * g     #Eigengewicht der Platte punktweise!!!

der Code berechnet und visualisiert die Simulation und speichert die Ergebnisse auf einem bestimmten Gitter in einem *.xyz-File ab
siehe Code: mm_xyzFile_generieren_GRAv.ipynb

  ERROR: wollten ein *.xyz File mit errechneten (x,y,z)-Werten erstellen, wobei die z-Werte aus gf_w (ngSolve-Lsg) waren, mit Error 'out of domain'
  weil in ausgeschnittene Punktauflager gf_w nicht definiert 
  -> mittlerweile gelöst

3. Code geschrieben, der Startwerte generiert und in *.xyz-File speichert
siehe Code: mm_xyzFile_generieren_SW.ipynb

4. Code geschrieben, der Startwerte und Gravitationswerte (lsg von ngsolve) zusammenrechnet (Endwerte) und diese gemeinsam mit Startwerte und Gravitationswerte simuliert

siehe Code: mm_xyzFile_zusammenrechnen_EW.ipynb




# Auflager selber bestimmen
im Ordner 'KruemmungAnalyse_python', den Code 'Auflager_Hauptcode.ipynb' öffnen 
darin kannst du den Radius der Auflagerkreise und die Mittelpunkte der Kreise (Anzahl egal, mind. 1er, nicht zu groß) initialisieren

für neue *.xyz-files einfach den titel als string zu filename_MW schreiben - egl eh selbsterklärend

der rest sollte passen

dann 'Run'

wahrschienlich musst du dir davor noch die libraries: 
- ngsolve
- numpy
- matplotlib 
- ipympl 
installieren

# CODE STRUKTUR/Update

## wichtigeAlteFiles 
darin sind die wichtigsten Codeteile, wie Kirchhoff-Love lösen, Krümmungsanalyse, *.xyz-Files zusammenrechnen, usw. gesondernt/einzeln gespeichert, damit man sehen kann, wie diese funktionieren

## CodeAblauf
darin ist ein file "Hauptcode", womit man mithilfe eines messwerte-Files, alles einmal durchlaufen lässt, inkl. analyse der Auflager, berechnung der Gravitationsauswirkung, usw.
