from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import os

def fitfunc(x, p1, p2, p3):
    return p1 + p2*x + p3*x*x

data_wire, data_t0, data_t0err= np.loadtxt("t0.dat", comments="!", unpack=True)
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.hold(True)
ax.plot(data_wire, data_t0, "x", color="k", label="x-t")
ax.set_xlim(50, 95)
ax.set_ylim(-3770.,-3740.)

plt.errorbar(data_wire, data_t0, yerr=data_t0err, fmt='bo', ecolor='r')
#plt.errorbar(data_x, data_p1, yerr=data_p2, fmt='ro', ecolor='g')
x = np.arange(50, 90, 0.01)
para_ini = [ -3800, 0, 1 ]
param, cov = curve_fit(fitfunc, data_wire, data_t0, para_ini)
y = param[0] + param[1]*x + param[2]*x*x

data_wire2, data_t02, data_t0err2= np.loadtxt("t0_a.dat", comments="!", unpack=True)
ax.plot(data_wire2, data_t02, "x", color="r")
plt.errorbar(data_wire2, data_t02, yerr=data_t0err2, fmt='go', ecolor='r')
plt.plot(x, y)

plt.xlabel("Fw")
plt.ylabel("p0")
plt.savefig("pdf/num_vs_t0.pdf")
