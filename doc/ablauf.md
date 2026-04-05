# Ablauf der Entwicklung

## Gravitations-Code
1. 1D-Modell
Ich habe begonnen die Verwerfung unserer Glasplatte als 1D Problem zu betrachten und gelöst, um ein bisschen in die Thematik der Mechanik und Physik zu kommen.
Wichtige Erkenntnisse waren fuer mich, die Wichtigkeit zu wissen, ob Kräfte punktuell oder in unserem Fall flächendeckend, in unserem Fall gleichmäßig auftreten.

2. Kirchhoff-Love
Den 2D Code habe ich in VS-Code mit python insbesondere NGSolve geschrieben. Ich habe eine super Dokumentation der KL-Gleichung auf NGSolve-docs gefunden, die ich relativ ähnlich nachgearbeitet habe.
Danach habe ich viel visualisiert

3. Testwerte/Zusammenrechnen
Ich habe mir Startwerte (SW) generiert, die Auflager definiert und mit den aus dem Gravitations-Code (KL-Code) erhaltenen Daten (GravW) zusammengerechnet -> Endwerte (EW) erhalten

SW, GravW und EW visualisiert

4. Messwerte
von Papa echte Messwerte (MW) einer Platte erhalten und getestet

Achtung: von nun an ist im Dateinamen der Daten immer die Dicke der getesteten Platte inkludiert
zB. 
- '3.6mm_messwerte.xyz'
- '3.6mm_gravitation.xyz' 
- '3.6mm_endwerte.xyz'

## Auflager bestimmen
5. mittels Krümmung
wir haben uns in x- und y-Richtung jeweils die Krümmung der Mittellinie angesehen. Mittels Least-Square-Methode, welche mir einen Radius und Kreismittelpunkt zurückgab.
-> wenn mittelpunkt größer-gleich unseren Werten (+Toleranz), positive Krümmung, sonst negative Krümmung

Problem: Glasplatte kann man nicht mit so banalem Modell analysieren, ist oft ganz anders gebogen - zu minimalisitisch/rudimentär

6. mittels Minima-Analyse
bei einfacher Minima-Analyse, hatte ich das Problem, dass die Minima immer nur an einem Punkt bzw. in einem kleinen Umkreis des Punktes gefunden wurden. Dadurch erhielt ich massive Auswirkungen an Stellen, weit weg des Punktes bzw. Umkreises.

6.1 Gebiet geviertelt und Minima-Analyse
hat zwar im Großen und Ganzen funktioniert, war aber keine elegante Lösung. Jenachdem wie die Platte verzogen ist, ist es eine bessere oder schlechtere Loesung, was nicht optimal ist. Da waere manchmal dritteln schoener oder generell das Gebiet anders aufzuteilen -> zu kompliziert.

Idee bis auf weiteres verworfen.

