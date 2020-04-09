#!/usr/bin/env python
from geometry_msgs.msg import Point
from math import cos, sin
o_x = 0     # Origin of Global Coordinate
o_y = 0

class Temp:
    def __init__(self):
        print("Initialized")

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

theta = 10 #Global to Coordinate Orientation from anticlockwise
global_frame_x = 10   # Robot in Global Coordinate
global_frame_y = 10
local_requested_x = 2     # marker in local coordinate
local_requested_y = 0
global_requested_x = 0    # Goal in Global Coordinate
global_requested_y = 0
def local_global(theta,)
    cos_theta = cos(theta)
    sin_theta = sin(theta)
    diff_x = local_requested_x - global_frame_x
    diff_y = local_requested_y - global_frame_y

    global_requested_x = (diff_x * cos_theta) + (diff_y * sin_theta)
    global_requested_y = (diff_x * -sin_theta) + (diff_y * cos_theta)
