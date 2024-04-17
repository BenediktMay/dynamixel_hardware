#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from rclpy.action import ActionClient

#/joint_trajectory_controller/follow_joint_trajectory control_msgs/action/FollowJointTrajectory
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectoryPoint
from builtin_interfaces.msg import Duration


#manual send of positions
#ros2 action send_goal /joint_trajectory_controller/follow_joint_trajectory control_msgs/action/FollowJointTrajectory -f "{nt_trajectory_controller/fol  trajectory: {ctory control_msgs/action/FollowJointTrajectory -f "{
#    joint_names: [joint1],
#    points: [es: [joint1],
#      { positions: [-1.57], time_from_start: { sec: 2 } },
#      { positions: [1.57], time_from_start: { sec: 4 } },,
#      { positions: [0], time_from_start: { sec: 6 } }} },
#    ] { positions: [0], time_from_start: { sec: 6 } }
#  } ]
#}"}
class SendPositionsTest(Node):
    def __init__(self):
        super().__init__('send_positions_test')
        self.send_positions_test_action_server = ActionClient(
            self, 
            FollowJointTrajectory, 
            'joint_trajectory_controller/follow_joint_trajectory')
        
    def send_goal(self):
        self.get_logger().info('entering send_goal')
        goal_msg = FollowJointTrajectory.Goal()
        goal_msg.trajectory.joint_names = ['joint1']
        goal_msg.trajectory.points = [
            JointTrajectoryPoint(positions=[-1.57], time_from_start=Duration(sec=2)),
            JointTrajectoryPoint(positions=[1.57], time_from_start=Duration(sec=4))
        ]

        self.get_logger().info('waiting for server')
        self.send_positions_test_action_server.wait_for_server()
        self.get_logger().info('Sending goal')
        self.send_positions_test_action_server.send_goal_async(goal_msg)

def main(args=None):
    rclpy.init(args=args)
    send_positions_test = SendPositionsTest()
    send_positions_test.send_goal()
    rclpy.spin(send_positions_test)
    rclpy.shutdown()