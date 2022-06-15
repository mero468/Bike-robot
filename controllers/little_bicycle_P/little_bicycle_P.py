"""little_bicycle_P controller."""

from controller import Robot #Supervisor
from controller import DistanceSensor
# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
ds = robot.getDevice('ds_left')
ds.enable(timestep)

ds1 = robot.getDevice('ds_left1')
ds1.enable(timestep)



# get wheel motor
whemotor = robot.getDevice('wheel motor')
whemotor.setPosition(float('inf'))
whemotor.setVelocity(0)

# get handlebars motor
hndmotor = robot.getDevice('handlebars motor')
hndmotor.setPosition(0)

# keyboard enable
robot.keyboard.enable(timestep)
robot.keyboard = robot.getKeyboard()

# Initialize camera
camera = robot.getDevice('camera')
camera.enable(timestep*4)

# Max bicycle velocity
maxS = 11

# Handlebar angle
hMax = 0.1920 # rads (11°) Max

hndB = 0 #-hMax # default: right

# Ride mode (1 autoatic; 0 manual)
autoR = 0
avoidObstacleCounter = 0
# Main loop:
key = 0
while robot.step(timestep) != -1:

    # Set velocity rear wheel
    whemotor.setVelocity(6)
    hndmotor.setPosition(0)
    #turn right
    if avoidObstacleCounter > 0:
            avoidObstacleCounter -= 1
            hndmotor.setPosition(hMax)
            autoR = 0
            whemotor.setVelocity(-3)
    else:  # read sensors
        if ds.getValue() <700 or ds1.getValue()<700:
           avoidObstacleCounter = 100
              
    
    # if (key == 314): # left key
        # hndB = hMax
        # autoR = 0
    # elif (key == 316): # right key
        # hndB = -hMax
        # autoR == 0
    # elif (autoR == 0):
        # hndB = 0 # center
    # if (key == 315):
        # hndB = -hMax 
        # autoR = 1 # automatic on

    pass
