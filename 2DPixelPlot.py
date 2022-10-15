# importing modules
import numpy as np
import matplotlib.pyplot as plt

# creating a dataset
data = np.random.random((10, 25, 10))

# data is an 3d array  with
# 10x12x10=1200 elements.
# reshape this 3d array in 2d
# array for plotting
nrows, ncols = 50, 50
data = data.reshape(nrows, ncols)

# creating a plot
pixel_plot = plt.figure()


# customizing plot
plt.title("pixel_plot")
pixel_plot = plt.imshow(
    data, cmap='Blues', interpolation='nearest', origin='lower')

plt.colorbar(pixel_plot)

# save a plot
plt.savefig('pixel_plot.png')

# show plot
plt.show()