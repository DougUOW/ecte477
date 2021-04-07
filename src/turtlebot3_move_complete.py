#!/usr/bin/env python

#Complete code for correct programming techniques to drive TB3 in a circle for a
#set amount of time the stop.

#ECTE477 Lab 2

import rospy
from geometry_msgs.msg import Twist

class MoveTB3():

    def __init__(self):
        self.tb3_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate =rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)
    
    def publish_once_in_cmd_vel(self):
        """
        This is because publishing in topics sometimes fails the first time you publish
        In continuos publishing systems, this is no big deal, but in systems that only
        publish once, it is very important
        """
        while not self.ctrl_c:
            connections = self.tb3_vel_publisher.get_num_connections()
            if connections > 0:
                self.tb3_vel_publisher.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()
    
    def shutdownhook(self):
        # Works better than rospy.is_shutdown()
        self.ctrl_c = True

    def move_tb3(self, moving_time=5.0,linear_speed=0.5, angular_speed=0.5):

        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = angular_speed
        i = 0

        rospy.loginfo("Moving TB3!")
        while not self.ctrl_c and i <= moving_time:
            self.publish_once_in_cmd_vel()
            i = i+1
            self.rate.sleep()

        self.stop_tb3()

    def stop_tb3(self, linear_speed=0.0, angular_speed=0.0):

        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = angular_speed

        rospy.loginfo("Stopping TB3!")
        self.publish_once_in_cmd_vel()        

if __name__ == '__main__':
    rospy.init_node('move_tb3_test', anonymous=True)
    movetb3_object = MoveTB3()
    try:
        movetb3_object.move_tb3()
    except rospy.ROSInternalException:
        pass



