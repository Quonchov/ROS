#!/usr/bin/env python
import rospy
from cmvision.msg import Blobs, Blob
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from sensor_msgs.msg import CameraInfo


class MarkerBasics(object):

    def __init__(self):
        self.marker_objectlisher = rospy.Publisher('/marker_greenball', Marker, queue_size=1)
        self.rate = rospy.Rate(1)
        self.init_marker(index=0,z_val=0)

    def init_marker(self,index=0, z_val=0):
        self.marker_object = Marker()
        self.marker_object.header.frame_id = "/camera_link"
        self.marker_object.header.stamp    = rospy.get_rostime()
        self.marker_object.ns = "mira"
        self.marker_object.id = index
        self.marker_object.type = Marker.SPHERE
        self.marker_object.action = Marker.ADD

        my_point = Point()
        my_point.z = z_val
        self.marker_object.pose.position = my_point

        self.marker_object.pose.orientation.x = 0
        self.marker_object.pose.orientation.y = 0
        self.marker_object.pose.orientation.z = 0.0
        self.marker_object.pose.orientation.w = 1.0
        self.marker_object.scale.x = 0.05
        self.marker_object.scale.y = 0.05
        self.marker_object.scale.z = 0.05

        self.marker_object.color.r = 0.0
        self.marker_object.color.g = 1.0
        self.marker_object.color.b = 0.0
        # This has to be otherwise it will be transparent
        self.marker_object.color.a = 1.0

        # If we want it for ever, 0, otherwise seconds before desapearing
        self.marker_object.lifetime = rospy.Duration(0)

    def update_position(self,position):        
        self.marker_object.pose.position = position
        self.marker_objectlisher.publish(self.marker_object)


class BallDetector(object):
    def __init__(self):        
        self.rate = rospy.Rate(1)
        self.save_camera_values()        
        rospy.Subscriber('/blobs', Blobs, self.greenball_detect_callback)        
        self.markerbasics_object = MarkerBasics()

    def save_camera_values(self):
        data_camera_info = None
        while data_camera_info is None:
            data_camera_info = rospy.wait_for_message('/mira/mira/camera1/camera_info', CameraInfo, timeout=5)
            rospy.loginfo("No Camera info found, trying again")


        self.cam_height_y = data_camera_info.height
        self.cam_width_x = data_camera_info.width
        rospy.loginfo("CAMERA INFO:: Image width=="+str(self.cam_width_x)+", Image Height=="+str(self.cam_height_y))

    def greenball_detect_callback(self,data):

        if(len(data.blobs)):

            for obj in data.blobs:
                if obj.name == "GreenBall":
                    rospy.loginfo("Blob <"+str(obj.name)+"> Detected!")
                    greenball_point = Point()
                    # There is a diference in the axis from blobs and the camera link frame.
                    # We convert to percent of the screen
                    # TODO: Take into account the Depth distance and camera cone.
                    rospy.loginfo("self.cam_width_x="+str(self.cam_width_x))
                    rospy.loginfo("self.cam_width_x="+str(self.cam_height_y))
                    rospy.loginfo("obj.x="+str(obj.x))
                    rospy.loginfo("obj.y="+str(obj.y))

                    middle_width = float(self.cam_width_x)/2.0 
                    middle_height = float(self.cam_height_y)/2.0

                    greenball_point.x = (obj.x - middle_width) / float(self.cam_width_x)
                    greenball_point.z = (obj.y - middle_height) / float(self.cam_height_y)                    
                    greenball_point.y = 0.6            
                    rospy.loginfo("blob is at Point="+str(greenball_point))
                    self.markerbasics_object.update_position(position=greenball_point)


        else: 
             rospy.logwarn("No Blobs Found")


    def start_loop(self):
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('greenball_detections_listener_node', anonymous=True)
    greenball_detector_object = BallDetector()
    greenball_detector_object.start_loop()