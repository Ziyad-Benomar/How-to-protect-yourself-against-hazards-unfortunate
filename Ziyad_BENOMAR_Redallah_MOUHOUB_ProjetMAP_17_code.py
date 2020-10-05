"""
Comment se prémunir contre les aléas malheureux?
Sujet proposé par Thibaut MASTROLIA

Par: Ziyad BENOMAR et Redallah MOUHOUB

"""
## Questions de simulations

import math
import numpy as np
import  matplotlib.pyplot as plt

## S1.

lmbda=5
t=1

n=np.random.poisson(lmbda*t)  # n suit une loi de Poisson de paramètre lmbda*t
U=[0]+[ np.random.uniform(0,t) for i in range(n)]+[t] # Les valeurs 0 et t ajoutées au début et en fin de la liste 
U.sort()                                              # vont servir pour la représentation graphique
Y=[0]+[i for i in range(n+1)]

plt.step(U,Y)
plt.axis([0,t,0,n+1])
plt.xticks(U,[0]+["$t_{"+str(i)+"}$" for i in range(1,n+1)])
plt.show()


## S2.

"""" Les J_i, suivant une loi normale centrée, ne sont pas conformes avec l'interprétation que nous avons donnée à la question T7; les sauts aléatoires devraient être positifs."""

lmbda=5
t=1
mu=0
sigma=math.sqrt(5)

n=np.random.poisson(lmbda*t)
U=[0]+[ np.random.uniform(0,t) for i in range(n)]+[t]
U.sort()
Y=[0]+[0 for i in range(n+1)]
for i in range(1,n+1):
    Y[i+1]=Y[i]+(np.random.normal(mu,sigma**2))  #on pourrait ajouter 'abs' si on veut avoir des sauts positifs

plt.step(U,Y)
plt.axis([0,t,min(Y)-1,max(Y)+1])
plt.xticks(U,[0]+["$t_{"+str(i)+"}$" for i in range(1,n+1)])
plt.show()

## S3.

lamda = 5
mu = 1
sigma = 1
u = 20
c = 7
lim_compteur=15 # cf. la remarque ci-dessous.
temps_ruine=-1 # -1 si la ruine n'a pas eu lieu, et strictement positive sinon.

"""Avec les valeurs mu =1, lambda=5 et c=7, on a c-lambda*mu = 2 > 0, donc R_t tend vers +\infty p.s., et par suite, on n'est pas sûrs qu'une ruine totale aura lieu.
On ne peut donc pas prendre R_t<0 comme condition d'arrêt de notre programme, car rien ne garantit sa réalisation. D'où l'utilisation d'un compteur, ."""


t_1 = np.random.exponential(lamda)
temps = [0, t_1]
R = [u, u + c*t_1]
compteur = 0

while temps_ruine==-1 and compteur <lim_compteur:
    compteur+=1
    t = temps[-1] + np.random.exponential(lamda)
    temps.append(temps[-1])
    temps.append(t)
    n=np.random.poisson(lamda*(temps[-1]-temps[-2])) # Cette construction est justifiée par les propriétés de stationnarité
    C_t=0                                            # et d'indépendance admises dans la première partie du problème
    for i in range(n):
        C_t += np.random.normal(mu, sigma**2)
    R.append(R[-1] - C_t)       # chaque élement répété 2 fois de de suite pour un souci de représentation graphique
    if R[-1]<0 : temps_ruine=temps[-2]
    delta = c*(temps[-1] - temps[-2])
    R.append(R[-1] + delta)

print(temps_ruine)
if temps_ruine!=-1 :
    plt.axhline(0,color='red', linestyle='--')
    plt.axvline(temps_ruine,color='red', linestyle='--')
plt.plot(temps, R)
plt.show()