"""Description:
The script deals with the upload of the manipulated images to the web server with the help of the Python requests module. 
"""

#!/usr/bin/env python3
import requests
import os,sys

url = "[linux-instance-IP-Address]/upload/"

path = "/home/user-instance/supplier-data/images/"
pic_dir = os.listdir(path)

for pic in pic_dir:
    if '.jpeg' in pic:
        with open(path + pic, 'rb') as opened:
            r = requests.post(url, files={'file': opened})