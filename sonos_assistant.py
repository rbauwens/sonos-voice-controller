#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import subprocess
import sys
import sonos
import jishi_controller

import aiy.assistant.auth_helpers
import aiy.audio
import aiy.voicehat
from google.assistant.library import Assistant
from google.assistant.library.event import EventType

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def say_whats_playing():
    sonos_class = sonos.Sonos()
    current_track = sonos_class.get_current_track()
    print("current_track: ", current_track)
    aiy.audio.say('Sonos is currently playing %s' % current_track)

def play_next():
    sonos_class = sonos.Sonos()
    rc = sonos_class.next_track()
    if rc:
        aiy.audio.say('Playing next track')
    else:
        aiy.audio.say('''I can't do that right now''')

def pause():
    sonos_class = sonos.Sonos()
    rc = sonos_class.pause()
    if rc:
        aiy.audio.say('Paused')
    else:
        aiy.audio.say('Unable to pause')

def play():
    sonos_class = sonos.Sonos()
    rc = sonos_class.play()
    if rc:
        aiy.audio.say('Playing')
    else:
        aiy.audio.say('''I can't do that right now''')

def process_event(assistant, event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        if text == 'power off':
            assistant.stop_conversation()
            power_off_pi()
        elif text == '''what's playing''':
            assistant.stop_conversation()
            say_whats_playing()
        elif text == 'skip this song':
            assistant.stop_conversation()
            play_next()
        elif text == 'pause sonos':
            assistant.stop_conversation()
            pause()
        elif text == 'play sonos':
            assistant.stop_conversation()
            play()

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    jishi_controller.start_sonos_controller()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()
