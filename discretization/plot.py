import numpy
from matplotlib import pyplot
import time, sys

eta = numpy.zeros(101)
f = numpy.zeros(101)

filename = ('x_03_linear.csv', 'x_03_upwind.csv', 'x_03_linearUpwind.csv', 'x_03_QUICK.csv')
label_name = ['linear','upwind','linearUpwind', 'QUICK']
X = [0.03, 0.035, 0.040, 0.045]
markers = ['s', '>', 'v', '*']
U_inf = 0.2
vis = 1e-6


fig = pyplot.figure(figsize=(11,7), dpi=100)

i = 0
for fname in filename:
	y,x = numpy.loadtxt(fname, delimiter=';', unpack=True)
	eta[:] = x[:] * numpy.sqrt( U_inf/(2.*vis*X[0]) )
	f[:] = y[:] / U_inf
	pyplot.plot(eta, f, markers[i], label=label_name[i])
	i += 1

x,y = numpy.loadtxt('BlasiusF.dat', delimiter=',', unpack=True)
pyplot.plot(x, y, lw=2, label="Blasius' solution")


pyplot.xlabel('$\eta$')
pyplot.ylabel('$ f \prime (\eta) $');

pyplot.legend(loc=4)
pyplot.ylim(0, 1.2)
pyplot.show()
