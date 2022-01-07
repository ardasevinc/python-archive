#!/usr/bin/env python3

import re
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import numpy as np

text_file = open("yes_gang.txt")
text = text_file.read()
text_file.close()

media_regex_pattern = r"<Media omitted>"
big_pattern = "(\d+\/\d+\/\d+,\s)(\d+:\d+)(\s-\s)(.*?)(:)"
big_regex = re.compile(big_pattern)


msg_count = {}
name1 = ""
for line in text.splitlines():
    match = big_regex.search(line)
    if match is not None:
        name1 = match.group(4)
        if name1 not in msg_count:
            msg_count[name1] = 1
        if name1 in msg_count:
            msg_count[name1] += 1
    if match is None:
        try:
            msg_count[name1] += 1
        except KeyError:
            pass



keys = list(msg_count.keys())
values = list(msg_count.values())

for i in range(len(values)):
    print(keys[i] + ": " + str(values[i]))
