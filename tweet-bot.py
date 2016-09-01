#!/usr/bin/env python2

from twitter import *
from slacker import Slacker
#== For output of all tweet objects in JSON
# import json
# from pygments import highlight, lexers, formatters
#==

slack = Slacker('xoxb-')
config = {}
execfile("config", config)
twitter = Twitter(
        auth = OAuth(config["access_token_key"], config["access_token_secret"], config["consumer_key"], config["consumer_secret"]))
user = ""
results = twitter.statuses.user_timeline(screen_name = user,count=1)
#== For output of all tweet objects in JSON
# formatted_json = json.dumps(results, indent=4, sort_keys=True)
# colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
# print(colorful_json)
#==

for obj in results:
    oid = obj["id"]
tweeturl = "https://twitter.com/" + str(user) + "/status/" + str(oid)

smessage = tweeturl

slack.chat.post_message('#some-slack-room', smessage, as_user=True)