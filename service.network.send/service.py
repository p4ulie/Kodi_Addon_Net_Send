# -*- coding: utf-8 -*-
import json
import time
import datetime
import xbmc
import xbmcgui
import xbmcaddon
import requests

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

class Settings_Monitor(xbmc.Monitor):
    def __init__(self, player):
        self.player = player

    def onSettingsChanged(self):
        self.player.update_settings()

class Player_Monitor(xbmc.Player):
    def __init__(self):
        self.update_settings()
        self.playing_movie = None
        self.playing_tv_show = None
        self.playing_other = None

    def send_command_on(self, event):

        xbmc.log("%s: Toggle Group 01: %s" % (addonname, self.enabled_group_01_toggle), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Toggle Group 02: %s" % (addonname, self.enabled_group_02_toggle), level=xbmc.LOGDEBUG)
        xbmc.log("%s: HTTP Method 01: %s" % (addonname, self.http_method_01), level=xbmc.LOGDEBUG)
        xbmc.log("%s: HTTP Method 02: %s" % (addonname, self.http_method_02), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Toggle Movies: %s" % (addonname, self.active_for_movies_toggle), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Toggle TV Shows: %s" % (addonname, self.active_for_tvshows_toggle), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Toggle Other: %s" % (addonname, self.active_for_other_toggle), level=xbmc.LOGDEBUG)

        if (self.active_for_movies_toggle == "true" and self.playing_movie)\
        or (self.active_for_tvshows_toggle == "true" and self.playing_tv_show)\
        or (self.active_for_other_toggle == "true" and self.playing_other):

            now = time.strptime(datetime.datetime.now().strftime("%H:%M"), "%H:%M")

            if (self.active_time_from < now) or (self.active_time_to > now):


                if self.enabled_group_01_toggle == "true":
                    if self.url_list_01 != "":
                        url_list = self.url_list_01.split(';')
                        for url in url_list:
                            xbmc.log("%s: Group 01, sending %s %s to %s" % (addonname, self.http_method_01, self.command_on_01, url),
                                     level=xbmc.LOGDEBUG)
                            if self.http_method_01 == "GET":
                                r = requests.get(url, data=self.command_on_01)
                            if self.http_method_01 == "POST":
                                r = requests.post(url, data=self.command_on_01)
                            if self.http_method_01 == "PUT":
                                r = requests.put(url, data=self.command_on_01)

                if self.enabled_group_02_toggle == "true":
                    if self.url_list_02 != "":
                        url_list = self.url_list_02.split(';')
                        for url in url_list:
                            xbmc.log("%s: Group 02, sending %s %s to %s" % (addonname, self.http_method_02, self.command_on_02, url),
                                     level=xbmc.LOGDEBUG)
                            if self.http_method_02 == "GET":
                                r = requests.get(url, data=self.command_on_02)
                            if self.http_method_02 == "POST":
                                r = requests.post(url, data=self.command_on_02)
                            if self.http_method_02 == "PUT":
                                r = requests.put(url, data=self.command_on_02)

                if self.enabled_group_03_toggle == "true":
                    if self.url_list_03 != "":
                        url_list = self.url_list_03.split(';')
                        for url in url_list:
                            xbmc.log("%s: Group 03, sending %s %s to %s" % (addonname, self.http_method_03, self.command_on_03, url),
                                     level=xbmc.LOGDEBUG)
                            if self.http_method_03 == "GET":
                                r = requests.get(url, data=self.command_on_03)
                            if self.http_method_03 == "POST":
                                r = requests.post(url, data=self.command_on_03)
                            if self.http_method_03 == "PUT":
                                r = requests.put(url, data=self.command_on_03)


    def send_command_off(self, event):

        xbmc.log("%s: Media type - playing movie: %s" % (addonname, self.playing_movie), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Media type - playing TV show: %s" % (addonname, self.playing_tv_show), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Media type - playing other: %s" % (addonname, self.playing_other), level=xbmc.LOGDEBUG)

        if (self.active_for_movies_toggle == "true" and self.playing_movie)\
        or (self.active_for_tvshows_toggle == "true" and self.playing_tv_show)\
        or (self.active_for_other_toggle == "true" and self.playing_other):

            now = time.strptime(datetime.datetime.now().strftime("%H:%M"), "%H:%M")

            if (self.active_time_from < now) or (self.active_time_to > now):

                if self.enabled_group_01_toggle == "true":
                    if self.url_list_01 != "":
                        url_list = self.url_list_01.split(';')
                        for url in url_list:
                            xbmc.log("%s: Group 01, sending %s %s to %s" % (addonname, self.http_method_01, self.command_off_01, url),
                                     level=xbmc.LOGDEBUG)
                            if self.http_method_01 == "GET":
                                r = requests.get(url, data=self.command_off_01)
                            if self.http_method_01 == "POST":
                                r = requests.post(url, data=self.command_off_01)
                            if self.http_method_01 == "PUT":
                                r = requests.put(url, data=self.command_off_01)

                if self.enabled_group_02_toggle == "true":
                    if self.url_list_02 != "":
                        url_list = self.url_list_02.split(';')
                        for url in url_list:
                            xbmc.log("%s: Group 02, sending %s %s to %s" % (addonname, self.http_method_02, self.command_off_02, url),
                                     level=xbmc.LOGDEBUG)
                            if self.http_method_02 == "GET":
                                r = requests.get(url, data=self.command_off_02)
                            if self.http_method_02 == "POST":
                                r = requests.post(url, data=self.command_off_02)
                            if self.http_method_02 == "PUT":
                                r = requests.put(url, data=self.command_off_02)

                if self.enabled_group_03_toggle == "true":
                    if self.url_list_03 != "":
                        url_list = self.url_list_03.split(';')
                        for url in url_list:
                            xbmc.log("%s: Group 03, sending %s %s to %s" % (addonname, self.http_method_03, self.command_off_03, url),
                                     level=xbmc.LOGDEBUG)
                            if self.http_method_03 == "GET":
                                r = requests.get(url, data=self.command_off_03)
                            if self.http_method_03 == "POST":
                                r = requests.post(url, data=self.command_off_03)
                            if self.http_method_03 == "PUT":
                                r = requests.put(url, data=self.command_off_03)


    def onPlayBackStarted(self):
        # turn light switch off

        xbmc.log("NetSend addon - Playback started at %s" % time.time(), level=xbmc.LOGDEBUG)

        if self.enabled_global_toggle == "true" and self.active_on_play_toggle == "true":
            self.now_playing()
            self.send_command_off(event="Start")

    def onPlayBackStopped(self):
        # turn light switch on

        xbmc.log("NetSend addon - Playback stopped at %s" % time.time(), level=xbmc.LOGDEBUG)

        if self.enabled_global_toggle == "true" and self.active_on_stop_toggle == "true":
            self.send_command_on(event="Stop")

    def onPlayBackEnded(self):
        # turn light switch on

        xbmc.log("NetSend addon - Playback ended at %s" % time.time(), level=xbmc.LOGDEBUG)

        if self.enabled_global_toggle == "true" and self.active_on_end_toggle == "true":
            self.send_command_on(event="End")

    def onPlayBackPaused(self):
        # turn light switch on

        xbmc.log("NetSend addon - Playback paused at %s" % time.time(), level=xbmc.LOGDEBUG)

        if self.enabled_global_toggle == "true" and self.active_on_pause_toggle == "true":
            self.now_playing()
            self.send_command_on(event="Pause")

    def onPlayBackResumed(self):
        # turn light switch off

        xbmc.log("NetSend addon - Playback resumed at %s" % time.time(), level=xbmc.LOGDEBUG)

        if self.enabled_global_toggle == "true" and self.active_on_resume_toggle == "true":
            self.now_playing()
            self.send_command_off(event="Resume")

    def now_playing(self):
        # check media type when a video starts, pauses, or resumes
        query = {'jsonrpc': '2.0', 'method': 'Player.GetItem', 'params': { 'properties': ['showtitle', 'season', 'episode', 'duration', 'streamdetails'], 'playerid': 1 }, 'id': 'VideoGetItem'}
        response_json = xbmc.executeJSONRPC(json.dumps(query))
        response = json.loads(response_json)

        xbmc.log("%s: Media info: %s" % (addonname, response_json), level=xbmc.LOGDEBUG)

        if response['result']['item']['type'] == 'movie':
            self.playing_movie = True
            self.playing_tv_show = False
            self.playing_other = False
            xbmc.log("%s: Media type set - playing movie: %s" % (addonname, self.playing_movie), level=xbmc.LOGDEBUG)
        elif response['result']['item']['type'] == 'episode':
            self.playing_movie = False
            self.playing_tv_show = True
            self.playing_other = False
            xbmc.log("%s: Media type set - playing TV show: %s" % (addonname, self.playing_tv_show),
                     level=xbmc.LOGDEBUG)
        else:
            self.playing_movie = False
            self.playing_tv_show = False
            self.playing_other = True
            xbmc.log("%s: Media type set - playing other: %s" % (addonname, self.playing_other), level=xbmc.LOGDEBUG)

    def update_settings(self):
        # update variables
        xbmc.log("%s: Settings updated." % (addonname), level=xbmc.LOGDEBUG)
        self.enabled_global_toggle = addon.getSetting('enabledGlobal_toggle')
        self.active_for_movies_toggle = addon.getSetting('activeForMovies_toggle')
        self.active_for_tvshows_toggle = addon.getSetting('activeForTVshows_toggle')
        self.active_for_other_toggle = addon.getSetting('activeForOther_toggle')

        self.active_on_play_toggle = addon.getSetting('activeOnPlay_toggle')
        self.active_on_pause_toggle = addon.getSetting('activeOnPause_toggle')
        self.active_on_resume_toggle = addon.getSetting('activeOnResume_toggle')
        self.active_on_stop_toggle = addon.getSetting('activeOnStop_toggle')
        self.active_on_end_toggle = addon.getSetting('activeOnEnd_toggle')

        self.active_time_from = time.strptime(addon.getSetting('activeTimeFrom'), "%H:%M")
        self.active_time_to = time.strptime(addon.getSetting('activeTimeTo'), "%H:%M")

        self.enabled_group_01_toggle = addon.getSetting('enabledGroup01_toggle')
        self.url_list_01 = addon.getSetting('urlList10')
        self.http_method_01 = addon.getSetting('httpMethod10')
        self.command_on_01 = addon.getSetting('command10On')
        self.command_off_01 = addon.getSetting('command10Off')

        self.enabled_group_02_toggle = addon.getSetting('enabledGroup02_toggle')
        self.url_list_02 = addon.getSetting('urlList20')
        self.http_method_02 = addon.getSetting('httpMethod20')
        self.command_on_02 = addon.getSetting('command20On')
        self.command_off_02 = addon.getSetting('command20Off')

        self.enabled_group_03_toggle = addon.getSetting('enabledGroup03_toggle')
        self.url_list_03 = addon.getSetting('urlList30')
        self.http_method_03 = addon.getSetting('httpMethod30')
        self.command_on_03 = addon.getSetting('command30On')
        self.command_off_03 = addon.getSetting('command30Off')

        xbmc.log("%s: Toggle Group 01: %s" % (addonname, self.enabled_group_01_toggle), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Toggle Group 02: %s" % (addonname, self.enabled_group_02_toggle), level=xbmc.LOGDEBUG)
        xbmc.log("%s: HTTP Method 01: %s" % (addonname, self.http_method_01), level=xbmc.LOGDEBUG)
        xbmc.log("%s: HTTP Method 02: %s" % (addonname, self.http_method_02), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Toggle Movies: %s" % (addonname, self.active_for_movies_toggle), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Toggle TV Shows: %s" % (addonname, self.active_for_tvshows_toggle), level=xbmc.LOGDEBUG)
        xbmc.log("%s: Toggle Other: %s" % (addonname, self.active_for_other_toggle), level=xbmc.LOGDEBUG)


def main():

    player = Player_Monitor()
    settings = Settings_Monitor(player)
    monitor = xbmc.Monitor()

    xbmc.log("%s: Starting" % (addonname), level=xbmc.LOGNOTICE)

    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            # Abort was requested while waiting. We should exit
            break
        # xbmc.log("NetSend addon periodic notice at %s" % time.time(), level=xbmc.LOGDEBUG)

    xbmc.log("%s: Ending" % (addonname), level=xbmc.LOGNOTICE)

if __name__ == '__main__':

    xbmc.log("%s: Initialized" % (addonname, ), level=xbmc.LOGNOTICE)

    main()
