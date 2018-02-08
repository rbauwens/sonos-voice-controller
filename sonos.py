#!/usr/bin/python -tt
import requests
import request_base
import datetime


class Sonos:

    #private static final Logger LOGGER = Logger.getLogger( Adapter.class.getName() );
    def class_test(self):
        print("I found the class")
    
    def getCurrentTrack(self):
        response = request_base.make_request("state")
        
        if response.json():
            jsonObject = response.json()
            if "currentTrack" in jsonObject:
                currentTrackJson = jsonObject["currentTrack"]
                title = currentTrackJson["title"]
                artist = currentTrackJson["artist"]
                return title + " - " + artist
            
        return "No Current Track Found"

    def getNextTrack(self):
        response = request_base.make_request("state")
        if response.json():
            jsonObject = response.json()
            if "nextTrack" in jsonObject:
                nextTrackJson = jsonObject["nextTrack"]
                title = nextTrackJson["title"]
                artist = nextTrackJson["artist"]
                return title + " - " + artist
            return "No Next Track Found"
        return "No Next Track Found"
    

    """
    def getFavorites():
        response = request_base.make_request("favorites")
        
        ArrayList<String> favorites = new ArrayList<>()
        if response.json():
            String responseBody = response.json()
            if (responseBody.contains("[") && responseBody.contains("]")) {
                if (responseBody.length() == 2)
                {
                    return favorites;
                }

                String[] parts1 = responseBody.split("\\[");
                String[] parts2 = parts1[1].split("\\]");

                if (parts2[0].contains(",")) {
                    String[] parts3 = parts2[0].split("\\,");
                    for (String s : parts3) {
                        favorites.add(s.substring(1, s.length() - 1));
                    }
                }
                else { //only one favorite
                    favorites.add(parts2[0].substring(1, parts2[0].length() - 1));
                }
            }
            return favorites;
        }
        return favorites;
    """

    def playFavorite(self, favorite):
        action = "favorite/" + favorite
        response = request_base.make_request(action)
        statusCode = response.status_code
        return statusCode == 200

    def pause(self):
        #LOGGER.log( Level.INFO, "Pause")
        statusCode = 0
        try:
            response = request_base.make_request("pause")
            statusCode = response.status_code
        except Error:
            print("Pause threw an Exception: " + Error)
        
        return statusCode == 200

    def play(self):
        #LOGGER.log( Level.INFO, "Play")
        status_code = 0
        response = request_base.make_request("play")
        status_code = response.status_code
        
        return status_code == 200

    def togglePlayPause(self):
        statusCode = 0
        try:
            response = request_base.make_request("playpause")
            statusCode = response.status_code
        except Error:
            print("Play/Pause threw an Exception: " + Error)
        
        return statusCode == 200
   
    def nextTrack(self):
        response = request_base.make_request("next")
        statusCode = response.status_code
        return statusCode == 200
    
    def previousTrack(self):
        response = request_base.make_request("previous")
        statusCode = response.status_code
        return statusCode == 200
    
    def getCurrentVolume(self):
        response = request_base.make_request("state")
        return response.json()["volume"]
    
    def volumeUp(self):
        response = request_base.make_request("volume/+3")
        statusCode = response.status_code
        return statusCode == 200

    def volumeDown(self):
        response = request_base.make_request("volume/-3")
        statusCode = response.status_code
        return statusCode == 200
    
