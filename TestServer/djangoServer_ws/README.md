//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                           T E S T       S E R V E R      V2
                           
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Development Web Server using Django technology that allows the user to request an exercise
(Jupyter Notebook) and execute it in a mixed way: combining the local hardware of the client 
(in this case the webcam and the kernel of jupyter) and the Notebook served by this server 
that has been executed on a remote machine.

This v2 of the server establishes the communication with the Notebook Server
directly from the browser via JavaScript, in order to solve NATs and firewalls.

## USAGE:

  1. Go to the main directory:
  `$ cd mysite/`
  
  2. Run the server at all the interfaces, listening in the desired port:
  `$ python manage.py runserver 0.0.0.0:8000`
