#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from assignment_2_2022.msg import odom_custom_msg
import os

start_description_flag=1



def callback(data):

    my_pub = rospy.Publisher('position_and_velocity', odom_custom_msg, queue_size=5)

    my_message = odom_custom_msg()

    my_message.x = data.pose.pose.position.x
    my_message.y = data.pose.pose.position.y
    my_message.vel_x = data.twist.twist.linear.x
    my_message.vel_y = data.twist.twist.linear.y

    print("***************************")
    print(my_message)
    my_pub.publish(my_message) #to publish the robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the topic /odom.
    print("***************************")


def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\n\n------------------Node description------------------\n\n")
        print("This node publishes the robot position and velocity ")
        print("as a custom message (x,y, vel_x, vel_z), by relying ")
        print("on the values published on the topic /odom.")
        input("\n\nPress Enter key to continue!")
        start_description_flag=0   
    

if __name__ == '__main__':

    start_description(start_description_flag)
    rospy.init_node('Node-B')    
    rospy.Subscriber("/odom", Odometry, callback) #to subscribe to get data from the topic /odom of class /Odometry
    rospy.spin()
