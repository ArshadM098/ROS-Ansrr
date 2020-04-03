#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool, String
import sys, tty, termios, select


if __name__ == '__main__':
    rospy.init_node("manual_input", anonymous=False)

    print("Waiting for SET Command....")
    pub_mode_control = rospy.Publisher("mode_control_ACK", Bool, queue_size=10)

    pub_keys = rospy.Publisher("keys_input", String, queue_size=1)
    rate = rospy.Rate(100)

    if(rospy.wait_for_message("mode_control_SET", Bool,60).data):
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
