#!/usr/bin/python2

import commands as subprocess
import os

print("content-type: text/html")
print("")

print("""
<head>
<title>Hadoop Setup</title>
</head>

<body><center>

<marquee><h1><font color=red>Welcome to the Hadoop Setup</font></h1></marquee>
<table border='3'>

<tr>
<td>Install Java</td>
<td><form action='java_install.py'>
Enter your IP address: <input type='text' name='ip' /></br>
Enter your password: <input type='password' name='pw' /></br>
<input type='submit' />
</form></td>
</tr>

<tr>
<td>Install Hadoop</td>
<td><form action='hadoop_install.py'>
Enter your IP address: <input type='text' name='ip' /></br>
Enter your password: <input type='password' name='pw' /></br>
<input type='submit' />
</form></td>
</tr>

<tr>
<td>Setup HDFS Cluster</td>
<td><a href='../hadoop.html'>Enter HDFS Setup Menu</a></td>
</tr>

<tr>
<td>Setup MR Cluster</td>
<td><a href='../mapreduce.html'>Enter MR Setup Menu</a></td>
</tr>

<tr>
<td>Uninstall Hadoop</td>
<td><a href='hadoop_uninstall.py'>Click here to uninstall</a></td>
</tr>
""")

