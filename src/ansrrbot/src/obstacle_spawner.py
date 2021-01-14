#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Range
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, PointCloud
from math import cos,sin
threshold = 0.25

class robot_odom:

    def __init__(self):
        rospy.Subscriber("/odom", Odometry, self.update)
        self.x = 0
        self.y = 0
        self.angle = 0

    def update(self,msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.angle = msg.pose.pose.orientation.z
        rospy.loginfo("X = %f // Y = %f // 0 = %f",self.x, self.y, self.angle)



def local_to_global(local_requested,global_frame,theta): # Parameter Types is geometry_msgs.Point
    cos_theta = cos(theta)
    sin_theta = sin(theta)
    diff_x= local_requested.x - global_frame.x
    diff_y = local_requested.y - global_frame.y
    return p((diff_x * cos_theta) + (diff_y * sin_theta),(diff_x * -sin_theta) + (diff_y * cos_theta))

def p(x,y): # Creates Point using xy coordinate
    temp = Point()
    temp.x = x
    temp.y = y
    return temp

def det_obs(msg,args):
    temp = get_xy_dist(msg.range)
    if(temp < threshold ):
        # rospy.logwarn("Sensor %d: %f",args,temp)
        obstacle = local_to_global(p(temp,0),p(args.x,args.y),args.angle)
        return
    # rospy.loginfo("Sensor %d: %f",args,temp)

def get_xy_dist(sense_range):
    theta = 0.1745# 10 degrees
    return sense_range*cos(theta)



if __name__ == '__main__':
    rospy.init_node("obstacle_spawner", anonymous=False)
    ansrr = robot_odom()
    # rospy.Subscriber("/obs_us1", Range, det_obs, 1)
    # rospy.Subscriber("/obs_us2", Range, det_obs, 2)
    # rospy.Subscriber("/obs_us3", Range, det_obs, 3)
    # rospy.Subscriber("/obs_us4", Range, det_obs, 4)
    # rospy.Subscriber("/obs_us5", Range, det_obs, 5)
    rospy.Subscriber("/obs_us1", Range, det_obs, ansrr)


    rospy.spin()
    print("Ending this sensor read node")
