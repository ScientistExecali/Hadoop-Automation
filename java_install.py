#!/usr/bin/python2

import commands as subprocess
import os
import cgi

print("content-type:text/html")
print("\n")

form=cgi.FieldStorage()
ip=form.getvalue('ip')
pw=form.getvalue('pw')

#ip=input("ip:");
#pw=input("pw:");

subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} mkdir /root/Software/".format(pw,ip))
subprocess.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/Software/jdk-8u171-linux-x64.rpm root@{}:/root/Software/".format(pw,ip))
subprocess.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/Software/config.py root@{}:/root/Software/".format(pw,ip))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} rpm -ivh /root/Software/jdk-8u171-linux-x64.rpm".format(pw,ip))
subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} python /root/Software/config.py".format(pw,ip))
print("Java installation is complete")

#print("<a href='hadoop_install.py'>Next</a>")
