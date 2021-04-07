#!/usr/bin/env python

#this code will subscribe to /scan topic and read lidar dsitance
#data. the lidar array of data contains 360 values. the first index
#in the array, index=0, is directly in front of the TB3. index=179
#is directly behind the TB3

#used for ECTE477 Lab2

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print(msg.ranges[0])

rospy.init_node('read_lidar')

sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()