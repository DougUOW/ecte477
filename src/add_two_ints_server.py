#!/usr/bin/env python

# Used for ECTE477. 5.1.3 in 2021. 3.3 in 2020.
# Exercise is looking at how ROS Services work. This is the server node.
# Node is designed to add two integers supplied from the client node.
# Launch command = rosrun ecte477 add_two_ints_server.py
# Client node = add_two_ints_client.py
# Launch server node first.
# Code taken from Brendan Halloran.

import rospy
from ecte477.srv import AddTwoInts, AddTwoIntsResponse

def handle_add_two_ints(req):
	print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
	return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
	rospy.init_node('add_two_ints_server')
	s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
	print "Ready to add two ints."
	rospy.spin()

if __name__ == "__main__":
	add_two_ints_server()
