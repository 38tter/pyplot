from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import os

def abs_fit(x, p1, p2, p3):
  return p1 + p3*np.abs(x-p2)

def abs_fit2(x, p1, p2):
  return p1 + np.abs(x-p2)

#date = 19012311
date = 19013016
numl = 2130
numr = 2177
datpath = 't0.dat'
datpath2 = 't0_a.dat'
for num in range(numl, numr):
    if(os.path.exists("../eps/{0}/slicet0/dat/slicefitt0-fit{1}.dat".format(date, num)) == False):
        continue
    data_p0, data_p1, data_p2 = np.loadtxt("../eps/{0}/slicet0/dat/slicefitt0-fit{1}.dat".format(date, num), comments="!", unpack=True)
    data_x = np.loadtxt("../eps/{0}/slicet0/dat/slicefitt0-xaxis{1}.dat".format(date, num), comments="!", unpack=True)
    if(len(data_p0)<4):
        continue
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    ax.hold(True)
    ax.plot(data_x, data_p1, "x", color="k", label="x-t")
    ax.set_xlim(-3750, -3550.)
    ax.set_ylim(-3780.,-3650.)
    #ax.legend(loc80upper left"
    x = np.arange(-3750., -3550., 0.01)
    
    para_ini = [ -3650, -3650, 1 ]
    param, cov = curve_fit(abs_fit, data_x, data_p1, para_ini)
    y = param[0] + param[2]*np.abs(x-param[1])

    para_ini2 = [ -3650, -3650 ]
    param2, cov2 = curve_fit(abs_fit2, data_x, data_p1, para_ini2)
    y2 = param2[0] + np.abs(x-param2[1])

    ferr = np.sqrt(np.diag(cov))
    with open(datpath, mode='a') as f:
        f.write('\n{0} {1} {2}'.format(num-2000, param[0], ferr[0]))
    
    ferr2 = np.sqrt(np.diag(cov2))
    with open(datpath2, mode='a') as f:
        f.write('\n{0} {1} {2}'.format(num-2000, param2[0], ferr2[0]))
     
    plt.plot(x, y)
    plt.plot(x, y2)
    plt.errorbar(data_x, data_p1, yerr=data_p2, fmt='ro', ecolor='g')
    hum = num - 2000
    plt.annotate('t\' = p0 + p1*|t-p2|' ,xy=(-3650, -3670))
    plt.xlabel("t_Fw{0},{1}-t_Fp".format(hum-1, hum+1))
    plt.ylabel("t_Fw{0}-t_Fp".format(hum))
    plt.savefig("pdf/abs_fit%s.pdf" % num)
