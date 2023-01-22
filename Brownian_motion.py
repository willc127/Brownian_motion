import turtle as t
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random
import csv

# create a brownian motion function


def brownian(scale, steps, dist):
    # Specify screen properties
    scr = t.Screen()
    scr.setup(width=1.0, height=1.0)
    (width, height) = scr.screensize()

    # Specify background color
    t.bgcolor('black')

    # Specify turtle properties
    t.shape('circle')
    t.shapesize(stretch_wid=0.75, stretch_len=0.75)
    t.width(2)

    # Specify speed of drawing; 0 = fastest
    t.speed(0)

    # Get a color from a colormap for each step
    row = np.linspace(0.0, 1.0, steps)
    rgb = mpl.colormaps['jet'](row)[np.newaxis, :, :3]  # Convert color to rgb

    x = np.zeros(steps)
    y = np.zeros(steps)

    # Draw the random walk of a particle
    for i in range(0, steps):
        print(i)
        # Get a color for the particle
        t.pencolor(rgb[0][i])
        t.color(rgb[0][i])
        if dist == 'normal':
            (x[i], y[i]) = t.pos()  # get position in each step
            t.forward(random.gauss(0, 1)*scale) # Move forward with a gaussian distribution
            t.right(random.gauss(0, 1)*360) # Turn with a gaussian distribution
            # If particle is out of screen, turn back
            if abs(x[i]) > width or abs(y[i]) > height:
                t.right(180)
        elif dist == 'random':
            (x[i], y[i]) = t.pos()  # get position in each step
            t.forward(random.random()*scale) # Move forward with a random distribution
            t.right(random.random()*360)  # Turn with a random distribution
            # If particle is out of screen, turn back
            if abs(x[i]) > width or abs(y[i]) > height:
                t.right(180)
    return [x, y]
    t.done()


# Call function
steps = 10000
scale = 10
dist_type = 'normal'
# Set random seed for reproducibility
random.seed(9)

#Get positions of brownian motion
(X, Y) = brownian(scale, steps, dist_type)

#Define the variable r (total distance of particle)
r = np.zeros(steps)
#Define the variable time (time of particle)
time = np.arange(steps)

#Open file to write the results
with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'X', 'Y', 'r'])
    for i in range(steps):
        r[i] = (X[i]**2 + Y[i]**2)**0.5 #Calculate the total distance of particle
        writer.writerow([time[i],X[i], Y[i], r[i]])

