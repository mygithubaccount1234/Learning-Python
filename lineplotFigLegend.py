# lineplotFigLegend.py
import numpy as np
import pylab as pl
# Make x, y arrays for each graph
x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
x2 = [1, 2, 4, 6, 8]
y2 = [2, 4, 8, 12, 16]
8
# use pylab to plot x and y : Give your plots names
plot1 = pl.plot(x1, y1, �r�)
plot2 = pl.plot(x2, y2, �go�)
# give plot a title
pl.title(�Plot of y vs. x�)
# make axis labels
pl.xlabel(�x axis�)
pl.ylabel(�y axis�)
# set axis limits
pl.xlim(0.0, 9.0)
pl.ylim(0.0, 30.)
# make legend
pl.legend([plot1, plot2], (�red line�, �green circles�), �best�, numpoints=1)
# show the plot on the screen
pl.show()
