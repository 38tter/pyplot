from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def abs_fit(x, p1, p2, p3):
  return p1 + p3*np.abs(x-p2)

data_t0, data_x0 = np.loadtxt("test.dat", comments="!", unpack=True)
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.hold(True)
ax.plot(data_t0, data_x0, "x", color="k", label="x-t")
ax.set_xlim(0., 200.)
ax.set_ylim(0., 10.)
ax.legend(loc="upper left")
x = np.arange(0, 200, 0.01)

param, cov = curve_fit(abs_fit, data_t0, data_x0)
y = param[0] + param[2]*np.abs(x-param[1])

plt.plot(x, y)
plt.savefig("abs_fit.pdf")
