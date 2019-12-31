import time, os, sys, smtplib, thread, subprocess, glob
from os import path
#print("\033c")

i = 1
oioioi = os.path.dirname(os.path.abspath(__file__))+"/writings/"
checki = time.strftime("%Y-%m-%d")+"-reflexoes-" + str(i) + "o-pomodoro-"
filename = time.strftime("%Y-%m-%d")+"-reflexoes-" + str(i) + "o-pomodoro-"+ ".txt"
adeus = glob.glob(oioioi+checki+ '**')
if path.exists("/Applications/WriteRoom.app"):
    application = "/Applications/WriteRoom.app"
else:
    application = "/Applications/TextEdit.app"

print 'cheguei aqui'

if not path.exists(oioioi):
    print 'the folder does not exist: creating new folder /writings/'
    os.mkdir(oioioi)

if not adeus:
    print 'cheguei aqui 2'
    print '['+'\033[91m\33[1m'+'-'+'\33[0m'+'] - File does not exist'
    f = open(os.path.expanduser(oioioi+filename), "w")
    print 'cheguei aqui 3'
    print '[*] - Creating file: ' + filename
    f.close()
    print '['+'\033[32m\33[1m'+'+'+'\33[0m'+'] - File created successfully'
    bash_command1 = "open  -a "+application+" "+oioioi+filename
    print '[*] - Opening File ...'
    subprocess.call(bash_command1,shell=True)
    bash_command2 = "osascript self-c.applescript 30"
    print '[*] - Closing Down the Internet... See you in 30 minutes'
    subprocess.call(bash_command2,shell=True)
else:
    #Tenho mesmo de ver esta parte muito melhor, mas ja da para perceber
    while len(glob.glob(oioioi+time.strftime("%Y-%m-%d")+"-reflexoes-" + str(i) + "o-pomodoro-"+ '**')) != 0:
        print '['+'\033[91m\33[1m'+'-'+'\33[0m'+'] - File '+str(i)+' already existed'
        i += 1
        filename = time.strftime("%Y-%m-%d")+"-reflexoes-" + str(i) + "o-pomodoro-"+ ".txt"
        print '['+'\033[91m\33[1m'+'-'+'\33[0m'+'] - Creating new file with index - '+str(i)
    f = open(os.path.expanduser(oioioi+filename), "w")
    print '[*] - Creating file: ' + filename
    f.close()
    print '['+'\033[32m\33[1m'+'+'+'\33[0m'+'] - File created successfully'
    bash_command1 = "open  -a "+application+" "+oioioi+filename
    print '[*] - Opening File ...'
    subprocess.call(bash_command1,shell=True)
    if path.exists("/Applications/WriteRoom.app") and path.exists(os.path.dirname(os.path.abspath(__file__))+"/self-c.applescript"):
        bash_command2 = "osascript self-c.applescript 30"
        print '[*] - Closing Down the Internet... See you in 30 minutes'
        subprocess.call(bash_command2,shell=True)
