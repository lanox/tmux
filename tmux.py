#!/usr/bin/env python

import os
import random
import subprocess

gen_name_random = [
    "admiring",
    "adoring",
    "albattani",
    "agitated",
    "amazing",
    "angry",
    "awesome",
    "backstabbing",
    "berserk",
    "big",
    "boring",
    "clever",
    "cocky",
    "compassionate",
    "condescending",
    "cranky",
    "desperate",
    "determined",
    "distracted",
    "dreamy",
    "drunk",
    "ecstatic",
    "elated",
    "elegant",
    "evil",
    "fervent",
    "focused",
    "furious",
    "gigantic",
    "gloomy",
    "goofy",
    "grave",
    "happy",
    "high",
    "hopeful",
    "hungry",
    "insane",
    "jolly",
    "jovial",
    "kickass",
    "lonely",
    "loving",
    "mad",
    "modest",
    "naughty",
    "nauseous",
    "nostalgic",
    "pedantic",
    "pensive",
    "prickly",
    "reverent",
    "romantic",
    "sad",
    "serene",
    "sharp",
    "sick",
    "silly",
    "sleepy",
    "small",
    "stoic",
    "stupefied",
    "suspicious",
    "tender",
    "thirsty",
    "tiny",
    "trusting"
]
assign_random_name = (random.choice(gen_name_random))
attached_session = ['tmux', 'list-sessions', '-F', '#{session_attached}']
new_session = 'tmux new -s %s' % assign_random_name
reattach_session = 'tmux attach'

get_session_number = subprocess.Popen(attached_session, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
store_session_number = get_session_number.stdout.read().strip().decode("utf-8")

if store_session_number == "1":
    os.system(new_session)
elif store_session_number == "0":
    os.system(reattach_session)
else:
    os.system(new_session)
