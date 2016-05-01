import numpy
from matplotlib import pyplot
import time, sys

eta = numpy.zeros(101)
f = numpy.zeros(101)

label_name = ['x = 0.03 m','x = 0.035 m','x = 0.04 m','x = 0.045 m']
X = [0.03, 0.035, 0.040, 0.045]
markers = ['>', 'v', '*', 's']
U_inf = 0.2
vis = 1e-6


fig = pyplot.figure(figsize=(11,7), dpi=100)


y,x = numpy.loadtxt('x_03_inflow_5.csv', delimiter=';', unpack=True)
eta[:] = x[:] * numpy.sqrt( U_inf/(2.*vis*X[0]) )
f[:] = y[:] / U_inf
pyplot.plot(eta, f, markers[0], label=label_name[0])

x,y = numpy.loadtxt('BlasiusF.dat', delimiter=',', unpack=True)
pyplot.plot(x, y, lw=.5, label="Blasius' solution")


pyplot.xlabel('$\eta$')
pyplot.ylabel('$ f \prime (\eta) $');

pyplot.legend(loc=4)
pyplot.ylim(0, 1.2)
pyplot.show()
