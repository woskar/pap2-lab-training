import matplotlib.pyplot as plt
import numpy as np


f, U_A1, U_A2, U_A3, U_A4, U_A5 = np.loadtxt('tab3.txt', skiprows=1, usecols=(0,1,2,3,4,5), unpack=True)


plt.loglog(f, U_A1, linestyle='None', marker='.', label='$R_{G}=680 k\Omega, U_{G}=0.3 V_{SS}$')
plt.loglog(f, U_A2, linestyle='None', marker='x', label='$R_{G}=274 k\Omega, U_{G}=0.3 V_{SS}$ ')
plt.loglog(f, U_A3, linestyle='None', marker='o', label='$R_{G}=48.7 k\Omega, U_{G}=1.0 V_{SS}$')
plt.loglog(f, U_A4, linestyle='None', marker='s', label='$R_{G}=48.7, U_{G}=1.0, C=540 pF$')
plt.loglog(f, U_A5, linestyle='None', marker='+', label='$R_{G}=48.7, U_{G}=1.0, C=47 nF$')
plt.xlabel('Frequenz $f$')
plt.ylabel('Ausgangsspannung $U_{aus}$')
plt.title('Frequenzgang: $V\'=f(v)$ (Tabelle3)')
plt.legend(title='Widerstand und Eingangsspannung:', loc='best', shadow='true')
