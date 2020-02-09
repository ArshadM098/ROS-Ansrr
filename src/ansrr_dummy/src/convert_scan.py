#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def convert_cb(msg,scan_pub):
    temp = []
    for i in xrange(len(msg.ranges)):
        if(msg.ranges[i] > 10):
            temp.append(10)
        else:
            temp.append(msg.ranges[i])
    msg.ranges = tuple(temp)
    scan_pub.publish(msg)

if( __name__ == "__main__"):
    rospy.init_node('convert_scan')
    scan_pub = rospy.Publisher("scan", LaserScan, queue_size=10)
    rospy.Subscriber("raw_scan",LaserScan,convert_cb,scan_pub)
    rospy.spin()
