#!/usr/bin/env python
# subscriber_node.py

import rospy
from geometry_msgs.msg import Point

def my_callback(location):
    rospy.loginfo("Recieved Robot Location: {0},{1}".format(location.x, location.y))

def my_subscriber_method():
    rospy.init_node('robot_location_listener')
    rospy.Subscriber('robot_location', Point, my_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        my_subscriber_method()
    except rospy.ROSInterruptException:
        pass