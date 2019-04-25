# 2018-tfm-Carlos-Awadallah

# Week 32
Since our Notebooks (both current and potential) have extended functionality through Jupyter extensions and widgets, we have studied the way (in the form of instructions in the DockerFile) to enable this functionality within the container in which the Jupyter server is running.

On the other hand, we have studied the current state of support of the Docker tool for other operating systems, such as Windows or MacOS, since one of the reasons for using these containers is to make the application multiplatform. However, we have found that, for the time being, in the case of Windows OS there is only support for Windows 10 Pro and Windows Enterprise versions, while for MacOS the problem lies in the lack of access to the hardware connected via USB. Therefore, it is still not worth continuing with this line of research, which we will postpone until this situation changes.

# Week 31
This week we launched the third prototype of the mixed execution, with the client side prepared through a docker image that launches everything necessary (including the Jupyter extensions, the OpenCV libraries, the Notebook server, ..) and that provides access to the local hardware. Here is a video-example:

##### [YOUTUBE VIDEO] Mixed Execution Testing with Docker-Based Client side
[![mixed execution docker](https://img.youtube.com/vi/KlgqdIBA4TE/0.jpg)](https://www.youtube.com/watch?v=KlgqdIBA4TE "")

Token access has been removed since the XSRF checking is not needed here: the docker container, once launched by the client, is only accesible from the client's network, so there are not security problems coming from outside. In addition, the potential problems the client (or whatever) could cause would affect only the container, resulting in the client having to re-run the docker, but no further problems (anything involving client's machine).

# Week 30
The network connectivity with the docker has been checked from the host machine, and also the access to the camera through the corresponding flags in the command to launch the docker image, and the OpenCV utilities for accessing the webcam :
```
$ python -c "import cv2;print(cv2.VideoCapture(0).isOpened())"
```
For mixed execution to work, we need to launch a Jupyter server instance from within the docker, but at the same time it must be accessible from the user interface of the host machine (browser). We map the port of the docker in which the server listens to the same port of the machine, in such a way that the client has normal access to it. However, there are some problems of permissions to solve to be able to copy things from the outside to the inside of the docker.

We have also revisited the issue of replacing the token check with the use of cookies. However, the CORS policies do not allow consulting, modifying or obtaining cookies from other domains, for which we are not able to obtain the value of the cookie for the Jupyter server domain. Other ways have been studied, such as including code in the iframe DOM (nor is it allowed).

# Week 29
Once the server is running, the client side will be prepared so that the mixed execution works through the installed docker. The intention is that the students who access the application do not have to install any tool, but will be provided with a simplified docker that will contain everything necessary to face robotic exercises through the web application. Therefore, the docker image will be expanded with OpenCV libraries, jupyter widgets and some extensions necessary for the exercises.

On the other hand, the relevant tests will be carried out with the docker itself to check if there is connectivity with the local webcam, network support and access to the hardware through the USB ports. With this, we can prepare exercises that access the camera or even the interfaces of a customer's robot.

# Week 28
Since mixed technology is already working at this point, it is time to build an instance of the real Unibotics server (a simple development server version) to adapt the code to the application and to the existing database and python classes. This week we will study the technologies used in the server infrastructure, including Docker, templates with JQuery and websockets. It will be tried to lift up a linux virtual environment that allows to install the corresponding versions of all the involved parts so that the server works correctly.
The official docker image will also be installed.

# Week 27
We studied the need to use the Google extension for jupyter and the use of the websockets protocol. In principle, it seems that this does not intervene in the process, and therefore can be discarded, reducing the dependencies that customers must install to access the practices.

On the other hand, and for reasons of security and integrity of the code, we studied the ways of obfuscating and minimizing the new javascript code that intervenes in the communication between browser and Notebook Server. The tool that has been most striking is (https://obfuscator.io/) that allows to act on many parameters that result in a protected code following the most convenient specifications.

# Week 26
Given the problems in the last tests, I have partially changed the focus of the problem: from this point, I will use the client's Browser as an intermediary between the remote Web Server and the client's Notebook Server. Basically, the browser will act as a proxy, forwarding the messages established by the web server as if it was the origin of them. With this, I get through the security mechanisms of the client's machine. However, it has been necessary to make multiple changes to the test server to send all the necessary data to the browser, in addition to using JavaScript for communication.

In this case, both the first test (UC3M -> URJC) and the second (HOME -> URJC) worked as planned. A video example of the second test can be seen here:

##### [YOUTUBE VIDEO] Prototype of Mixed Execution for Unibotics.
[![mixed execution prototype](https://img.youtube.com/vi/IsNA5rBRBsA/0.jpg)](https://www.youtube.com/watch?v=IsNA5rBRBsA "")

# Week 25
Given the success in the test of using different machines with server and client roles, it is time to perform the test by placing the client's machine behind a NAT and a firewall, as would happen in any house of a potential user.
In this case, the requests and commands that the web server sends to the Notebook server had to go through the security mechanisms of the machines in the face of foreign messages. Without demanding to open certain ports for communication (those used by the web server) the test was unsuccessful. I will thoroughly investigate the scenario to situate the error and study possible remedies.

We also studied the code of the Google extension to get ideas. Moreover, we continue looking forward to solve the cookie problem. Ultimately, I made a manual grouping of the back-end files that support the Test Notebook (Color Filter) and I studied minimization tools to lighten the traffic between server and client over the web.

# Week 24
We went to perform the tests on different machines. For this, a first machine has been used to run the web server with Django technology, which will be waiting to receive the request for the ColorFilter exercise that was adapted last week. A second machine will act as a client, where the Jupyter server will be run, which will wait to receive orders from the web server to obtain, execute, modify and re-send the Notebook based on the interaction with the human user. A video example of the two-machine mixed execution is shown on the next video:

##### [YOUTUBE VIDEO] Mixed Execution Testing with Two Machines
[![mixed execution 2 machines](https://img.youtube.com/vi/nGDd6HG124s/0.jpg)](https://www.youtube.com/watch?v=nGDd6HG124s "")

Given that the current option involves sending several code and configuration files that support the exercise, we began to study ways to minimize Python code.


# Week 23
To test the mixed execution implemented, this week has focused on adapting the ColorFilter Notebook to connect to the available webcam and operate normally on the customer's machine. This includes sending the back-end files of the exercise, for which different mechanisms have been studied among which are: take advantage of the REST API with the necessary format, investigate the Python web import mechanisms and also the systems of packaging of files of this language. For now, the best option is to continue with the REST API, although we leave the other options open for later review.

In addition, we have studied the Django sessions and some web mechanisms to replace the token (manual) with the cookie that Jupyter establishes in order to connect to the server, so that later we will substitute the token for that cookie to increase the automation of the process.

# Week 22
We perform a series of tests to verify that the kernel that executes the code is the right one (the one that we started remotely in the client's Notebook Server). We check that by interrupting the kernel in the client, the Notebook code of the test website can no longer be executed. The next test will be already using two different machines.

We also implemented a way to collect the filled Notebook with the code retouched by the user. The test server, when a certain event occurs (according to predictions of whether the client has made a change in the iframe), will request the kernel to send the current version of the Notebook. In addition, when the user clicks on a button to exit the exercise, this latest version will also be requested, and will be stored on the test server.

##### [YOUTUBE VIDEO] Mixed Execution (Remote Web Server + Local Notebook Server + Local Kernel) FIRST VERSION
[![mixed execution 2](https://img.youtube.com/vi/2BqTAunmx30/0.jpg)](https://www.youtube.com/watch?v=2BqTAunmx30 "")

We continue investigating how to use browser cookies. Django [sessions](https://docs.djangoproject.com/en/2.1/topics/http/sessions/) may be necessary.

# Week 21
The next step is to remotely start (via messages from our test web server) a Jupyter session and a kernel associated with the Notebook that has been sent. We use other REST API operations (duly completed), sent to the appropriate routes to start and connect everything.

For debugging purposes and to verify the operation and execution of the code by the kernel that has been launched in the client, we studied the options of embed the Notebook on the web that serves the test server. It may be necessary to re-write the jupyter configuration file, to tweak the security options (XSRF) of the Tornado server on which the Notebooks server is mounted. We focus on using <iframe>.
  
Up to this point, all the agents involved are correctly started, and the kernel seems to be ready to receive execution requests associated with the code of the Notebook from the web.

# Week 20
We have built the first version of the test server through Django. This server simply waits for requests, and when it receives a "start exercise" type request, it simply serves the appropriate Notebook (this time there is only one exercise available) through the REST API, to a kernel that the user must launch (in this case, in a different port).
![TEST SERVER](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/TEST_SERVER.png)
Through the POST operation and establishing the appropriate route, the body of the HTTP message with the correct options and the appropriate security headers (through the token that the Notebook Server establishes to create user sessions), we get the Kernel to receive the Notebook:
![POST](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/POST_REST_API.png)

We have to study the options for the client to request the rest of the code files on which the Notebook depends (back-end of the exercise). We also have to study the possibilities to try to replace the token with the cookies that the Notebook Server establishes in the browser when it is launched.

# Week 19
We started working on a test server. We explore two routes:

- Open the client's docker ports, so that it uses the self-contained docker of Academy (gazebo + gazeo web + notebook server + jupyter kernel). The web server authenticates itself in github and collects the private Notebook with secure copy and copies it to the docker of the machine. This works, but we can not ask users to tweak the status of the ports on their computer.

- Notebook Server + Kernel on the client side. The remote server (web server) puts the notebook in the directory where the Notebook Server is running (local), and then sends orders to it in order to work normal. We need to understand the HTTP API that the Notebook Server uses (in search of an operation that says, for example, take this Notebook). We suspect that we would need HTTP from browser to web server and local WebSockets from the browser to the notebook server.

Since the second option is the most interesting, we studied the [REST API](https://github.com/jupyter/jupyter/wiki/Jupyter-Notebook-Server-API), that contains some operations that can be useful to us.

![REST API](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/REST_API.png)

## Week 18
We finish studying the traces that the source code of Jupyter prints to know what is happening during the establishment of the communication. We also studied the [extension](https://github.com/googlecolab/jupyter_http_over_ws/blob/master/jupyter_http_over_ws/handlers.py) of Colaboratory to embed the HTTP communication in the WebSockets protocol, to later adapt this solution to avoid problems with the users' firewalls, since the jupyter infrastructure allows it to be used to package the ZMQ messages.

We studied the possibility of installing Jupyter from source to change the main files for others with the retouched code to print more traces, and to observe more clearly the steps that are followed. We also started to explore other tools such as the Jupyter REST API.

## Weeks 16 and 17

Now it's time to deepen the distribution of Jupyter through the code files accessible from the browser (session.js and kernel.js mainly) to fully understanding the tools we can use to achieve the objectives of local runtimes for Jupyter Notebooks .

We also used some sniffers to monitor the communication between the Colaboratory server and the browser, and between the last and the local kernel to check how the communication was resolved (involving the HTTP and WebSockets protocols).

I uploaded the resources that the Notebook incorporates to a [Github Pages' repository](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/tree/master/docs) to be able to link them via HTTP with the Notebook, so that they are visible without the end user having to download them. These resources will be moved to the web server when we have built the final version.

## Week 15

We have continued doing research of the colaboratory infrastructure to adapt the exercise Notebook so that it could work normally on the Google server, allowing the visualization loop. In addition, we have rulet out using integrated widgets in the Notebook since Colaboratory does not have support for custom messages, only has certain widgets adapted for machine leraning that do not work for us. The possibility of including buttons in the front-end will be investigated. This is the result of the running Notebook through a mixed connection:
##### [YOUTUBE VIDEO] Mixed Execution (Remote Server + Local Kernel) Through Google Colaboratory
[![mixed execution](https://img.youtube.com/vi/oF6kp_x16M4/0.jpg)](https://www.youtube.com/watch?v=oF6kp_x16M4 "")

We will now focus on the study of the sessions and the kernel that jupyter uses for messaging, to extract the connection information (URL) from a new local kernel and connect to it from the browser.

## Week 14

This week we focused on refining the Notebook to find a solution that allows us to preserve the ability to visualize in an iterative loop and the buttons that allow executing or stopping the code and turn on or off the display of filtered images.
We have studied Colab available widgets: (https://colab.research.google.com/notebooks/widgets.ipynb)
Some changes need to be made to the infrastructure of the exercise.

## Week 13

The first thing we have done is to try to study the Google Colab solution. We have uploaded one of our Notebooks to their server as a test, and we have used the tools they offer to connect to a local execution environment (https://research.google.com/colaboratory/local-runtimes.html)

![local_runtimes](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/local_runtimes_colab.png)

To try to get an idea of its behaviour, I used Wireshark to capture the traffic in my Loopback interface on the port where I had launched the kernel that the Colab server was connected.

![wireshark](https://github.com/RoboticsURJC-students/2018-tfm-Carlos-Awadallah/blob/master/docs/wireshark_localruntimes.png)

I tried to connect the server without having launched the kernel and to kill the kernel while connected with no revealing results: the server just reconnected to a kernel on the reomote server and still working.

At this point, I have thoroughly studied the communication between the Notebook Server and the Jupyter Kernel.

## Week 12

At this point, we need to explore possible ways to make the Notebook, stored on the Academy server (remote), execute the code using the local hardware (Local Jupyter Kernel).
This is possible through local execution environments, such as the [Google Collaborative solution](https://research.google.com/colaboratory/local-runtimes.html). For this, it is necessary to incorporate an extension to the kernel of jupyter, enable it, and replace the ZeroMQ protocol in charge of the communication between Jupyter frontends and kernels by a solution that allows to "deceive" the local browser so that certain things coming from the server are sent to the jupyter local kernel, in such a way that the Notebook Server will connect with the browser and the browser with the jupyter kernel => JdeRobot Colaboratory

In principle, this script should work: (https://www.npmjs.com/package/@jupyterlab/services)
repo: (https://github.com/jupyterlab/jupyterlab/tree/master/packages/services)

The next weeks will be devoted to the investigation of these routes and the search for a possible solution to the problem, to achieve full local execution of the Color Filter Notebook.

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

##### [YOUTUBE VIDEO] Buttons for Play, Pause and Visualization On/Off
[![buttons](https://img.youtube.com/vi/00w6aofU95A/0.jpg)](https://www.youtube.com/watch?v=00w6aofU95A "")

## Week 9

### Visualization Loop
Taking advantage of the infinite loop of the iterative method that executes the algorithm of the students, we have programmed the visualization of the filtered images resulting from the execution of said algorithm in the loop, sampling every certain iterations to print a filtered image in the Notebook every 3 seconds. With this, we extended the set of debugging tools for this exercise:

##### [YOUTUBE VIDEO] Visualization Loop printing filtered images each 3sec
[![visloop](https://img.youtube.com/vi/BBZKI12Hxtg/0.jpg)](https://www.youtube.com/watch?v=BBZKI12Hxtg "")

### Academic Pause
To make it easier for students to complete the task, we have modified the Notebook of this exercise so that it follows a "Live Programming" philosophy, with which students have tools to pause the execution of the code, make changes to their algorithm and rerun their code with the changes made, all without having to restart the kernel or leave the Notebook:

##### [YOUTUBE VIDEO] Academic Pause
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
##### [YOUTUBE VIDEO] Result of the extensions 'Initialization Cells' added to Color Filter Notebook.
[![catmousecompetition](https://img.youtube.com/vi/e2_fgAAeLx4/0.jpg)](https://www.youtube.com/watch?v=e2_fgAAeLx4 "")

## Week 7
On the occasion of the celebration of [IROS2018](https://www.iros2018.org/) in Madrid, and the contribution of JdeRobot to the conference with the [Program-A-Robot-2018](https://jderobot.org/Program-A-Robot-2018) contest, we have made a break to help in the organization and participate in it. During this week I prepared solutions for the two exercises proposed for the contest: 

Cat & Mouse
![catmouse](http://jderobot.org/store/jmplaza/uploads/campeonato-drones/dronecatmouse.jpg)

Escape from the hangar
![hangar](http://jderobot.org/store/jmplaza/uploads/campeonato-drones/hangar.jpg)

### Competition 
##### [YOUTUBE VIDEO] Execution during the competition.
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

##### [YOUTUBE VIDEO] Selectable Source (Camera Stream).
[![Selectable Source](https://img.youtube.com/vi/meVvdFs3Vt0/0.jpg)](https://www.youtube.com/watch?v=meVvdFs3Vt0 "")
##### [YOUTUBE VIDEO] Selectable Source (Output).
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

##### [YOUTUBE VIDEO] Button to print Video (Camera Stream).
[![Print Video Button](https://img.youtube.com/vi/ouDR7TC1_uI/0.jpg)](https://www.youtube.com/watch?v=ouDR7TC1_uI "")
##### [YOUTUBE VIDEO] Button to print Video (Filtered Images).
[![Print Video Button](https://img.youtube.com/vi/Qq9KgkcM5FU/0.jpg)](https://www.youtube.com/watch?v=Qq9KgkcM5FU "")
