#!/usr/bin/python -tt
import os
import subprocess
import requests
import time
            
def is_jishi_up():
    try: 
        r = requests.head("http://localhost:5005")
        return r.status_code == 200
    except requests.exceptions.ConnectionError:
        return False
    
    
def start_sonos_controller():
    jishi_up = is_jishi_up()
    try:
        os.chdir("/home/pi/sonos/jishi-node-sonos-http-api-0d03be9")
        p = subprocess.Popen(["npm", "start"])
        count = 0
        while (jishi_up == False and count < 10):
            jishi_up = is_jishi_up()
            time.sleep(2)
            count = count + 1
        if jishi_up:
            return True
        return False
    except Exception as err:
        print("Failed to start sonos controller: " + str(err))
        
