Please follow the following guide to make the application running.

Operating System: Independent
Programming Language - Python2.7
Python packages - flask, cheetah

You can install the python package on the ubuntu by the following command
on the terminal 
$ sudo pip install cheetah
$ sudo pip install flask

If you do not have pip installed, please install it by the following command
$ sudo apt-get install python-pip

Copy the package to the directory.
Make sure, you have an active internet connection.
On the terminal type:
$ export PYTHONPATH=/path/to/parent/directory

You can run the application by
$./addressbook.py

Now Open the browser and navigate to http://0.0.0.0:8008. Make sure that no other application is running on port 8008.

#################################
####### Additional Notes  #######
#################################

1. The database used is MySQL. Make sure that you have installed it on your system
2. The AddressBook.sql file located in AddressBook/db_files can be used to create the database 
   and preload the records into the system.
3. The MySQL configuration like the ip, port, username and password can be updated by changing the 
   values in AddressBook/config/constants.py