#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import base64

from instabot_py import InstaBot

bot = InstaBot(
    login="between_boundaries",
    password=base64.b64decode(b'cmVnaVNwZWs3').decode('utf-8'),
    like_per_day=200,
    comments_per_day=300,
    tag_list=['naturephotography','urbanphotography','scuba'],
    tag_blacklist=['nsfw'], 
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=150,
    follow_time=1 * 60,
    unfollow_per_day=300,
    unlike_per_day=0,
    unfollow_recent_feed=True,
    # If True, the bot will also unfollow people who dont follow you using the recent feed. Default: True
    time_till_unlike=3 * 24 * 60 * 60,  # 3 days
    unfollow_break_min=15,
    unfollow_break_max=30,
    user_max_follow=0,
    # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
    user_min_follow=0,
    log_mod=0,
    proxy="",
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["Wow, amazing shot!","So beautiful! ❤️","🔥 🔥 🔥","Epic!!","Such a great snap!","Amazing!!","So jealous of this shot 😀","Great snap 👍","Yaaaaaassss 👌"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[],
    unfollow_whitelist=[])

bot.mainloop()
