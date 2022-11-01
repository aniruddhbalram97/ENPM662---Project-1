#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def talker():
        pub_rear_l = rospy.Publisher('/Robot_Assembly/rear_wheel_left_controller/command', Float64, queue_size=10)
        pub_rear_r = rospy.Publisher('/Robot_Assembly/rear_wheel_right_controller/command', Float64, queue_size=10)
        pub_front_l = rospy.Publisher('/Robot_Assembly/front_wheel_left_steering_controller/command', Float64, queue_size=10)
        pub_front_r = rospy.Publisher('/Robot_Assembly/front_wheel_right_steering_controller/command', Float64, queue_size=10)
        rospy.init_node('publisher', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        i = 1
        while(i<=13):
           print("Publishing\n")
           vel_val = -5
           pub_rear_l.publish(vel_val)
           pub_rear_r.publish(vel_val)
           pub_front_l.publish(0)
           pub_front_r.publish(0)
           i+=1
           rospy.sleep(1)
   
if __name__ == '__main__':
       try:
           talker()
       except rospy.ROSInterruptException:
           pass