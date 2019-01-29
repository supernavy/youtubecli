'''
Created on Jan 24, 2019

@author: lihaijun
'''
from urllib.request import urlopen

class Stream(object):
    '''
    classdocs
    '''
    def __init__(self, url,chunk_size=8 * 1024):
        '''
        Constructor
        '''
        self.url = url
        self.chunk_size = chunk_size
        
    def readResponse(self):
        """Read the response in chunks."""
        response = urlopen(self.url)
        while True:
            buf = response.read(self.chunk_size)
            if not buf:
                break
            yield buf
            
class Html(object):
    '''
    Html
    '''
    def __init__(self, url):
        self.url = url;
        
    def readResponse(self):
        response = urlopen(self.url)
        return response.read().decode('utf-8')
    
class Header(object):
    def __init__(self, url):
        self.url = url
        
    def readResponse(self):
        response = urlopen(self.url)
        return {k.lower(): v for k, v in response.info().items()}