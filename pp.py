# -*- coding: utf-8 -*-
import sys


pp_minimum, pp_maximum = float(sys.argv[1]), float(sys.argv[2])
glorious_pp_list = open('osupp.txt', 'r')
beatmaps = []

for line in glorious_pp_list.readlines():
    #pp, index, name = line.replace('\n','').split(';')
    line = line.replace('\n', '')
    try:
        pp, index, name = line.split(';')
        beatmaps.append((float(pp), float(index), name))
    except ValueError:
        pass

glorious_pp_list.close()

for pp, index, name in beatmaps:
    continue_search = (pp >= pp_minimum) and (pp <= pp_maximum)

    if continue_search:
        keywords = ('tv', 'hard', 'short')
        continue_search = False

        for word in keywords:
            if word in name.lower():
                continue_search = True

        if continue_search:
            print '['+str(pp)+' PP] '+name+': http://osu.ppy.sh/s/'+str(index)

### Osu PączkoPaczka [PP] by maciej01
### Usage: pp.py <minimum pp> <maximum pp>
### Place osupp.txt in the same direction as script from this pastebin:
### http://pastebin.com/xCeZevW5
### Just remove the first line, and you're good to go.
