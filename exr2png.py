import os
import time
from sys import argv

path = argv[1]

if os.path.isfile(path):
    command = 'H:/repositories/mitsuba0.5-original/build/binaries/MinSizeRel/mtsutil.exe -q tonemap -g 2.2 ' + path
    print(command)
    os.system(command)

elif os.path.isdir(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if '.exr' in name:
                file_name = os.path.join(root, name)
                command = 'H:/repositories/mitsuba0.5-original/build/binaries/MinSizeRel/mtsutil.exe -q tonemap -g 2.2 ' + file_name
                print(command)
                os.system(command)

os.system('del mitsuba.DESKTOP-*.log')
print('done.')
time.sleep(1)