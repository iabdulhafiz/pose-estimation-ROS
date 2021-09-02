#! /home/ibra/dvs_ws/src/pose_estimation/DeepPoseEstimation/blender/2.93/python/bin/python3.9


import cv2
import sys
print("Python version sss")
print (sys.version)
print("Version info.")
print (sys.version_info)

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
