import os
import sys
from time import sleep
import html
import numpy
import requests
from youtube_transcript_api import YouTubeTranscriptApi

TOKEN_PATH = [d for d in os.listdir() if "TOKEN_" in d]
if len(TOKEN_PATH) == 0:
    print("You have to create a directory with the name TOKEN_{your token}.\n"
          "Example: TOKEN_IJHEO2J3KjkOEWIJKEKklj323\n")
    sys.exit()

key = TOKEN_PATH[0].replace("TOKEN_", "")

if len(sys.argv) <= 3:
    print("Search youtube videos based on content (captions)")
    print('Usage: python sic.py <"search scope"> <maxresults> <"multiple strings" "like" "this">')
    sys.exit()

q = requests.utils.quote(sys.argv[1])
mr = requests.utils.quote(sys.argv[2])
words = []
for x in range(3, len(sys.argv)):
    words.append(requests.utils.quote(sys.argv[x]))

url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={mr}&order=viewCount&q='\
    '{q}&type=video&videoCaption=closedCaption&key={key}'.format(q=q, mr=mr, key=key)

response = requests.get(url)
json = response.json()
print('Found ' + str(len(json['items'])) + ' videos.')

for i in json['items']:
    found = 0
    sleep(1)
    vid = i['id']['videoId']
    vid_string = html.unescape(i['snippet']['title'])
    ch_string = html.unescape(i['snippet']['channelTitle'])
    try:
        current_caption = YouTubeTranscriptApi.get_transcript(vid)
    except YouTubeTranscriptApi.CouldNotRetrieveTranscript:
        print('No captions for the video: {vid_string} ({vid})'.format(vid_string=vid_string, vid=vid))
        continue;
    for cc in current_caption:
        for word in words:
            if word.lower() in cc['text'].lower():
                found += 1
                print(
                    'Found occurrence for "{word}" at {vid_string} ({vid}) -> '
                    'https://youtu.be/{vid}?t={time}'.format(vid_string=vid_string, word=word,
                                                             vid=vid,
                                                             time=int(numpy.ceil(cc['start'])))
                )
    if not found:
        print('No occurrences found on video {vid_string} by {ch_string} ({i}/{tvid})'.format(ch_string=ch_string,
                                                                                       i=json['items'].index(i) + 1,
                                                                                       tvid=len(json['items']),
                                                                                       vid_string=vid_string))
    else:
        print('Found {found} occurrences at {vid_string} ({vid}) -> '
              'https://youtu.be/{vid}'.format(vid_string=vid_string, found=found,
                                                             vid=vid))
