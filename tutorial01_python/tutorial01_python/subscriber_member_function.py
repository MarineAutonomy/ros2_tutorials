# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
import numpy as np
import math

from std_msgs.msg import String
from sensor_msgs.msg import Imu


def euler_from_quaternion(quaternion):
    """
    Converts quaternion (w in last place) to euler roll, pitch, yaw
    quaternion = [x, y, z, w]
    Bellow should be replaced when porting for ROS 2 Python tf_conversions is done.
    """
    x = quaternion[0]
    y = quaternion[1]
    z = quaternion[2]
    w = quaternion[3]

    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = np.arctan2(sinr_cosp, cosr_cosp)

    sinp = 2 * (w * y - z * x)
    pitch = np.arcsin(sinp)

    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = np.arctan2(siny_cosp, cosy_cosp)

    return math.degrees(roll), math.degrees(pitch), math.degrees(yaw)


class SubPub(Node):

    def __init__(self):
        super().__init__('pub_sub_node_NA18B103')
        
        # publisher that publishes orientation in terms of euler angles
        ## CREATE A PUBLISHER OBJECT
        self.publisher_=
        
        ### CREATE A SUBSCRIBER OBJECT
        self.subscriber = 

    def listener_callback(self, msg):
        ###  below write a code that:
        # reads sbg message
        # extract quaternions out of it
        # convert it to euler angles
        # populate the string message below
        # Use the function above to convert from quaternion to euler
        # finally remember to update setup.py
       
        # formulate a String message 
        euler_msg = String()
        euler_msg.data = f"yaw = {yaw}\t pitch = {pitch}\t roll = {roll}\t"
        self.publisher_.publish(euler_msg)


def main(args=None):
    rclpy.init(args=args)

    print("setting up a subscriber...")

    minimal_subscriber_publisher = SubPub()

    print("starting to read data...")

    rclpy.spin(minimal_subscriber_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
