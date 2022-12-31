from cmath import nan
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys
import math
import imageio
np.set_printoptions(threshold=sys.maxsize)
 
def mandelbrot_eval(c, z):
     return z**2 + c

def mandelbrot_iter(c):
    num_iter = 100
    treshold = 100000
    z = 0 +0j
    for x in range(num_iter):
        z = mandelbrot_eval(c,z)

    #return 0 if np.absolute(z) != nan else np.absolute(z)
    return np.absolute(z)

    return np.absolute(z) < treshold
    

def generate_grid(x_bounds, y_bounds, grid_size):
    number_of_samples = grid_size
    x = np.linspace(x_bounds[0], y_bounds[0], number_of_samples)
    y = np.linspace(x_bounds[1], y_bounds[1], number_of_samples)
    xv, yv = np.meshgrid(x, y)
    return xv + yv*1j


def get_mandel_mask(x, y, grid_size): 
    grid = generate_grid(x, y, grid_size)
    mask = mandelbrot_iter(grid)
    return mask


def create_animation():
    grid_size = 400

    num_frames = 300
    frames = []
    for i in range(1,num_frames):
        print(i)
        x = (-10/i, -4/i + 0.7)
        y = (10/i, 4/i + 0.7)
        mask = np.nan_to_num(get_mandel_mask(x,y,grid_size))
        
        mask = mask.reshape(grid_size, grid_size)
        
        mask = np.clip(mask, 0, 10)
        mask[mask == 10] = 0
        #mask = mask/np.max(mask)
        frames.append([plt.imshow(mask, interpolation="nearest", origin="upper", cmap="inferno",vmin=0, vmax=1)])

    #imageio.mimsave('movie.gif', frames, duration=0.1)
    
    fig = plt.figure()
    #fig.set_size_inches(1, 1, True)
    ani = animation.ArtistAnimation(fig, frames, interval=100, blit=True,
                                repeat_delay=10)
    writergif = animation.PillowWriter(fps=30)
    ani.save('mandelbrot.gif',writer=writergif)
    
    plt.show()

create_animation()


'''
mask = get_mandel_mask()
print(mask)
mask = mask.reshape(grid_size, grid_size)
#mask = np.clip(mask, 0, 100)
print (mask.shape)
plt.colorbar()
plt.show()
'''