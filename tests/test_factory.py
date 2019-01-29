import unittest
import json
import os
from youtubecli.factory import WatchPageFactory
from youtubecli.service import YoutubeService
 
 
class FactoryTest(unittest.TestCase):
    def test_create_watch_page(self):
        watchPage = WatchPageFactory().createWatchPage("https://www.youtube.com/watch?v=YOCYvBuX1XY")
        print(json.dumps(watchPage))
    
    def test_youtube_service(self):
        watchPage = WatchPageFactory().createWatchPage("https://www.youtube.com/watch?v=y5wo6_cBw_0")
        filename = 'test.'+watchPage['stream_videos'][0]['type'].split(';')[0].split('/')[1]
        fp = os.path.join(os.getcwd(), filename)
        fh = open(fp, 'wb')
        YoutubeService().downloadVideo(watchPage['stream_videos'][0], fh)
    