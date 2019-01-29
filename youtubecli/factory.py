'''
Created on Jan 23, 2019

@author: lihaijun
'''
from youtubecli.network import Html
from youtubecli.network import Header
from bs4 import BeautifulSoup
from urllib.parse import parse_qsl
from urllib.parse import unquote
import re
import json

REGEX_WATCH_ID = re.compile(r'(?:v=)([0-9A-Za-z_-]{11}).*', 0)
REGEX_PLAYER_CONFIG = re.compile(r';ytplayer\.config\s*=\s*({.*?});')

class WatchPageFactory(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def createWatchPage(self, url):
        watch_id = REGEX_WATCH_ID.search(url).group(1);
        
        html = Html(url).readResponse();
        soup = BeautifulSoup(html, features="html.parser")
        
        player_config_args = json.loads(REGEX_PLAYER_CONFIG.search(html).group(1))['args']
        
        stream_videos = []
        for i in player_config_args['url_encoded_fmt_stream_map'].split(','):
            video_config = {k: unquote(v) for k, v in parse_qsl(i)}
            video = dict((k, video_config[k]) for k in ('itag', 'quality', 'url', 'type'))
            video['size'] = Header(video.get('url')).readResponse()['content-length']
            stream_videos.append(video)
        
        return {'url':url, 'watch_id':watch_id, 'watch_title':soup.title.string, 'stream_videos':stream_videos}
