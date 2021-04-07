#!/usr/bin/env python
# subscriber_node_class.py
 
import rospy
from geometry_msgs.msg import Point

class subscriber_node:
    def __init__(self):
        self.sub = rospy.Subscriber('robot_location', Point, self.callback)
        rospy.spin()

    def callback(self, location):
        rospy.loginfo("Received robot location: {0} ,{1}".format(location.x, location.y))

if __name__ =='__main__':
    try:
        rospy.init_node('robot_location_listener')
        sn = subscriber_node()
    except  rospy.ROSInterruptException:
        pass
