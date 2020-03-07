#!/usr/bin/env python

## TODO: incomplete script.
import rospy

rospy.init_node('us_reader')
pub = rospy.Publisher('us_array',Int32)

rate = rospy.Rate(2)
while not rospy.is_shutdown():
    pub.publish(count)
    count += 1
    rate.sleep()
