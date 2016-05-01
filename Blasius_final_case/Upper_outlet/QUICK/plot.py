import numpy
from matplotlib import pyplot
import time, sys

eta = numpy.zeros(101)
f = numpy.zeros(101)

filename = ['x_01.csv','x_02.csv','x_03.csv','x_04.csv']
label_name = ['x = 0.03 m','x = 0.035 m','x = 0.04 m','x = 0.045 m']
X = [0.01, 0.02, 0.03, 0.04]
markers = ['>', 'v', '*', 's']
U_inf = 0.2
vis = 1e-6


fig = pyplot.figure(figsize=(11,7), dpi=100)

i = 0
for fname in filename:
	y,x = numpy.loadtxt(fname, delimiter=';', unpack=True)
	eta[:] = x[:] * numpy.sqrt( U_inf/(2.*vis*X[i]) )
	f[:] = y[:] / U_inf
	pyplot.plot(eta, f, markers[i], label=label_name[i])
	i += 1
x,y = numpy.loadtxt('BlasiusF.dat', delimiter=',', unpack=True)
pyplot.plot(x, y, lw=3, label="Blasius' solution")


pyplot.xlabel('$\eta$')
pyplot.ylabel('$ f \prime (\eta) $');

pyplot.legend(loc=4)
pyplot.ylim(0, 1.2)
pyplot.show()
