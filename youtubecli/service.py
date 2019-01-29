'''
Created on Jan 25, 2019

@author: lihaijun
'''
import logging
from youtubecli.network import Stream

logger = logging.getLogger(__name__)

def default_on_progress(chunk, fh, bytes_remaining):
#    print('bytes_remaining='+str(bytes_remaining))
    fh.write(chunk)
    logger.info('remaining bytes %s', bytes_remaining);
        
def default_on_complete(fh):
    print('download completed at '+str(fh))
    logger.info('download completed at %s', fh);
    
class YoutubeService(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def downloadVideo(self, video, fh, itag = None,on_progress=default_on_progress, on_complete=default_on_complete):
        bytes_remaining = int(video['size']);
        streamUrl = video['url'];
        
        for chunk in Stream(streamUrl).readResponse():
            # reduce the (bytes) remainder by the length of the chunk.
            bytes_remaining -= len(chunk)
            # send to the on_progress callback.
            on_progress(chunk, fh, bytes_remaining)
        on_complete(fh)
        
