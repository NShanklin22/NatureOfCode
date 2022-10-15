from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation

noisex = PerlinNoise(octaves = 20, seed =1)
noisey = PerlinNoise(octaves= 20, seed = 50)
xpix,ypix = 20,20
#pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
# plt.imshow(pic,cmap='gray')
#
# plt.show()
fig, ax = plt.subplots()
xvals = []
yvals = []

def animate(i, xvals:list, yvals:list):

    # Add x and y to lists
    xvals.append(i)
    yvals.append(noisey(i/50))
    # Limit x and y lists to 10 items
    xvals = xvals[-250:]
    yvals = yvals[-250:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xvals, yvals)
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.20)
    ax.set_title('Plot of random numbers from https://qrng.anu.edu.au')
    ax.set_xlabel('Date Time (hour:minute:second)')
    ax.set_ylabel('Noise Y')

# Set up plot to call animate() function every 1000 milliseconds
ani = animation.FuncAnimation(fig, animate, fargs=(xvals,yvals), interval=10)

plt.show()