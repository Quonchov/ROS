#!/usr/bin/env python

ros::Subscriber subPointCloud
ros::Publisher pubPointCloud

cv::Mat imageFrame
imageFrame = cv::Mat(cloud->height, cloud->width, CV_8UC3)

# raw depth value from RGB pixel coordinate
int i = (u) + (v)*cloud->width

# 3D coordinates from point cloud using depth value
float x3Ddepth = (float)cloud->points[i].x
float y3Ddepth = (float)cloud->points[i].y
float z3Ddepth = (float)cloud->points[i].z