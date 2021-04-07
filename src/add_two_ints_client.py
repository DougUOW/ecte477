#!/usr/bin/env python

# Used for ECTE477. 5.1.4 in 2021. 3.4 in 2020.
# Exercise is looking at how ROS Services work. This is the client node.
# Node is designed to send two integres to the server node, where addition will occur.
# Launch command = rosrun ecte477 add_two_ints_client.py
# Server node = add_two_ints_server.py
# Launch server node first.
# Code taken from Brendan Halloran.

import sys
import rospy
from ecte477.srv import *

def add_two_ints_client(x, y):
	rospy.wait_for_service('add_two_ints')
	try:
		add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
		resp1 = add_two_ints(x, y)
		return resp1.sum
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def usage():
	return "USAGE: %s [x y]"%sys.argv[0]

if __name__ == "__main__":
	if len(sys.argv) == 3:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
	else:
		print usage()
		sys.exit(1)
	print "Requesting %s+%s"%(x, y)
	print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))

