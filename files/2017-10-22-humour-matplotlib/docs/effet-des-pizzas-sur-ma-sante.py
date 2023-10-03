#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
====
XKCD
====

Shows how to create an xkcd-like plot.
"""
import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Monroe
    # http://xkcd.com/418/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks([])
    ax.set_ylim([-30, 10])

    data = np.ones(100)
    data[70:] -= np.arange(30)

    plt.annotate(
        u'LE JOUR OÙ JE ME SUIS RENDU\nCOMPTE QUE JE POUVAIS MANGER\nDES PIZZAS QUAND ÇA ME CHANTAIT',
        xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(2, -17))

    plt.plot(data)

    plt.xlabel('temps')
    plt.ylabel(u'ma santé globale')
    fig.text(
        0.5, 0.05,
        u'D’après “Stove Ownership” de xkcd par Randall Monroe',
        ha='center')
    plt.savefig("effet-des-pizzas-sur-ma-sante.png")

plt.show()
