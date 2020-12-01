## Projet python
import numpy as np
import math
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import scipy as sp


#fonctions types
def maximum(l):
    maxi = l[0]
    for i in l:
        if i >= maxi:
            maxi = i
    return maxi

def minimum(l):
    min = l[0]
    for i in l:
        if i <= min:
            min = i
    return min

def moy(l):
    a=0
    for i in l:
        a=a+i
    return a/len(l)

def med(l):
    if len(l) % 2 == 0 :
        return (l[int(len(l)/2)]+l[int(len(l)/2 +1)])/2
    else:
        return l[int((len(l))//2 +1)]


def variance(l):
    va=0
    for i in l:
        va=va +(i-moy(l))**2
    return va/len(l)

def ecart_t(l):
    return variance(l)**0.5

#ouvre et lis le fichier csv
df = pd.read_csv(r"C:\Users\arthur\Desktop\EIVP\info",header=0,sep=";")
df.columns=df.columns.str.strip()
df['sent_at']=pd.to_datetime(df['sent_at'], format="%Y-%m-%d %H:%M:%S +0200")
df.head()

#renvoie l'ensemble des lignes du tableau trier par date croissante
df1 = df.sort_values(by="sent_at",ascending=True)
df1.head(-1)
#filtrage par intervalle de temps sur le tableau trié chrononlogiquement
h_debut='2020-08-25 00:00:52'
h_fin='2020-09-22 23:51:54'
df3=df1[(df1['sent_at']>=h_debut) & (df['sent_at']<=h_fin)]


#renvoie un graphique du bruit par capteur en fonction du temps
for Id in range(1,7):
    df2 = df3[df3['id']==Id]
    df2.head(-1)
    x = df2['sent_at']
    for i in ['noise']:
        y=df2[i]
        plt.plot(x, y, label='Capteur'+str(Id))
plt.legend()
plt.title('Bruit en fonction du temps')
plt.show()

#renvoie un graphique de la température par capteur en fonction du temps
for Id in range(1,7):
    df2 = df3[df3['id']==Id]
    df2.head(-1)
    x = df2['sent_at']
    for i in ['temp']:
        y=df2[i]
        plt.plot(x, y, label='Capteur'+str(Id))
plt.legend()
plt.title('Température en fonction du temps')
plt.show()

#renvoie un graphique de l'humidité par capteur en fonction du temps
for Id in range(1,7):
    df2 = df3[df3['id']==Id]
    df2.head(-1)
    x = df2['sent_at']
    for i in ['humidity']:
        y=df2[i]
        plt.plot(x, y, label='Capteur'+str(Id))
plt.legend()
plt.title('Humidité en fonction du temps')
plt.show()

#renvoie un graphique de la luminosité par capteur en fonction du temps
for Id in range(1,7):
    df2 = df3[df3['id']==Id]
    df2.head(-1)
    x = df2['sent_at']
    for i in ['lum']:
        y=df2[i]
        plt.plot(x, y, label='Capteur'+str(Id))
plt.legend()
plt.title('Luminosité en fonction du temps')
plt.show()

#renvoie un graphique du c02 par capteur en fonction du temps
for Id in range(1,7):
    df2 = df3[df3['id']==Id]
    df2.head(-1)
    x = df2['sent_at']
    for i in ['humidity']:
        y=df2[i]
        plt.plot(x, y, label='Capteur'+str(Id))
plt.legend()
plt.title('Co2 en fonction du temps')
plt.show()


#séparation du tableau par capteurs

capteur1 = df1[ df1['id'] == 1 ]
capteur2 = df1[ df1['id'] == 2 ]
capteur3 = df1[ df1['id'] == 3 ]
capteur4 = df1[ df1['id'] == 4 ]
capteur5 = df1[ df1['id'] == 5 ]
capteur6 = df1[ df1['id'] == 6 ]

#maximum sur les caractéristiques perçu par les capteurs
for Id in range (1,7):
    capteur = df1[ df1['id'] == Id ]
    print("\nLes valeurs maximales de ce capteur sont:\n",capteur.max())

#minimum sur les caractéristiques perçu par les capteurs
for Id in range (1,7):
    capteur = df1[ df1['id'] == Id ]
    print("\nLes valeurs minimales de ce capteur sont :\n",capteur.min())

#variance sur les caractéristiques perçu par les capteurs
for Id in range (1,7):
    capteur = df1[ df1['id'] == Id ]
    print("\nLa variance de ce capteur est :\n",capteur.var())

#moyenne sur les caractéristiques perçu par les capteurs
for Id in range (1,7):
    capteur = df1[ df1['id'] == Id ]
    print("\nLa moyenne de ce capteur est :\n",capteur.mean())

#médiane sur les caractéristiques perçu par les capteurs
for Id in range (1,7):
    capteur = df1[ df1['id'] == Id ]
    print("\nLa mediane de ce capteur est :\n",capteur.median())

#écart type sur les caractéristiques perçu par les capteurs
for Id in range (1,7):
    capteur = df1[ df1['id'] == Id ]
    print("\nL'écart type' de ce capteur est :\n",capteur.std())

#calcul indice humidex
    H=[]
    for i in range (0,len(df3['temp'])):
        H.append(df3['temp'].iloc[i]+0.5555*(6.112*np.exp(5417.7530*(1/273.16-1/(273.16+df3['humidity'].iloc[i])))-10))
    print (H)

#lecture dans le tableau avec 1 colonne en plus concernant l'indice humidex
df4 = df3.assign(indice_humidex = H )

#renvoie un graphique de l'indice humidex par capteur en fonction du temps
for Id in range(1,7):
    df2 = df4[df4['id']==Id]
    df2.head(-1)
    x = df2['sent_at']
    for i in ['indice_humidex']:
        y=df2[i]
        plt.plot(x, y, label='Capteur'+str(Id))
plt.legend()
plt.title('Indice humidex en fonction du temps')
plt.show()


#indice de correlation entre 2 variables
""""ρx,y=0  ⇒
Il n’y a PAS du tout de corrélation entre X et Y

ρx,y=1 ⇒
Il y a corrélation totale positive entre X et Y (X et Y sont liées et évoluent dans le même sens)

ρx,y=–1 ⇒
Il y a corrélation totale négative entre X et Y (X et Y sont
liées mais évoluent en sens opposés)
"""
from scipy.stats import pearsonr
x=df1['temp']
y=df1['humidity']
coeff_pearson,_ = pearsonr(x,y)
print("coefficient de Pearson = {}".format(coeff_pearson))


