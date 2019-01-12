#!/usr/bin/python36

import subprocess
import os
import cgi

print("content-type:text/html")
print("\n")

form=cgi.FieldStorage()
node=form.getvalue('node')
ip=form.getvalue('ip')
pw=form.getvalue('pw')
mip=form.getvalue('mip')
jip=form.getvalue('jip')

subprocess.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/Config_Files/mapred.xml root@{}:/etc/hadoop/mapred-site.xml".format(pw,ip))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} sed -i 's/#/{}/g' /etc/hadoop/mapred-site.xml".format(pw,ip,jip))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} setenforce 0".format(pw,ip))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} iptables -F".format(pw,ip))

if node=='Master':
	subprocess.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/Config_Files/core.xml root@{}:/etc/hadoop/core-site.xml".format(pw,ip))
	subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} sed -i 's/#/{}/g' /etc/hadoop/core-site.xml".format(pw,ip,mip))
	subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop-daemon.sh start jobtracker".format(pw,ip))
	y=subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} jps".format(pw,ip))
	x=subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop job-list-active-tracker".format(pw,ip))
	print("<pre>")
	print(x)
	print("</pre>")
	if 'JobTracker' in y:
		print("Job tracker started")
	else:
		print("Job tracker failed to start")		

if node=='Slave':
	subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop-daemon.sh start tasktracker".format(pw,ip))
	y=subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} jps".format(pw,ip))
	if 'TaskTracker' in y:
		print("Task tracker started")
	else:
		print("Task tracker failed to start")		

