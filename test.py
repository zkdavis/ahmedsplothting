import matplotlib.pyplot as plt
import numpy as np
from Plotter.Plotter import  dataset,figret
import Plotter.Plotter as PL
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Fixing random state for reproducibility
np.random.seed(19680801)

N_points = 100000
n_bins = 20

# Generate a normal distribution, center at x=0 and y=5
x = np.random.randn(N_points)
y = .4 * x + np.random.randn(100000) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg

#z- This method sometimes has mismatch array sizes
#newy,newx,_= axs[0].hist(x, bins=n_bins)
axs[0].hist(x, bins=n_bins)
axtest = axs[0]
axs[1].hist(y, bins=n_bins)
#z- this works consistently
testpatches = axtest.patches
newx = []
newy = []
for i in testpatches:
    newx.append(i.get_xy()[0])
    newy.append(i.get_height())
#plot to check
ds = dataset()
ds.x = newx
ds.y = newy



pl = PL.Plotter()
pl.Plot([ds],pyplt=plt,xscale="linear",yscale="linear")
plt.show()