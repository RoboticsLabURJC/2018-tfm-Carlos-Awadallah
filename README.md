# 2018-tfm-Carlos-Awadallah

## Week 1
During the recent development of the [JdeRobot-Academy website](http://academy.jderobot.org:8000/) we have been investigating tools for its enrichment with computer vision practices. To do this, we must ensure that the Jupyter Notebook connects to the camera of the client's system, in such a way that the solution can be programmed on the images provided by that camera.

#### Selectable Video Source (Color Filter)
We begin this process by modifying the Color Filter node so that it accepts different video streams, in a configurable way. With this, the user can choose the video source he/she wants to use to solve the practice:

- Local Camera with OpenCV flow
- Video file stored in the local file system
- External camera (simulated or USB) through ROS / ICE plugins

The video source is selectable by modifying the configuration file of the exercise.

A solution for the exercise has been proposed in order to verify the correct functioning of the changes made. In addition, an entry has been created in the [developer's forum](https://developers.jderobot.org/t/color-filter-exercise/58) to discuss possible improvements or failures.

#### CamServerWeb + CamVizWeb
In the future we will try to make a new version of this practice via WebRTC + Electron. We started this path by running the JdeRobot [CamServerWeb + CamVizWeb tutorial](https://jderobot.org/Tutorials#Cameraserver-web_.2B_Cameraview-web), with recently developed tools. We found some execution problems related to incompatibilities between RosBridgeServer and some Python packages. We modified this tutorial and the installation instructions to incorporate the solution to the problem.



### Canny example in android using OpenCV libraries:

[![](http://img.youtube.com/vi/IWV2fLG0j7k/0.jpg)](http://www.youtube.com/watch?v=IWV2fLG0j7k "")
