import sys
import time
import paramiko 
import cmd
import datetime
import os,datetime,shutil,socket 

today = datetime.date.today()
todaystr = today.isoformat()
now = time.localtime()

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 

cur_time= "%04d%02d%02d_%02d%02d%02d"%(now.tm_year, now.tm_mon, now.tm_mday,
                                       now.tm_hour, now.tm_min, now.tm_sec)

# Create Directory 
# backup_dir : Backup log Directroy 
# home_dir : Backup img Directory 

backup_dir = ("C:\L3_SW_Img\Cisco3560_Backup_img_log" + '_' + todaystr)
home_dir = ("C:\L3_SW_Img\Cisco3560_Backup_img" + '_' + todaystr) 
            
if not os.path.isdir(home_dir):
    os.makedirs(home_dir)
    print("Cisco3560_Backup Img Directory %s was created." %home_dir)

if not os.path.isdir(backup_dir):
    os.makedirs(backup_dir)
    print("Cisco3560_Img Log  Directory %s was created." %backup_dir)

source_folder = ('C:\TFTP-Root')
source_folder_1 = ('C:\Python27\CiscoSW_SSH')
dest_folder = home_dir
dest_folder_1 = backup_dir

# backup_log = open('Backup_img_log' + cur_time + '.txt' ,'a')

#print ("Backup_img_log %s was created." %backup_log)
#print "\n*************************" + "Backup_Config_" + cur_time + " Start " + " *************************\n"

#authentication
USER = 'administrator'
PASSWORD = 'entAro'
secret = 'entAroEN'

s = open('cisco_hosts1.txt')
for ip in s.readlines():
    ip = ip.strip()
    if ip != "" and ip == "10.40.1.6":
        try:          
            #ssh session starts
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, username=USER, password=PASSWORD)
            
            backup_log = open('Backup_log_' + cur_time + '.txt' ,'a')            
            now = time.localtime()
            cur_time_1= "%04d-%02d-%02d %02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday,
                                                    now.tm_hour, now.tm_min, now.tm_sec)
            
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
            
            #copying SW_IOS to tftp
            chan.send('copy flash: tftp\n')
            time.sleep(1)
            chan.send('c3560-ipbasek9-mz.122-55.SE7\n')
            #chan.send('c3560-ipbasek9-mz.122-55.SE11.bin\n')
            time.sleep(1)
            chan.send('172.20.120.117\n')   
            chan.send(IPAddr)
            chan.send('\n')
            time.sleep(1)
            chan.send('\n')
            time.sleep(100)

            client.close()

            print ("\n" + cur_time_1 + " Cisco_3560 Img Backup for " + ip + " successfully!!!!")
            backup_log.write("\n" + cur_time_1 + " Cisco_3560 Img Backup done for " + ip + " successfully!!!!")

        except:
            
            now = time.localtime()
            cur_time_1= "%04d-%02d-%02d %02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday,
                                                    now.tm_hour, now.tm_min, now.tm_sec)

            backup_log = open('Backup_log_' + cur_time + '.txt' ,'a')   
            
            print ("\n" + cur_time_1 + " Cisco_3560 Img Backup for " + ip + " Failure!!!!")
            backup_log.write("\n" + cur_time_1 + " Cisco_3560 Img Backup done for " + ip + " Failure!!!!")
            
    elif ip != "" and ip == "10.40.1.9":
        try:          
            #ssh session starts
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, username=USER, password=PASSWORD)
            
            backup_log = open('Backup_log_' + cur_time + '.txt' ,'a')            
            now = time.localtime()
            cur_time_1= "%04d-%02d-%02d %02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday,
                                                    now.tm_hour, now.tm_min, now.tm_sec)
            
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
            
            #copying SW_IOS to tftp
            chan.send('copy flash: tftp\n')
            time.sleep(1)
            chan.send('c3560-ipbasek9-mz.122-55.SE7.bin\n')
            time.sleep(1)
            #chan.send('172.20.120.117\n')   
            chan.send(IPAddr)
            chan.send('\n')
            time.sleep(1)
            chan.send('\n')
            time.sleep(100)

            client.close()

            print ("\n" + cur_time_1 + " Cisco_3560 Img Backup for " + ip + " successfully!!!!")
            backup_log.write("\n" + cur_time_1 + " Cisco_3560 Img Backup done for " + ip + " successfully!!!!")

        except:
            
            now = time.localtime()
            cur_time_1= "%04d-%02d-%02d %02d:%02d:%02d"%(now.tm_year, now.tm_mon, now.tm_mday,
                                                    now.tm_hour, now.tm_min, now.tm_sec)

            backup_log = open('Backup_log_' + cur_time + '.txt' ,'a')   
            
            print ("\n" + cur_time_1 + " Cisco_3560 Img Backup for " + ip + " Failure!!!!")
            backup_log.write("\n" + cur_time_1 + " Cisco_3560 Img Backup done for " + ip + " Failure!!!!")        
    

#    print ip
    s.close()
    backup_log.close()
        
time.sleep(10)
files = os.listdir(source_folder)

for f in files:
    shutil.move(source_folder+'\\'+f,dest_folder)

files_1 = os.listdir(source_folder_1)

for p in files_1:
    if  p.startswith("Backup_log"):
        shutil.move(source_folder_1+'\\'+p,dest_folder_1)

    








