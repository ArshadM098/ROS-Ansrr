#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool, String
import sys, tty, termios, select


def input_callback(msg,args):
    pub_mode_control = args[0]
    pub_keys = args[1]
    rate = args[2]
    print("Set Command Received. Sending ACK...")
    rospy.sleep(2)
    pub_mode_control.publish(True)
    old_attr = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    while(not rospy.is_shutdown()):
        if select.select([sys.stdin],[],[], 0)[0] == [sys.stdin]:
            pub_keys.publish(sys.stdin.read(1))
        rate.sleep()
    termios.tcsetattr(sys.stdin,termios.TCSADRAIN, old_attr)
    print("Ending Manual Input Interface Access...")

if __name__ == '__main__':
    rospy.init_node("manual_input", anonymous=False)

    print("Waiting for SET Command....")
    pub_mode_control = rospy.Publisher("mode_control_ACK", Bool, queue_size=1)

    pub_keys = rospy.Publisher("keys_input", String, queue_size=1)
    rate = rospy.Rate(100)
    rospy.Subscriber("mode_control_SET", Bool,input_callback,(pub_mode_control,pub_keys,rate))
    rospy.spin()
