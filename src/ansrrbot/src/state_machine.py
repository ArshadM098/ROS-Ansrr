#!/usr/bin/env python

import rospy
from smach import State,StateMachine
from time import sleep

class MANUAL_OVERRIDE(State):
    def __init__(self):
        State.__init__(self, outcomes=['failed','success'])
    def execute(self, userData):
        print("System is executing 'MANUAL_OVERRIDE' procedures")
        return 'success'
class GET_HOME(State):
    def __init__(self):
        State.__init__(self, outcomes=['failed','success'])
    def execute(self, userData):
        print("System is executing 'GET_HOME' procedures")
        print("Setting current position as origin (0,0)")
        return 'success'
class START_GMAPPING(State):
    def __init__(self):
        State.__init__(self, outcomes=['failed','success'])
    def execute(self, userData):
        print("System is executing 'START_GMAPPING' procedures")
        return 'success'
class GET_POINTS(State):
    def __init__(self):
        State.__init__(self, outcomes=['failed','success'])
    def execute(self, userData):
        print("System is executing 'MANUAL_OVERRIDE' procedures")
        print("Getting Points for Clearing Region")
        return 'success'
class MAKE_MAP(State):
    def __init__(self):
        State.__init__(self, outcomes=['failed','success'])
    def execute(self, userData):
        print("System is executing 'MAKE_MAP' procedures")
        return 'success'
class DISPLAY_MAP(State):
    def __init__(self):
        State.__init__(self, outcomes=['failed','success'])
    def execute(self, userData):
        print("System is executing 'DISPLAY_MAP' procedures")
        return 'success'
class USER_CONFIRMATION(State):
    def __init__(self):
        State.__init__(self, outcomes=['failed','confirm','update'])
    def execute(self, userData):
        print("System is executing 'USER_CONFIRMATION' procedures")
        return 'confirm'
class UPDATE_POINTS(State):
    def __init__(self):
        State.__init__(self, outcomes=['failed','success'])
    def execute(self, userData):
        print("System is executing 'UPDATE_POINTS' procedures")
        return 'success'

def main():
    print('Creating SMACH')
    rospy.init_node('robot_smach', anonymous=False)
    sm = StateMachine(['complete','failed'])

    with sm:
        StateMachine.add('MANUAL_OVERRIDE',MANUAL_OVERRIDE(),
        transitions={'success':'GET_HOME','failed':'failed'})
        StateMachine.add('GET_HOME',GET_HOME(),
        transitions={'success':'START_GMAPPING','failed':'failed'})
        StateMachine.add('START_GMAPPING',START_GMAPPING(),
        transitions={'success':'GET_POINTS','failed':'failed'})
        StateMachine.add('GET_POINTS',GET_POINTS(),
        transitions={'success':'MAKE_MAP','failed':'failed'})
        StateMachine.add('MAKE_MAP',MAKE_MAP(),
        transitions={'success':'DISPLAY_MAP','failed':'failed'})
        StateMachine.add('DISPLAY_MAP',DISPLAY_MAP(),
        transitions={'success':'USER_CONFIRMATION','failed':'failed'})
        StateMachine.add('USER_CONFIRMATION',USER_CONFIRMATION(),
        transitions={'confirm':'complete','update':'UPDATE_POINTS','failed':'failed'})
        StateMachine.add('UPDATE_POINTS',UPDATE_POINTS(),
        transitions={'success':'MAKE_MAP','failed':'failed'})

    sm.execute()

if __name__ == '__main__':
    main()
