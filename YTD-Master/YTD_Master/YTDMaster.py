""""
Author : Soumil shah
Email : soushah@my.bridgeport.edu
Version 1.0.1
"""
from apiclient.discovery import build
import pandas as pd

class YoutubeVideo(object):
    def __init__(self, api_key='YOUR KEY', channel_id='UC_eOodxvwS_H7x2uLQa-svw'):
        self.api_key = api_key
        self.channel_id= channel_id
        self.temp = []
        self.data = self.__validate()
        self.__base_url = "https://www.youtube.com/watch?v="

    def __validate(self):
        try:
            self.youtube = build('youtube', 'v3', developerKey=self.api_key)
            self.videos = self.__generator()
            return self.videos
        except:
            print("API Key or Channel ID was incorrect ")

    def __generator(self):

        # get Uploads playlist id
        res = self.youtube.channels().list(id=self.channel_id,
                                           part='contentDetails').execute()
        playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Blank Videos
        next_page_token = None

        while True:
            res = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                    part='snippet',
                                                    maxResults=50,
                                                    pageToken=next_page_token).execute()

            self.temp += res['items']
            next_page_token = res.get('nextPageToken')

            if next_page_token is None:
                break

        return self.temp

    @property
    def get_title(self):
        return [x['snippet']['title'] for x in self.data]

    @property
    def get_video_url(self):
        return [self.__base_url + x['snippet']['resourceId']['videoId'] for x in self.data]

    @property
    def get_image(self):
        return [self.__base_url+x['snippet']['thumbnails']['medium']['url'] for x in self.data]

    @property
    def get_all(self):
        get_title = self.get_title
        link = self.get_video_url
        image = self.get_image
        return [y for y in zip(get_title,link,image)]

    @property
    def save_excel(self):
        get_title = self.get_title
        link = self.get_video_url
        image = self.get_image
        self.df = pd.DataFrame({"Title":get_title,
                                "link":link,
                                "Image":image})
        self.df.to_excel("Youtube.xlsx")
        print("Report Created ")
        return True

    @property
    def save_json(self):
        get_title = self.get_title
        link = self.get_video_url
        image = self.get_image
        self.df = pd.DataFrame({"Title":get_title,
                                "link":link,
                                "Image":image})
        self.df.to_json("Youtube.json")
        print("Report Created ")






