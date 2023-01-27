#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
import actionlib.msg
import assignment_2_2022.msg
import actionlib
import assignment_2_2022.msg
import os

start_description_flag=1





def target_client():


    x_position = input("\nEnter X position Please: ")
    y_position = input("\nEnter Y position Please: ")

 
    x_position = int(x_position)
    y_position = int(y_position)
 
    print(f'\nYou have entered: \nposition X: {x_position}  \nposition Y: {y_position}')
    #global client

 

    # Waits until the action server starts.

    print("\n###############################################")
    print("\nWating for connection to the action server")

    client.wait_for_server()

    # Create a goal function ,this goal will be sent to the action server
    
    goal = PoseStamped()


    goal.pose.position.x = x_position
    goal.pose.position.y = y_position

    goal = assignment_2_2022.msg.PlanningGoal(goal)


    # the goal is ready to be sent , now we send the goal to the action server.
    client.send_goal(goal)
    
    print("\nGoal is sent to the sever")
    input("\nPress Enter key to select an operation!")
    interface()
      
    #client.wait_for_result()


def cancel_target():

    client.cancel_goal()
    print(f"\nTarget is canceled")
    input("\n\nPress Enter key to select an operation!")
    interface()



def wrong():

    print("!!!! Wrong input !!!!")
    rospy.sleep(6)
    interface()



def interface():

    os.system('clear')
    print("###############################################\n")    
    print("##          Robot control interface          ##\n")
    print("###############################################\n")
    print("1:Target position\n")
    print("2:Cancel\n")
    print("3:Exit\n")   

    user_select = input("Select your operation: ")
    
    if   (user_select == "1"):
        target_client()

    elif (user_select == "2"):
        cancel_target() 

    elif (user_select == "3"):
        exit()

    else:
        wrong()


def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\n\n------------------Node description------------------\n\n")
        print("This is the node that implements an action client, ")
        print("allowing the user to set a target (x, y) or to ")
        print("cancel it.")
        input("\n\nPress Enter to continue!")
        start_description_flag=0   

    

if __name__ == '__main__':
    #try:
        # to initialize rospy node to let the SimpleActionClient publish and subscribe via ROS.
        
    start_description(start_description_flag)

    rospy.init_node('Node-A') #to define a node that we want to create .
    client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction ) #syntax for action client used in ROS where we provide both the name of the topic ,and the type of the message where we want to publish and subscribe . 
    interface() # it's a function 
    rospy.spin() # rospy.spin() to not let python exit until this node stops
   
