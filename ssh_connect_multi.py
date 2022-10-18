import sys
import time
import paramiko 
import os
import cmd
import datetime
import os,datetime,shutil

today = datetime.date.today()
todaystr = today.isoformat()
new_todaystr = str(todaystr)

#Create Backup Folder(C:\Config\Config_Backup)
home_dir = ("C:\Config\Config_Backup" + '_' + todaystr) 
            
if not os.path.isdir(home_dir):
    os.makedirs(home_dir)
    print("Home directory %s was created." %home_dir)

source_folder = ('C:\TFTP-Root')
dest_folder = home_dir

#authentication
#HOST = '172.20.120.17' 
USER = 'administrator'
PASSWORD = 'entAro'
secret = 'entAroEN'

#Open file cisco_host.txt
#Read IP address 
f = open('cisco_hosts.txt')
for ip in f.readlines():
	ip = ip.strip()

#ssh session starts
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, username=USER, password=PASSWORD)

#ssh shell
chan = client.invoke_shell()
time.sleep(1)
#enter enable secret
chan.send('en\n')
chan.send(secret +'\n')
time.sleep(1)
#terminal lenght for no paging 
chan.send('term len 0\n')
time.sleep(1)

#show SW_config and write output
chan.send('copy running-config tftp://172.20.120.34\n')
time.sleep(1)
chan.send('\n')
time.sleep(1)
chan.send('\n')
time.sleep(1)

#Move files in C:\TFTP-Root\\ to C:\Config\Config_Backup
files = os.listdir(source_folder)

for f in files:
    shutil.move(source_folder+'\\'+f,dest_folder)

client.close()

#print ip
#f.close()
