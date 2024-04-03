import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# This was just how I loaded my position data in from a separate file. Loading in the position data in your
# code shouldn't be difficult, you'll just need to pass the values for each body into the animate_func for
# each frame
#-----------------------------------------------------------------------------------------------------------
x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5 = np.loadtxt('position_data.dat', unpack=True)

set1 = np.array([x1, y1])
set2 = np.array([x2, y2])
set3 = np.array([x3, y3])
set4 = np.array([x4, y4])
set5 = np.array([x5, y5])
numDataPoints = len(x1)
#-----------------------------------------------------------------------------------------------------------

# The num argument is basically just your frame number
# I added a factor called div to skip frames and speed up the animation,
# just keep it at 1 or delete it and all mention of it if you don't want it!
def animate_func(num):
    div = 1
    ax.clear()
    # Using ax.plot gives you a trailing tail for each body, you can use indexing trickery
    # to give that tail a finite length if you want
    ax.plot(set1[0, :div*num+1], set1[1, :div*num+1], c='orange')
    ax.plot(set2[0, :div*num+1], set2[1, :div*num+1], c='blue')
    ax.plot(set3[0, :], set3[1, :], c='white')
    ax.plot(set4[0, :div*num], set4[1, :div*num], c='orange', label='Satellite path')
    ax.plot(set5[0, :], set5[1, :], c='white')

    # The scatter function is how you'll plot the individual bodies, you can use the 's='
    # parameter to change the size of each body.
    ax.scatter(set1[0, div*num], set1[1, div*num], c='orange', marker='o', label='Sun')
    ax.scatter(set2[0, div*num], set2[1, div*num], c='blue', marker='.', label='Earth')
    ax.scatter(set3[0, div*num], set3[1, div*num], c='#a6a6a6', marker='o', label='Jupiter')
    ax.scatter(set4[0, div*num], set4[1, div*num], c='white', marker='.', label='Satellite')
    ax.scatter(set5[0, div*num], set5[1, div*num], c='#474747', marker='o', label='Uranus')
    ax.legend()
    ax.set_xlabel('x (AU)')
    ax.set_ylabel('y (AU)')
    ax.set_title('Uranus flyby with Jupiter Gravitational Assist')

    ax.set_xlim([-10, 10])
    ax.set_ylim([-2, 10])

    ax.set_aspect('equal')
    ax.set_facecolor('black')


# Plotting the Animation
fig = plt.figure()
ax = plt.axes()
line_ani = animation.FuncAnimation(fig, animate_func, interval=20,   
                                   frames=numDataPoints//1)
plt.show()
# FFwriter = animation.FFMpegWriter(fps=60)
# line_ani.save('UranusFlyby.mp4', writer = FFwriter, dpi=300)