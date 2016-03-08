# Floating barbell.
# initialize parameters
hg = 0 # height of green end
hr = 0 # height of red end
t=0 # time parameter
dt = 0.01 # time step

# this happens once at the start of execution
def setup():
    size(500,500) # set the size of the canvas

# this happens repeatedly, like frames in a movie
def draw():
    global t, hg, hr, dt
    background(255) # set the background to white
    # vary the heights using sine function
    hr = height/3*sin(2*PI*t)
    hg = height/3*sin(PI*t)
    fill(255,0,0) # set the left end to red
    ellipse(width/2-width/3,height/2+hr,10,10) # draw left end
    fill(0,255,0) # set the right end to green
    ellipse(width/2+width/3,height/2+hg,10,10) # draw right end
    # draw line connecting the ends
    line(width/2-width/3,height/2+hr,width/2+width/3,height/2+hg)
    t = t+dt # increment time