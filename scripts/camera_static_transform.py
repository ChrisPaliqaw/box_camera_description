#!/usr/bin/env python  
import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg


def publish_static():
    br = tf2_ros.TransformBroadcaster()

    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = "pc_cam_base_link"
    '''
    <arg name="x" default="4.71" />
    <arg name="y" default="-4.279791" />
    <arg name="z" default="0.02" />
    <arg name="R" default="0.0" />
    <arg name="P" default="0.0" />
    <arg name="Y" default="0.0" />
    '''
    t.transform.translation.x = 4.71
    t.transform.translation.y = -4.279791
    t.transform.translation.z = 0.02
    q = tf_conversions.transformations.quaternion_from_euler(0.0, 0.0, 0.0)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    rate = rospy.Rate(1)

    while True:
        br.sendTransform(t)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('camera_static_broadcaster')
    publish_static()
    rospy.spin()