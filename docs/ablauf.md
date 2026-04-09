# Ablauf Entwicklung

## Gravitations-Code
### 1. 1D-Modell
Ich habe begonnen die Verwerfung unserer Glasplatte als 1D Problem zu betrachten und geloest, um ein bisschen in die Thematik der Mechanik und Physik zu kommen.
Wichtige Erkenntnisse waren fuer mich, die Wichtigkeit zu wissen, ob Kraefte punktuell oder in unserem Fall flaechendeckend, in unserem Fall gleichmaeßig auftreten.


### 2. Kirchhoff-Love
Den 2D Code habe ich in VS-Code mit python insbesondere NGSolve geschrieben. Ich habe eine super Dokumentation der KL-Gleichung auf NGSolve-docs gefunden, die ich relativ aehnlich nachgearbeitet habe.

fuer Glas verwendete Parameter:
```
l = 1100 #mm Laenge
b = 360 #mm Breite
t  = 4     #mm Dicke

E  = 70e6      #Glas ~ N'/mm² Elastizitaetsmodul      
nu = 0.23       #dimensionslos, also bei m und mm gleich
rho = 2.5e-6   #kg/mm³ Dichte 
g = 9810     # Erdbeschleunigung mm/s²

q = rho * t * g     #Eigengewicht der Platte punktweise!!!
```

>ERROR: wollten ein *.xyz File mit errechneten (x,y,z)-Werten erstellen, wobei die z-Werte aus gf_w (ngSolve-Lsg) waren, mit Error 'out of domain' weil in ausgeschnittene Punktauflager gf_w nicht definiert -> mittlerweile geloest


### 3. Testwerte/Zusammenrechnen
Ich habe mir Startwerte (SW) generiert, die Auflager definiert und mit den aus dem Gravitations-Code (KL-Code) erhaltenen Daten (GravW) zusammengerechnet -> Endwerte (EW) erhalten

SW, GravW und EW visualisiert


### 4. Messwerte
von Papa echte Messwerte (MW) einer Platte erhalten und getestet

Achtung: von nun an ist im Dateinamen der Daten immer die Dicke der getesteten Platte inkludiert
zB. 
- '3.6mm_messwerte.xyz' -> mittlerweile: 'JJJJ-MM-DD_xxhxxmxxs_scan25-{t}.xyz',    wobei {t} fuer die Dicke in Millimeter steht
- '3.6mm_gravitation.xyz' 
- '3.6mm_endwerte.xyz'

## Auflager bestimmen
### 5. mittels Kruemmung
wir haben uns in x- und y-Richtung jeweils die Kruemmung der Mittellinie angesehen. Mittels Least-Square-Methode, welche mir einen Radius und Kreismittelpunkt zurueckgab.
-> wenn mittelpunkt groeßer-gleich unseren Werten (+Toleranz), positive Kruemmung, sonst negative Kruemmung

Problem: Glasplatte kann man nicht mit so banalem Modell analysieren, ist oft ganz anders gebogen - zu minimalisitisch/rudimentaer

### 6. mittels Minima-Analyse
bei einfacher Minima-Analyse, hatte ich das Problem, dass die Minima immer nur an einem Punkt bzw. in einem kleinen Umkreis des Punktes gefunden wurden. Dadurch erhielt ich massive Auswirkungen an Stellen, weit weg des Punktes bzw. Umkreises.

### 7. Gebiet geviertelt und Minima-Analyse
hat zwar im Großen und Ganzen funktioniert, war aber keine elegante Loe sung. Jenachdem wie die Platte verzogen ist, ist es eine bessere oder schlechtere Loesung, was nicht optimal ist. Da waere manchmal dritteln schoener oder generell das Gebiet anders aufzuteilen -> zu kompliziert.

Idee bis auf weiteres verworfen.

### 8. generelle Analyse: Auflager an Eckpunkten vs. Auflager in der Mitte
haben bemerkt, dass das ganze schwieriger wird als gedacht, haben bei einer 6000x1000 mm Platte mit 3mm Dicke eine maximale Verwerfung von ueber 1000mm!!!

Deswegen haben wir den Code erstmal mit einer Floatglas-Scheibe getestet - Problem: Werte haben nicht zusammengepasst!!!

### 9. Simply Supported vs. Clamped
die Kreis-Auflager, sind zwar als Simply Supported implementiert, wirken aber wegen der Dirichlet-Kreislinien, wie Clamped-Rbg.

--> muss noch geloest werden

