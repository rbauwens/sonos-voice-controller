#!/usr/bin/python -tt
import sonos

sonos_class = sonos.Sonos()
#sonos_class.class_test()
current_track = sonos_class.getCurrentTrack()
print("current_track: ", current_track)

next_track = sonos_class.getNextTrack()
print("next_track: ", next_track)

#rc = sonos_class.pause()
#print("pause status:", rc)

#rc = sonos_class.play()
#print("play status: ", rc)

#rc = sonos_class.togglePlayPause()
#print("togglePlayPause status: ", rc)

#rc = sonos_class.nextTrack()
#print("nextTrack status: ", rc)

#rc = sonos_class.previousTrack()
#print("previousTrack status: ", rc)

#volume = sonos_class.getCurrentVolume()
#print("getCurrentVolume: ", volume)

#rc = sonos_class.volumeUp()
#print("volumeUp status: ", rc)

#rc = sonos_class.volumeDown()
#print("volumeDown status: ", rc)
