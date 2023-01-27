#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import os

start_description_flag=1

  #the goals reached and canceled
reached_goal_counter =0
canceled_goal_counter = 0
sequence =1 


def callback_service(req):
    global canceled_goal_counter , reached_goal_counter , sequence
    print(f"Sequence: {sequence}\nNumber of canceled goal: {canceled_goal_counter}\nnumber of reached goal: {reached_goal_counter}")
    print("**********************************")
    sequence += 1
    return EmptyResponse()



def callback_subscriber(data):

    if data.status.status == 2:

        global canceled_goal_counter
        canceled_goal_counter += 1
    
    elif data.status.status == 3:

        global reached_goal_counter
        reached_goal_counter += 1


def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\n\n------------------Node description------------------\n\n")
        print("This node is a service node that, when called,")
        print("prints the number of goals reached and canceled.")
        input("\n\nPress Enter key to continue!")
        start_description_flag=0   


if __name__ == "__main__":

    start_description(start_description_flag)

    rospy.logwarn("service started")

    rospy.init_node('Node-C')

    rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, callback_subscriber) #this shows that after receiving data from the /reaching_goal/result topic we call the function callback_subscriber explained above.

    rospy.Service('reach_cancel_ints', Empty, callback_service)

    rospy.spin()
   
