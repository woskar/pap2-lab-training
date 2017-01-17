#PAP2 V256: Röntgenfluoreszenz

#Aufgabe 1a: Auswertung k_alpha-Strahlung: 

#Import der Module
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Einlesen der Daten in folgender Reihenfolge:
Z, Ea, sEa, sqEa, dsqEa = np.loadtxt('tab1.txt', skiprows=3, usecols=(1,2,3,4,5), unpack=True)
#Kernladungszahl Z
#Energie der K_alpha-Strahlung Ea
#Peakbreite der Ka Strahlung sEa
#Wurzel aus Ea: sqEa
#Fehler der Wurzel: dsqEa

# Z: [ 22.  26.  28.  29.  30.  40.  42.  47.]
# Ea: [  4.47   6.4    7.49   8.06   8.65  15.81  17.48  21.99]
# sEa: [ 0.29  0.28  0.26  0.26  0.26  0.26  0.25  0.25]
# sqEa: [ 2.11  2.53  2.73  2.83  2.94  3.98  4.18  4.69]
# dsqEa: [ 0.07  0.06  0.05  0.05  0.05  0.03  0.03  0.03]


#Fitfunktion: Moseleyesches Gesetz (wie in Einleitung vereinfacht)
def moseley(z, E, sigma):
    return E*(z - sigma)*np.sqrt(3/4)

#Fit durchführen
popt, pcov = curve_fit(moseley, Z, sqEa, maxfev=5000)
perr = np.sqrt(np.diag(pcov))

#Theoretischer Erwartungswert
Er=13.6*10**-3
x=np.arange(20, 50, 0.1)
y=np.sqrt(3*Er/4)*(x-1)

#Güte des Fits
chisquare=np.sum((((moseley(Z,*popt))-sqEa)/(dsqEa))**2)
dof=6 #degrees of freedom, Freiheitsgrad Anzahl Messwerte (8) - Fitparameter (2)
chisquare_red=chisquare/dof

from scipy.stats import chi2
prob=round(1-chi2.cdf(chisquare,dof),2)*100

#Plotten
plt.errorbar(Z, sqEa, yerr=dsqEa, linestyle='None', marker='x', label='$Messwerte$')
plt.plot(x, moseley(x, *popt), label='$Moseley-Fit$')
plt.plot(x,y, linestyle='--', label='$Moseley\ Erwartung$')
plt.xlabel('$Kernladungszahl\ Z\ des\ Elements$')
plt.ylabel('$Energie\ der\ Linie\ \sqrt{E} \ in\ \sqrt{keV}$')
plt.title('Diagramm 1: $K_{\\alpha}$-Linien-Energie abh. von Kernladungszahl')
plt.legend(loc='best')
plt.axis((20, 50, 2, 5))
plt.rcParams["figure.figsize"][0] = 8
plt.rcParams["figure.figsize"][1] = 5
plt.rcParams["font.family"]='serif'
plt.legend(title='Messwerte mit Fit', borderpad=1, borderaxespad=1, loc='upper left', shadow='true')

#Text im Plot
plt.text(38, 3.3, u'$\\sigma_{\\alpha}=%.3f \pm%.3f$' %(popt[1], perr[1]), fontsize=10)
plt.text(38, 3.1, u'$E_{\\alpha}=%.3f \pm%.3f\ eV$' %((popt[0]**2)*1000, (2*popt[0]*perr[0])*1000), fontsize=10)
plt.text(38, 2.9, u'$\chi^{2}=%.2f$' %(chisquare), fontsize=10)
plt.text(38, 2.7, u'$\chi_{red}^{2}=%.2f $' %(chisquare_red), fontsize=10)
plt.text(38, 2.5, u'$P=%.2f $' %(prob) + '%', fontsize=10)


print('Werte in roher Form:')
print('Beste Werte aus Fit: Wurzel(E) in Wurzel(keV) und sigma')
print(popt)
print('Fehler der Werte aus Fit (Wurzel der Kovarianzmatrixwerte)')
print(perr)
print('Chiquadratsumme:')
print (chisquare)
print("Fitwahrscheinlichkeit="+str(prob)+"%")

plt.savefig('v256_1.pdf',format='pdf')


#Aufgabe 1b: Auswertung k_beta-Strahlung:

#Import der Module
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Einlesen der Daten in folgender Reihenfolge:
Z, Eb, sEb, sqEb, dsqEb = np.loadtxt('tab1.txt', skiprows=5, usecols=(1,6,7,8,9), unpack=True)
#Kernladungszahl Z
#Energie der K_beta-Strahlung Eb
#Peakbreite der Kb Strahlung sEb
#Wurzel aus Eb: sqEb
#Fehler der Wurzel: dsqEb

#Z: [ 28.  29.  30.  40.  42.  47.]
#Eb: [  8.16   8.87   9.55  17.29  19.62  24.73]
#sEb: [ 0.31  0.27  0.31  0.29  0.29  0.29]
#sqEb: [ 2.86  2.98  3.09  4.16  4.43  4.97]
#dsqEb: [ 0.05  0.04  0.05  0.03  0.03  0.03]

#Fitfunktion: Moseleyesches Gesetz (wie in Einleitung vereinfacht)
def moseley2(Z1, E, sigma):
    return E*(Z1 - sigma)*np.sqrt(8/9)

#Fit durchführen
popt, pcov = curve_fit(moseley2, Z, sqEb, maxfev=5000)
perr = np.sqrt(np.diag(pcov))


#Theoretischer Erwartungswert
Er=13.6*10**-3
x=np.arange(20, 50, 0.1)
y=np.sqrt(8*Er/9)*(x-1.8)

#Güte des Fits
chisquare=np.sum(((moseley2(Z,*popt)-sqEb)/(dsqEb))**2)
dof=4 #degrees of freedom, Freiheitsgrad Anzahl Messwerte (6) - Fitparameter (2)
chisquare_red=chisquare/dof

from scipy.stats import chi2
prob=round(1-chi2.cdf(chisquare,dof),2)*100

#Plotten
plt.errorbar(Z, sqEb, yerr=dsqEb, linestyle='None', marker='x', label='$Messwerte$')
plt.plot(x, moseley2(x, *popt), label='$Moseley-Fit$')
plt.plot(x,y, linestyle='--', label='$Moseley\ Erwartung$')
plt.xlabel('$Kernladungszahl\ Z\ des\ Elements$')
plt.ylabel('$Energie\ der\ Linie\ \sqrt{E} \ in\ \sqrt{keV}$')
plt.title('Diagramm 2: $K_{\\beta}$-Linien-Energie abh. von Kernladungszahl')
plt.legend(loc='best')
plt.axis((27, 48, 2.5, 5.3))
plt.rcParams["figure.figsize"][0] = 8
plt.rcParams["figure.figsize"][1] = 5
plt.legend(title='Messwerte mit Fit', borderpad=1, borderaxespad=1, loc='upper left', shadow='true')
plt.text(38, 3.6, u'$\\sigma_{\\beta}=%.3f \pm%.3f$' %(popt[1], perr[1]), fontsize=10)
plt.text(38, 3.4, u'$E_{\\beta}=%.3f \pm%.3f\ eV$' %((popt[0]**2)*1000, (2*popt[0]*perr[0])*1000), fontsize=10)
plt.text(38, 3.2, u'$\chi^{2}=%.2f$' %(chisquare), fontsize=10)
plt.text(38, 3, u'$\chi_{red}^{2}=%.2f $' %(chisquare_red), fontsize=10)
plt.text(38, 2.8, u'$P=%.2f $' %(prob) + '%', fontsize=10)

print('Werte in roher Form:')
print('Beste Werte aus Fit: Wurzel(E) in Wurzel(keV) und sigma')
print(popt)
print('Fehler der Werte aus Fit (Wurzel der Kovarianzmatrixwerte)')
print(perr)
print('Chiquadratsumme:')
print (chisquare)
print("Fitwahrscheinlichkeit="+str(prob)+"%")

plt.savefig('v256_2.pdf',format='pdf')
