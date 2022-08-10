import os
from math import radians
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(
                'f1tenth_gym_ros'), 'launch'), '/gym_bridge_launch.py'])
        ),
        Node(
            package="pure_pursuit",
            executable="pure_pursuit_node.py",
            name="pure_pursuit_node",
            output="screen",
            emulate_tty=True,
            parameters=[
                {"lookahead_distance": 1.2},
                {"steering_angle_bound": 0.4},
                {"desired_speed": 3.0},
                {"min_speed": 1.0},
                {"proportional_control": 1.0},
                {"steering_angle_factor": 0.6},
                {"speed_factor": 1.0},
                {"sparse_waypoint_filename": 'sim_sparse'},
                {"waypoint_distance": 0.1},
            ]
        ),
        Node(
            package="pure_pursuit",
            executable="waypoint_path_service.py",
            name="waypoint_path_service",
            output="screen",
            emulate_tty=True,
            parameters=[]
        )
    ])