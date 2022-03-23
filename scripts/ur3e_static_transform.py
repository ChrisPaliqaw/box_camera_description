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
    t.child_frame_id = "base_link"
    t.transform.translation.x = -0.000018
    t.transform.translation.y = 0.000031
    t.transform.translation.z = 0.000225
    q = tf_conversions.transformations.quaternion_from_euler(0.000028, 0.000024, -0.00002)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    rate = rospy.Rate(1)

    while True:
        br.sendTransform(t)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('ur3e_static_broadcaster')
    publish_static()
    rospy.spin()