#PAP2 Versuch 245: Induktion
#Oskar Weinfurtner, Dezember 2016

#Aufgabe 1a: Induktionsgesetz U(f)

#Import von allen benötigten Modulen
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Manuelles Setzen der Größe des Plots
plt.rcParams["figure.figsize"][0] = 9
plt.rcParams["figure.figsize"][1] = 6

#Einlesen der Daten aus Tabelle 1
f, f_err, U1, U1_err = np.loadtxt('tab1.txt', skiprows=1, usecols=(0,1,2,3), unpack=True)

# Definition der Ausgleichsgerade y=f(x)
def linear(x, m, t):
    return m*x + t

#Bester Fit an die Geraden
popt, pcov = curve_fit(linear, f, U1)

#Abweichung ist Wurzel aus Diagonalelementen der Kovarianzmatrix
perr = np.sqrt(np.diag(pcov))

#Zeichnen der Messwerte mit Fehler und Plot
plt.errorbar(f, U1, linestyle='None', marker='x', label='Messwerte mit Fehler', xerr=f_err, yerr=U1_err)
x = np.linspace(0,16,10)
plt.plot(x, linear(x, *popt), linestyle='--', label='$Steigung: \; m_{fit}=%.2f \pm%.2f $' %(popt[0], perr[0]))

#Eigenschaften des Plots: Achsen, Beschriftungen, Gitternetz
plt.rcParams["font.family"]='serif'
plt.axis([0,16,-1,13])
plt.xlabel('Frequenz $f [Hz]$')
plt.ylabel('Gemessene Induktionsspannung $U_{Induktion} [V]$')
plt.title('Diagramm 1a: Induktionsspannung abh. von Frequenz $U_{Induktion}(f)$ (Tabelle1)')
plt.legend(title='Messwerte und Linearer Fit', loc='best', borderpad=1, borderaxespad=1, shadow='true', fontsize='medium')
plt.grid(True)


#Speichern des Plots
#plt.savefig('v245_1a.pdf', format='pdf')



#Aufgabe 1b: Induktionsgesetz U(I)

#Import von allen benötigten Modulen
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Manuelles Setzen der Größe des Plots
plt.rcParams["figure.figsize"][0] = 9
plt.rcParams["figure.figsize"][1] = 6

#Einlesen der Daten aus Tabelle 2
I, I_err, U2, U2_err = np.loadtxt('tab2.txt', skiprows=1, usecols=(0,1,2,3), unpack=True)

# Definition der Ausgleichsgerade y=f(x)
def linear(x, m, t):
    return m*x + t

#Bester Fit an die Geraden
popt, pcov = curve_fit(linear, I, U2)

#Abweichung ist Wurzel aus Diagonalelementen der Kovarianzmatrix
perr = np.sqrt(np.diag(pcov))

#Zeichnen der Messwerte mit Fehler und Plot
plt.errorbar(I, U2, linestyle='None', marker='x', label='Messwerte mit Fehler', xerr=I_err, yerr=U2_err)
x = np.linspace(0,16,10)
plt.plot(x, linear(x, *popt), linestyle='--', label='$Steigung: m_{fit}=%.2f \pm%.2f$' %(popt[0], perr[0]))

#Eigenschaften des Plots: Achsen, Beschriftungen, Gitternetz
plt.rcParams["font.family"]='serif'
plt.axis([0,5,0,9])
plt.xlabel('Spulenstrom $I_{Spule} [A]$')
plt.ylabel('Gemessene Induktionsspannung $U_{Induktion} [V]$')
plt.title('Diagramm 1b: Induktionsspannung abh. vom Spulenstrom $U_{Induktion}(I_{Spule})$ (Tabelle2)')
plt.legend(title='Messwerte und Linearer Fit', loc='best', borderpad=1, borderaxespad=1, shadow='true', fontsize='medium')
plt.grid(True)


#Speichern des Plots
plt.savefig('v245_1b.pdf', format='pdf')


#Aufgabe 2: Induktionsspannung U(I)

#Import von allen benötigten Modulen
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Manuelles Setzen der Größe des Plots
plt.rcParams["figure.figsize"][0] = 9
plt.rcParams["figure.figsize"][1] = 6

#Einlesen der Daten aus Tabelle 2
a, a_err, U, U_err = np.loadtxt('tab3.txt', skiprows=1, usecols=(0,1,2,3), unpack=True)

#Zeichnen der Messwerte mit Fehler und Plot
plt.errorbar(a, U, linestyle='-', marker='x', label='Messwerte mit Fehler', xerr=a_err, yerr=U_err)

#Eigenschaften des Plots: Achsen, Beschriftungen, Gitternetz
plt.rcParams["font.family"]='serif'
plt.axis([0,360,0,4])
plt.xlabel(r'$ Winkel \;\; \alpha_{Spule} [\degree]$')
plt.ylabel(r'Gemessene Induktionsspannung $U_{Induktion} [V]$')
plt.title(r'Diagramm 2a: Induktionsspannung abh. vom Winkel $U_{Induktion}(\alpha_{Spule})$ (Tabelle3)')
#plt.legend(title='Messwerte und Lineare Fitfunktion', loc='best', borderpad=1, borderaxespad=1, shadow='true')
plt.grid(True)

#Speichern des Plots
#plt.savefig('v245_2a.pdf', format='pdf')


#Polardarstellung der Auslenkung
a, a_err, U, U_err = np.loadtxt('tab3.txt', skiprows=1, usecols=(0,1,2,3), unpack=True)
theta = (360-a)*(np.pi/180) #Wir haben Spule rechtsrum gedreht
ax = plt.subplot(111, projection='polar')
ax.plot(theta, U, color='r', marker='.')
ax.grid(True)

ax.set_title(r"Diagramm 2b: Polardarstellung von $U_{Induktion}(\alpha_{Spule})$", va='bottom')
plt.savefig('v245_2b.pdf', format='pdf')


#Verhältnis von induzierter und angelegter Spannung als Funktion der Frequenz

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams["figure.figsize"][0] = 8
plt.rcParams["figure.figsize"][1] = 5

f, f_err, Uind, Uind_err, Ih, Ih_err, Uh, Uh_err=np.loadtxt('tab4.txt', skiprows=1, usecols=(0,1,2,3,4,5,6,7), unpack=True)

plt.errorbar(f, Uind/Uh, yerr=Uind/Uh*np.sqrt((Uind_err/Uind)**2+(Uh_err/Uh)**2), fmt='x', label='$Messwerte$' )
plt.xlabel('$Freqenz\ f\ \mathrm{[Hz]}$')
plt.ylabel('$ Spannungsverhaeltnis\ \\frac{U_{induziert}}{U_{angelegt}}$')
plt.title('Diagramm 3:  Spannungsverhaeltnis (ind/ang) abh. von Frequenz $f$')
plt.legend(loc='best', borderpad=1, borderaxespad=1, shadow='true')
plt.grid(True)
plt.savefig('v245_3.pdf')

#Widerstand (U/I) der Spule gegen die Frequenz


%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams["figure.figsize"][0] = 8
plt.rcParams["figure.figsize"][1] = 5

f, df, Uind, dUind, Ih, dIh, Uh, dUh=np.loadtxt('tab4.txt', skiprows=1, usecols=(0,1,2,3,4,5,6,7), unpack=True)

# Ausgleichsgerade definieren
def linear(x, m, t):
    return m*x + t

# Fit an die Kurve
popt, pcov = curve_fit(linear, f, Uh/Ih)

# Abweichung berechnen aus Kovarianzmatrix
perr = np.sqrt(np.diag(pcov))

#Plotten der Werte und Ausgleichsgerade
plt.errorbar(f, Uh/Ih, yerr=Uh/Ih*np.sqrt((dIh/Ih)**2+(dUh/Uh)**2), fmt='x', label='$Widerstand \ R=U_{Helmholtz}/I_{Helmholtz} $')
plt.plot(f, linear(f, *popt), linestyle='--', label='$ Steigung: \; m_{fit}=%.2e \pm%.2e$' %(popt[0], perr[0]), )
plt.xlabel('$Freqenz\ f\ \mathrm{[Hz]}$')
plt.ylabel('Widerstand $R=\\frac{U_{Helmholtz}}{I_{Helmholtz}} \ [\Omega] $')
plt.title('Diagramm 4: Widerstand (U/I) abh. von Frequenz $f$')
plt.legend(title='Messwerte und Linearer Fit', loc='best', borderpad=1, borderaxespad=1, shadow='true')
plt.grid(True)

#Speichern des Plots
plt.savefig('v245_4.pdf')
