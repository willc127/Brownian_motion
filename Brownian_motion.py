import turtle as t
import matplotlib as mpl
import numpy as np
import random

# create a brownian motion function
def brownian(scale, steps, dist):
    #Specify screen properties
    scr = t.Screen()
    scr.setup(width=1.0, height=1.0)
    (width, height) = scr.screensize()

    # Specify background color
    t.bgcolor('black')
    
    #Specify turtle properties
    t.shape('circle')
    t.shapesize(stretch_wid=0.75, stretch_len=0.75)
    t.width(2)

    # Specify speed of drawing; 0 = fastest
    t.speed(0)

    #Get a color from a colormap for each step
    row = np.linspace(0.0, 1.0, steps)
    rgb = mpl.colormaps['jet'](row)[np.newaxis, :, :3] #Convert color to rgb

    #Draw the random walk of a particle
    for i in range(0,steps):
        #Get a color for the particle
        t.pencolor(rgb[0][i])
        t.color(rgb[0][i]) 
        if dist =='normal':
            t.forward(random.gauss()*scale) #Move forward with a gaussian distribution
            t.right(random.gauss()*360) #Turn with a gaussian distribution
            (x,y) =t.pos() #get position in each step
            if abs(x) > width or abs(y) > height: #If particle is out of screen, turn back
                t.right(180)
        elif dist == 'random':
            t.forward(random.random()*scale) #Move forward with a random distribution
            t.right(random.random()*360) #Turn with a random distribution
            (x,y) =t.pos() #get position in each step
            if abs(x) > width or abs(y) > height: #If particle is out of screen, turn back
                t.right(180)
    t.done()

#Call function

brownian(20, 1000, 'random')