#!/usr/bin/env python3
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

x = 1
viewcount = ""
channelId = ""
maxresults = 50

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if "--viewcount" in arg:
            viewcount = '&order=viewCount'
            sys.argv.pop(sys.argv.index(arg))
            continue
        if "--channel" in arg:
            channelId = ('&channelId=' + sys.argv[sys.argv.index(arg) + 1]) if len(sys.argv) >= x + 1 else ""
            sys.argv.pop(sys.argv.index(arg) + 1)
            sys.argv.pop(sys.argv.index(arg))
            continue
        if "--maxresults" in arg:
            maxresults = sys.argv[sys.argv.index(arg) + 1] if len(sys.argv) >= x + 1 else 50
            sys.argv.pop(sys.argv.index(arg) + 1)
            sys.argv.pop(sys.argv.index(arg))

        continue

if len(sys.argv) < 3:
    print("Search youtube videos based on content (captions)")
    print(
        'Usage: python sic.py [--maxresults <maxresults>] [--viewcount] [--channel <channelId>]'
        ' <"search scope"> <"multiple strings" "like" "this">')
    print('--viewcount sorts results by view count.')
    print('--maxresults sets total results to search into (default: 50)')
    print('--channel sets a channel id to search from (e.g.: UCcefcZRL2oaA_uBNeo5UOWg)')
    sys.exit()

q = ("&q=" + requests.utils.quote(sys.argv[1])) if requests.utils.quote(sys.argv[1]) else ""
mr = maxresults
words = []
for z in range(2, len(sys.argv)):
    words.append(sys.argv[z])

videos = ""

if not channelId:

    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={mr}{viewcount}{channelId}' \
          '{q}&type=video&videoCaption=closedCaption&key={key}'.format(q=q, mr=mr, key=key, viewcount=viewcount,
                                                                       channelId=channelId)
else:
    r = requests.get(
        "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channelId}&key={key}".format(
            channelId=channelId.replace("&channelId=", ""), key=key))
    plist = r.json()
    videos = None
    if len(plist.get('items', [])) > 0:
        videos = plist["items"][0].get('contentDetails', {}).get('relatedPlaylists', {}).get('uploads', "")
    if not videos:
        print("Invalid Channel")
        sys.exit()
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&' \
          'maxResults=50&playlistId={plist}&key={key}'.format(key=key, plist=videos)

print(url)

response = requests.get(url)
json = response.json()
pages = [json]

# if we provide channel id, we'll support more than 50 results by getting next page
if channelId:
    next_page = json.get('nextPageToken', False)
    while next_page:
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&' \
              'maxResults=50&playlistId={plist}&key={key}&pageToken={next_page}'.format(key=key, plist=videos, next_page=next_page)
        print(url)
        response = requests.get(url)
        json = response.json()
        pages.append(json)
        next_page = json.get('nextPageToken', False)

    for j in pages:
        # this filters out items not containing any of the search words in their titles
        if q:
            j["items"] = [x for x in j["items"] if len([y for y in sys.argv[1].split(" ") if y in x["snippet"]["title"]]) > 0]

for json in pages:
    print('Found ' + str(len(json['items'])) + ' videos.')
    for i in json.get('items', {}):
        found = 0
        sleep(1)
        vid = i['id']['videoId'] if not channelId else i["snippet"]["resourceId"]["videoId"]
        vid_string = html.unescape(i['snippet']['title'])
        ch_string = html.unescape(i['snippet']['channelTitle'])
        try:
            current_caption = YouTubeTranscriptApi.get_transcript(vid)
        except YouTubeTranscriptApi.CouldNotRetrieveTranscript:
            print('No captions for the video: {vid_string} ({vid})'.format(vid_string=vid_string, vid=vid))
            continue
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
                                                                                                  i=json['items'].index(
                                                                                                      i) + 1,
                                                                                                  tvid=len(json['items']),
                                                                                                  vid_string=vid_string))
        else:
            print('Found {found} occurrences at {vid_string} ({vid}) -> '
                  'https://youtu.be/{vid}'.format(vid_string=vid_string, found=found,
                                                  vid=vid))
