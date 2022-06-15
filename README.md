# Bike-robot

A bicycle robot simulated in the webots application. The bicycle robot mimicks a real life model as it stays still and doesnt fall imidiately as
its dimensions and weight appropriation are accurate.

# Obstacle avoidance

The robot follows a map unkown condition motion planning algorithm which is called Start-Goal Algorithm: Lumelsky Bug Algorithms

A figure will show how the algorithm works

![image](https://user-images.githubusercontent.com/57250365/173895923-514e8a78-7f1a-43f9-a689-9ec3b3b8291c.png)

=> Unknown obstacles, known start and goal.
=> Simple “bump” sensors, encoders.
=> Choose arbitrary direction to turn (left/right) to make all turns, called “local direction”
=> Motion is like an ant walking around:
    – In Bug 1 the robot goes all the way around each obstacle encountered, recording the point nearest the goal,
      then goes around again to leave the obstacle from that point.
    – In Bug 2 the robot goes around each obstacle encountered until it can continue on its previous path toward the goal.
