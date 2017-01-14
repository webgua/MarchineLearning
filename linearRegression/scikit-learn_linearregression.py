%matplotlib inline
import matplotlib.pyplot as plt 

def runplt():
	plt.figure()
	plt.title(u'diameter-cost curver')
	plt.xlabel(u'diameter')
	plt.ylabel(u'cost')
	plt.axis([0,25,0,25])
	plt.grid(True)
	return plt

plt = runplt()
X = [[6],[8],[10],[14],[18]]
Y = [[7],[9],[13],[17.5],[18]]

plt.plot(X,Y,'k.')
plt.show()