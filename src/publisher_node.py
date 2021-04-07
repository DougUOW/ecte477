#!/usr/bin/env python
# publisher_node.py
import rospy
from geometry_msgs.msg import Point

def my_publisher_method():
    # Set up node  and  publisher
    rospy.init_node('robot_location_publisher')
    pub = rospy.Publisher('robot_location', Point, queue_size =10)
    rate = rospy.Rate(10) # 10hz
    # Initialise  the  location  of the  robot
    location = Point()
    location.x = 10
    location.y = 10
    location.z = 10
    # Loop at 10Hz
    while not rospy.is_shutdown():
        # Publish  current  location
        rospy.loginfo("Publishing location: {0} ,{1}".format(location.x, location.y))
        pub.publish(location)
        # Simulate a move is some  direction
        location.x += 1
        location.y += 2
        # Sleep  so this  loop  runs at 10 Hz
        rate.sleep()
        
if __name__  =='__main__':
    try:
        my_publisher_method()
    except  rospy.ROSInterruptException:
        pass
