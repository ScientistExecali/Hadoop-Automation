#!/usr/bin/python2

import commands as subprocess
import os
import cgi

print("content-type:text/html")
print("\n")

form=cgi.FieldStorage()
ip=form.getvalue('ip')
pw=form.getvalue('pw')

subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} rpm -ivh /root/Software/hadoop-1.2.1-1.x86_64.rpm --force".format(pw,ip))
print("Hadoop installation is complete")
