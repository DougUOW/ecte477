#!/usr/bin/env python

import rospy
from actionlib import SimpleActionClient
from ecte477.msg import FibonacciAction, FibonacciGoal

class fibonacci_client:
	def __init__(self, name):
		self.action_client = SimpleActionClient('fibonacci_server', FibonacciAction)
		self.action_client.wait_for_server()

		goal = FibonacciGoal(order=20)
		self.action_client.send_goal(goal)
		self.action_client.wait_for_result()
	
		result = self.action_client.get_result()
		rospy.loginfo('[Fibonacci Client] Result: {}'.format(', '.join([str(n) for n in result.sequence])))

if __name__ == '__main__':
	print "Starting ROS Fibonacci Client module"
	rospy.init_node('fibinacci_client', anonymous=True, log_level=rospy.DEBUG)
	fib = fibonacci_client('fibonacci_client')
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print "Shutting down ROS Fibonacci Client module"
