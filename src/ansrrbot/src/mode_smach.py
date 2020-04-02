#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

if __name__ == '__main__':
    rospy.init_node("mode_smach", anonymous=False)
    print("Waiting for SET Command....")
    pub = rospy.Publisher("mode_control_ACK", Bool, queue_size=10)
    if(rospy.wait_for_message("mode_control_SET", Bool,60).data):
        print("Set Command Received. Sending ACK...")
        rospy.sleep(2)
        pub.publish(True)
        while(not rospy.is_shutdown()):
            usrInput = raw_input("Press WASD to move: ")
            print(usrInput)
            if(usrInput == 'z'):
                break
