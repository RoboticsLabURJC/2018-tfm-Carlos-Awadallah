# 2018-tfm-Carlos-Awadallah

## Week 11

We have made some improvements in the user experience, such as clear all outputs when the students clicks on any button, so that they won't need to restar the kernel during the coding and debugging process. We have also replaced the "Play Code" and "Pause Code" buttons with an unique toggle "Play Code / Pause Code" button, which is more clear:

![nbextensions](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/playtoggle.png)

![nbextensions](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/pausetoggle.png)

We are close to integrating this new exercise in the JdeRobot-Academy web practices set, contributing with a new practice in computer vision. The code is already available in [GitLab](https://gitlab.jderobot.org/JdeRobot-Academy/exercises/tree/master/jupyter/color_filter_opencv).

We also did some research in other tools that allow us to enrich the functionality and intuitiveness of the exercises:
  - JupyterLab
  - Extensions
  
And also another ones to get closer to local execution of Notebooks stored on a remote server.
  

## Week 10
To make the experience of the users of this exercise easier, we have decided to implement buttons that act as interactive widgets between the student and the Notebook, which will be responsible for executing the actions implemented on Week 9, both the academic pause and the visualization (the latter can be activated or deactivated whenever the student wants).

We have improved the visualization loop to show filtered images every second, and also to display a warning message if a filtered image has not been established yet. 
All these widgets will be responsible, in addition, to manage the cleaning of the output of the cell where the code is executed, in such a way that the student does not need to restart the kernel or leave the booklet to solve the exercise and debug it.

##### [YOTUBE VIDEO] Buttons for Play, Pause and Visualization On/Off
[![buttons](https://img.youtube.com/vi/00w6aofU95A/0.jpg)](https://www.youtube.com/watch?v=00w6aofU95A "")

## Week 9

### Visualization Loop
Taking advantage of the infinite loop of the iterative method that executes the algorithm of the students, we have programmed the visualization of the filtered images resulting from the execution of said algorithm in the loop, sampling every certain iterations to print a filtered image in the Notebook every 3 seconds. With this, we extended the set of debugging tools for this exercise:

##### [YOTUBE VIDEO] Visualization Loop printing filtered images each 3sec
[![visloop](https://img.youtube.com/vi/BBZKI12Hxtg/0.jpg)](https://www.youtube.com/watch?v=BBZKI12Hxtg "")

### Academic Pause
To make it easier for students to complete the task, we have modified the Notebook of this exercise so that it follows a "Live Programming" philosophy, with which students have tools to pause the execution of the code, make changes to their algorithm and rerun their code with the changes made, all without having to restart the kernel or leave the Notebook:

##### [YOTUBE VIDEO] Academic Pause
[![academicpause](https://img.youtube.com/vi/lGeGHJZUxpY/0.jpg)](https://www.youtube.com/watch?v=lGeGHJZUxpY "")

## Week 8
As part of the refinement of the visualization and the interaction with the Jupyter Notebook of the Color Filter exercise, I have found and tested a series of tools not officially related to the IPython development team that allow to add functionality to the Jupyter Notebook. These extensions are mostly written in Javascript and will be loaded locally in client's browser. These are the [nbextensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions).

The link above contains a brief description of the repository and the extensions, a recipe for the installation and a user guide. I've installed as shown and tested two of the extensions provided: Initialization Cells and Hide Cell. When finishing the installation, a new section in the tree section toolbar is added:

![nbextensions](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/nbextensions1.png)

### Initialization Cells
Once installed, you can enable this extensions via [jupyter_nbextensions_configurator](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator):
![jupyter_nbextensions_configurator](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/nbextensions2.png)

You may have problems by enabling this way due to lacks of permissions (depending on your system). If so, just open a temrinal and type:
```
sudo jupyter nbextension enable init_cell/main
```
Once enabled, selecting the necessary toolbars for each extension as shown,
![toolbars](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/nbextensions5.png) 
a toolbar is added to each cell with options to mark the cell as "initialization cell", in such a way that when reloading the page (and restarting the kernel) the marked cells will autoexecute:

![checkbox](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/nbextensions3.png) 

### Hide Cells
Similar to the previous extension, there is another one that allows to hide the marked cells. Together with the previous one, the use of these extensions will help me to create a button in the Notebook without the code that generates it being visible.

Again, we need to enable this extension using the Jupyter nbextensions Configurator, or running:
```
sudo jupyter nbextension enable hide_input/main
```
Then, as shown [here](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/hide_input/readme.html), we need to mark the cell to be hidden. I've done it by modifying cell's metadata:

![metadata](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/nbextensions4.png)

THE RESULT IS THE FOLLOWING:
##### [YOTUBE VIDEO] Result of the extensions 'Initialization Cells' added to Color Filter Notebook.
[![catmousecompetition](https://img.youtube.com/vi/e2_fgAAeLx4/0.jpg)](https://www.youtube.com/watch?v=e2_fgAAeLx4 "")

## Week 7
On the occasion of the celebration of [IROS2018](https://www.iros2018.org/) in Madrid, and the contribution of JdeRobot to the conference with the [Program-A-Robot-2018](https://jderobot.org/Program-A-Robot-2018) contest, we have made a break to help in the organization and participate in it. During this week I prepared solutions for the two exercises proposed for the contest: 

Cat & Mouse
![catmouse](http://jderobot.org/store/jmplaza/uploads/campeonato-drones/dronecatmouse.jpg)

Escape from the hangar
![hangar](http://jderobot.org/store/jmplaza/uploads/campeonato-drones/hangar.jpg)

### Competition 
##### [YOTUBE VIDEO] Execution during the competition.
[![catmousecompetition](https://img.youtube.com/vi/V7mwVIvlWqk/0.jpg)](https://www.youtube.com/watch?v=V7mwVIvlWqk "")

### Research
In parallel I have started an investigation to discover tools with which to refine the visualization of the Color Filter practice.

### Beta-testing
Due to recent advances in new practices, I have acted as a beta-tester of the [Chrono](https://github.com/PabloMorenoVera/Academy/tree/master/exercises/chrono) practice, with which JdeRobot-Academy will soon be expanded:

![Chrono World](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/chrono1.png)
![Chrono GUI](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/chrono2.png)

## Week 6
We fine-tune details and complete the Jupyter Notebook of the Color Filter practice assuming that the necessary components are executed locally (camera).

## Week 5 
We continued exploring and testing the 'Colaboratory' solution. We have also made a small break to become Academy Web's beta-tester to fine-tune the server and correct minor flaws in order to use it in the [IROS](https://www.iros2018.org/) PROGRAM-A-ROBOT contest.

## Weeks 3 and 4
The next steps are to modify the Academy Web Server to store the Notebooks and take advantage of the computer capacity of the student's system (local kernel and remote notebook). With this we will be able to have the Notebook on the Web and connect it with the local camera of each student, without needing them to have the Notebook.

#### Research
We explored different ways to achieve the above, learning the [internal architecture of Jupyter](https://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html), and found a possible solution to the problem:

LOCAL RUNTIME -> https://github.com/googlecolab/jupyter_http_over_ws
LOCAL RUNTIME -> https://research.google.com/colaboratory/local-runtimes.html

Now it's time to test it.

We also started to explore the new WebSim tool for future projects.

## Week 2
#### Selectable Video Source (Color Filter Notebook)
Once the node has been modified to accept video from the local camera, we have done the same with the Jupyter Notebook version. This new booklet also accepts different configurable video sources. The main one will be to obtain the flow of the student's local camera with OpenCV.

##### [YOTUBE VIDEO] Selectable Source (Camera Stream).
[![Selectable Source](https://img.youtube.com/vi/meVvdFs3Vt0/0.jpg)](https://www.youtube.com/watch?v=meVvdFs3Vt0 "")
##### [YOTUBE VIDEO] Selectable Source (Output).
[![Output](https://img.youtube.com/vi/D8dOrv6z3BM/0.jpg)](https://www.youtube.com/watch?v=D8dOrv6z3BM "")

## Week 1
During the recent development of the [JdeRobot-Academy website](http://academy.jderobot.org:8000/) we have been investigating tools for its enrichment with computer vision practices. To do this, we must ensure that the Jupyter Notebook connects to the camera of the client's system, in such a way that the solution can be programmed on the images provided by that camera.

#### Selectable Video Source (Color Filter)
We begin this process by modifying the Color Filter node so that it accepts different video streams, in a configurable way. With this, the user can choose the video source he/she wants to use to solve the practice:

- Local Camera with OpenCV flow
- Video file stored in the local file system
- External camera (simulated or USB) through ROS / ICE plugins

The video source is selectable by modifying the configuration file of the exercise.

#### Solution
A solution for the exercise has been proposed in order to verify the correct functioning of the changes made. In addition, an entry has been created in the [developer's forum](https://developers.jderobot.org/t/color-filter-exercise/58) to discuss possible improvements or failures.

![Input](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/inputImage.png)
![Smooth](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/smoothImage.png)
![HSV](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/hsvImage.png)
![Threshold](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/thresholdImage.png)
![Output](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/filteredImage.png)

#### CamServerWeb + CamVizWeb
In the future we will try to make a new version of this practice via WebRTC + Electron. We started this path by running the JdeRobot [CamServerWeb + CamVizWeb tutorial](https://jderobot.org/Tutorials#Cameraserver-web_.2B_Cameraview-web), with recently developed tools. We found some execution problems related to incompatibilities between RosBridgeServer and some Python packages. We modified this tutorial and the installation instructions to incorporate the solution to the problem.

### Add-Ons
We have added a button that allows the student to print several consecutive frames in the Notebook (both the video of the camera and the successive images segmented by his/her algorithm).

##### [YOTUBE VIDEO] Button to print Video (Camera Stream).
[![Print Video Button](https://img.youtube.com/vi/ouDR7TC1_uI/0.jpg)](https://www.youtube.com/watch?v=ouDR7TC1_uI "")
##### [YOTUBE VIDEO] Button to print Video (Filtered Images).
[![Print Video Button](https://img.youtube.com/vi/Qq9KgkcM5FU/0.jpg)](https://www.youtube.com/watch?v=Qq9KgkcM5FU "")
