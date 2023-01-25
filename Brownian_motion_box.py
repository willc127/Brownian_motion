import turtle as t
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random
import csv


def brownian_box(scale, total_steps, dist_type, boxsize):
    # Specify screen properties
    scr = t.Screen()
    scr.bgcolor('black')

    # Draw box
    box = t.Turtle()
    box.penup()
    box.setposition(-boxsize, -boxsize)
    box.pendown()
    box.pensize(5)
    box.pencolor('white')
    box.color('white')
    for i in range(4):
        box.forward(2*boxsize)
        box.left(90)
    box.hideturtle()

    # Create a particle
    particle = t.Turtle()
    particle.shape('circle')
    particle.shapesize(stretch_wid=0.75, stretch_len=0.75)
    particle.width(2)

    # Specify speed of drawing; 0 = fastest
    particle.speed(0)

    # Get a color from a colormap for each step
    row = np.linspace(0.0, 1.0, total_steps)
    rgb = mpl.colormaps['jet'](row)[np.newaxis, :, :3]  # Convert color to rgb

    # Define positions of the particle
    x = np.zeros(total_steps)
    y = np.zeros(total_steps)

    # Draw the random walk of a particle
    for i in range(0, total_steps):
        print(i)
        (x[i], y[i]) = particle.pos()  # get position in each step
        # Get a color for the particle
        particle.pencolor(rgb[0][i])
        particle.color(rgb[0][i])

        if x[i] >= boxsize:
            particle.setposition(boxsize, y[i])
            particle.right(180)
        elif x[i] <= -boxsize:
            particle.setposition(-boxsize, y[i])
            particle.right(180)
        elif y[i] >= boxsize:
            particle.setposition(x[i], boxsize)
            particle.right(180)
        elif y[i] <= -boxsize:
            particle.setposition(x[i], -boxsize)
            particle.right(180)

        if dist_type == 'normal':
            # Move forward with a gaussian distribution
            particle.forward(random.gauss(0, 1)*scale)
            # Turn with a gaussian distribution
            particle.right(random.gauss(0, 1)*360)
        elif dist_type == 'random':
            # Move forward with a random distribution
            particle.forward(random.random()*scale)
            # Turn with a random distribution
            particle.right(random.random()*360)

    return [x, y]


# Calling function
total_steps = 6000
scale = 5
dist_type = 'normal'
boxsize = 100
# Set random seed for reproducibility
random.seed(3)
(X, Y) = brownian_box(scale, total_steps, dist_type, boxsize)

# Define the variable r (total distance of particle)
r = np.zeros(total_steps)
# Define the variable time (time of particle)
time = np.arange(total_steps)

# Open file to write the results
with open('results_box.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'X', 'Y', 'r'])
    for i in range(total_steps):
        # Calculate the total distance of particle
        r[i] = (X[i]**2 + Y[i]**2)**0.5
        writer.writerow([time[i], X[i], Y[i], r[i]])

t.done()
