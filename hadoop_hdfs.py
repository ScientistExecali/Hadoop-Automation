#!/usr/bin/python2

import commands as subprocess
import os
import cgi

print("content-type:text/html")
print("\n")

form=cgi.FieldStorage()
node=form.getvalue('node')
ip=form.getvalue('ip')
pw=form.getvalue('pw')
mip=form.getvalue('mip')
fname=form.getvalue('fname')

subprocess.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/Config_Files/core.xml root@{}:/etc/hadoop/core-site.xml".format(pw,ip))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} sed -i 's/#/{}/g' /etc/hadoop/core-site.xml".format(pw,ip,mip))

if node=='Master':
	subprocess.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/Config_Files/namenode.xml root@{}:/etc/hadoop/hdfs-site.xml".format(pw,ip))

elif node=='Slave':
	subprocess.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/Config_Files/datanode.xml root@{}:/etc/hadoop/hdfs-site.xml".format(pw,ip))

subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} sed -i 's/#/{}/g' /etc/hadoop/hdfs-site.xml".format(pw,ip,fname))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} rm -rfv /{}".format(pw,ip,fname))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} mkdir /{}".format(pw,ip,fname))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} setenforce 0".format(pw,ip))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} iptables -F".format(pw,ip))

if node=='Master':
	subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} 'echo Y|hadoop namenode -format'".format(pw,ip))
	subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop-daemon.sh start namenode".format(pw,ip))
	y=subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} jps".format(pw,ip))
	if 'NameNode' in y:
		print("Namenode started")
	else:
		print("Namenode failed to start")		

elif node=='Slave':
	subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop-daemon.sh start datanode".format(pw,ip))
	y=subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} jps".format(pw,ip))
	if 'DataNode' in y:
		print("Datanode started")
	else:
		print("Datanode failed to start")		

#x=subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} hadoop dfsadmin -report".format(pw,ip))
#print("<pre>")
#print(x)
#print("</pre>")
