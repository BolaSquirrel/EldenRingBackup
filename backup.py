import shutil
from datetime import datetime
from time import sleep

settings = open('settings.txt','r')
x = 0
for s in settings:
    if x == 0:
        saves = s.split(';')[1].strip('\n').strip(' ')
    if x == 1:
        backups = s.split(';')[1].strip('\n').strip(' ')
    x += 1

while True:
    datetime = datetime.now()
    filepath = '/EldenRing(' + str(datetime.year) + '-' + str(datetime.month) + '-' + str(datetime.day) + '-hour' + str(datetime.hour)  + ')'
    shutil.copytree(saves,backups + filepath)
    sleep(3600)