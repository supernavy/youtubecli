'''
Created on Jan 20, 2019

@author: lihaijun
'''

import argparse
import os
import sys
from youtubecli.factory import WatchPageFactory
from youtubecli.service import YoutubeService

def main():
    parser = argparse.ArgumentParser(description='Execute command with Youtube CLI')
    parser.add_argument('url', help='The YouTube /watch url', nargs='?')
    parser.add_argument(
        '-p', '--prefix', default='video', help=(
            'The prefix of file'
        ),
    )
    parser.add_argument(
        '-d', '--dir', default=os.getcwd(), help=(
            'The direction of downloaded file'
        ),
    )
    
    args = parser.parse_args()
    if not args.url:
        parser.print_help()
        sys.exit(1)
    print(args)
    watchPage = WatchPageFactory().createWatchPage(args.url)
    filename = args.prefix+'.'+watchPage['stream_videos'][0]['type'].split(';')[0].split('/')[1]
    fp = os.path.join(args.dir, filename)
    fh = open(fp, 'wb')
    YoutubeService().downloadVideo(watchPage['stream_videos'][0], fh)
    
if __name__ == '__main__':
    main()
    