# ecte477
Package for Lab Classes relating to ECTE477 Autonomous Systems at UOW
## Description
This package provides two simulated worlds that will be used during ECTE477 lab classes.
The worlds have been simulated in Gazebo, and are designed to allow students to test basic functionality of the Turtlebot3 robot.

###### blocked_road.world
This world consists simply of a straight road with a Turtlebot3 placed in the centre of the road. 3 meters from the Turtlebot3 is
a brick wall which placed across the road. Some other random objects are located in the world, which may be used for additional labs.
The brick wall, ground plane and objects have textures applied to them.

###### blocked_road_low_res.world
This world functions the same as blocked_road.world, however textures and the random objects have been removed. This world is provided in case any students
expeience any hardware resource issues.

## Launch Codes
`roslaunch ecte477 blocked_road.world`  
`roslaunch ecte477 blocked_road_low_res.world`

## Designed and Tested With:
Ubuntu 16.04  
ROS Kinetic Kame  
Gazebo 7.0
