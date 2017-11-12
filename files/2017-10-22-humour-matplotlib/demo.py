# -*- coding: utf-8 -*-

"""

Dans Spyder

- Appuyer sur F5 pour exécuter tout le script

Les lignes de commande ci-dessous sont forts utiles de temps à autres.
Pour les exécuter individuellement, mettre le curseur sur la ligne et
appuyer sur F9

# Affiche les graphiques dans la console
%matplotlib inline

# Affiche les graphiques dans une fenêtre séparée
%matplotlib auto

# Ferme toutes les fenêtres de graphiques
plt.close("all")

# Supprime toutes les variables
%reset -f

# Efface la console
clear

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# %%
if __name__ == "__main__":

    # NumPy
    x = np.linspace(-5 * np.pi, 5 * np.pi, 501)
    y = 1.55 * np.sin(x)/x

    # Matplotlib
    plt.close("all")
    plt.figure(figsize=(15, 5))
    plt.plot(x, y, label="Ça bouge, dis-donc !")
    plt.legend()
    plt.title("OUAH !")
    plt.xlabel("temps")
    plt.ylabel("intensité")
    plt.grid(True)
    plt.show()

    # Pandas
    df = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',
                     sep='\t')

    # Matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(df.selectable, label="Ça bouge, encore !")
    plt.legend()
    plt.title("OUAH !")
    plt.xlabel("x")
    plt.ylabel("selectable")
    plt.grid(False)
    x_ticks_locs = np.linspace(0, 400, 21)
    x_ticks_labels = ["" for tick in x_ticks_locs]
    x_ticks_labels[0::2] = [("%d" % (tick)) for tick in x_ticks_locs[0::2]]
    plt.xticks(x_ticks_locs, x_ticks_labels)
    plt.show()
