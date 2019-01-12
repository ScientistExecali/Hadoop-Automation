# Hadoop-Automation
Provides automation to Hadoop cluster setup

# Getting Started
The prerequisite for running this project is you must have a HTTP server running on your network.

1.Store these files in /var/www/cgi-bin
2.On the browser, type the following into the URL:
            http://localhost/cgi-bin/hadoop_main.py
  You can either type down the IP of the HTTP server or you can write localhost if you're automating the cluster setup from the server.
3.By providing the IP as well as the password to your root account, the cluster can be set up.

# Cluster Setup
1.Install Java on the system which is a part of the cluster.
2.Install Hadoop
3.After installing Java and Hadoop on all the nodes of the cluster, begin the cluster setup by providing the IP addresses of the master and the slaves.
