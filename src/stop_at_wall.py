#!/usr/bin/env python
# stop_at_wall.py

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    #print the distance to the wall
    print msg.ranges[0]

    if msg.ranges[0] > 1:
        move.linear.x = 0.1
        move.angular.z = 0.0
    
    if msg.ranges[0] < 1:
        move.linear.x = 0.0
        move.angular.z = 0.0

    pub.publish(move)

rospy.init_node('stop_at_wall_node')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()
