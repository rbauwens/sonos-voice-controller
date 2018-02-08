#!/usr/bin/python -tt
import os
import requests
import subprocess
import jishi_controller as jishi

def make_request(action, attempt=0):
    pi_url = "http://localhost:5005/"
    address = pi_url + "kitchen" + "/" + action
    #headers.set("Accept", "application/json")
    try:
        response = requests.get(address)    
        return response
    except requests.exceptions.ConnectionError as err:
        print("Error connection to Sonos jishi controller: {}".format(str(err)))
        print("Attempting to start jishi controller on localhost:5005")
        
        up = jishi.start_sonos_controller()
        if up:
            print("Successfully started jishi sonos controller")        
            #re-execute command
            if attempt == 0:
                return make_request(action, 1)

    
        
