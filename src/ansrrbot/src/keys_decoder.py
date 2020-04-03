#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

move_key_map = {'w': [0,-1], # Forward
                'a': [-1,0], # Left
                's': [ 0,1], # Backward
                'd': [1, 0], # Right
                'p': [0, 0], #Stop
}

def keys_callback(msg, pub_twist):
    print("Input Detected")
    if (len(msg.data) == 0 or not move_key_map.has_key(msg.data[0])):
        print("Invalid Key")
        return
    vels = move_key_map[msg.data[0]]
    t = Twist()
    t.angular.z = vels[0]
    t.linear.x = vels[1]
    pub_twist.publish(t)

if __name__ == '__main__':
    rospy.init_node("keys_decoder", anonymous=False)
    pub_twist = rospy.Publisher('cmd_vel',Twist, queue_size=1)
    rospy.Subscriber("keys_input",String ,keys_callback ,pub_twist)
    print("Started Translating Keys to Vel")
    rospy.spin()
