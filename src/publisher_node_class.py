#!/usr/bin/env python
# publisher_node_class.py
import rospy
from geometry_msgs.msg import Point

class publisher_node:
    def __init__(self):
        # Set up node  and  publisher
        self.pub = rospy.Publisher('robot_location', Point, queue_size =10)
        self.rate = rospy.Rate(10) # 10hz
        # Initialise  the  location  of the  robot
        self.location = Point()
        self.location.x = 10
        self.location.y = 10
        self.location.z = 10
        # Loop at 10Hz
        while not rospy.is_shutdown():
            self.publish_and_update()
            # Sleep so this loop runs at 10Hz
            self.rate.sleep()

    def publish_and_update(self):
        #Publish current location
        rospy.loginfo("Publishing location: {0} ,{1}".format(self.location.x, self.location.y))
        self.pub.publish(self.location)
        # Simulate a move in some direction
        self.location.x += 1
        self.location.y += 2

if __name__  =='__main__':
    try:
        rospy.init_node('robot_location_publisher')
        pn = publisher_node()
    except rospy.ROSInterruptException:
        pass
