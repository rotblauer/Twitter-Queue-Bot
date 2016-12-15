#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbapi
import json
import twitter

def tweet(twit):
    tweetToTweet = dbapi.topTweet()
    if not tweetToTweet:
        return

    if tweetToTweet.image != "undefined":

        # # Send images along with your tweets:
        # # - first just read images from the web or from files the regular way:
        with open("path/to/images/" + tweetToTweet.image, "rb") as imagefile:
            imagedata = imagefile.read()
        # - then upload medias one by one on Twitter's dedicated server
        #   and collect each one's id:
        # t_upload = Twitter(domain='upload.twitter.com',
            # auth=OAuth(token, token_secret, consumer_key, consumer_secret))
            id_img1 = twit.media.upload(media=imagedata)["media_id_string"]
        # id_img2 = t_upload.media.upload(media=imagedata)["media_id_string"]
        # - finally send your tweet with the list of media ids:
        # t.statuses.update(status="PTT ★", media_ids=",".join([id_img1, id_img2]))
            return (twit.statuses.update(status=tweetToTweet.content, media_ids=id_img1),
                tweetToTweet)

    # if not tweetToTweet.image:
    return (twit.statuses.update(status=tweetToTweet.content),
            tweetToTweet)


def urlWithEndpoint(endpoint):
    return baseURL + endPoint

def baseURL():
    return "https://api.twitter.com/1.1/"

def oAuthCredentials():
    with open("credentials.json") as credentialsFile:
        return json.loads(credentialsFile.readline())

def authenticate():
    credentials        = oAuthCredentials()
    consumerKey        = credentials["consumer_key"]
    consumerSecret     = credentials["consumer_secret"]
    accessKey          = credentials["access_key"]
    accessSecret       = credentials["access_secret"]

    auth = twitter.OAuth(accessKey, accessSecret, consumerKey, consumerSecret)
    return twitter.Twitter(auth=auth)

if __name__ == "__main__":
    twit = authenticate()
    response, tweeted = tweet(twit)
    if response:
        dbapi.popFirstTweet()
        print("Tweeted: \"" + tweeted.content + "\"")
    else:
        print("Could not send tweet. Will try again tomorrow.")
