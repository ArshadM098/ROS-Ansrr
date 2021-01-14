#!/usr/bin/env python

## TODO: incomplete script.
import rospy
from gazebo_msgs/SpawnModel.srv import spawn_urdf_model

rospy.init_node('service_call')
rospy.wait_for_service('')
rospy.ServiceProxy("spawning", spawn_urdf_model)
