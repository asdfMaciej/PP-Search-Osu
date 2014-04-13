# -*- coding: utf-8 -*-
import sys

try:
    pp_minimum, pp_maximum = float(sys.argv[1]), float(sys.argv[2])
except IndexError:
    sys.exit("[!] Error - put in 2 parameters!")

glorious_pp_list = open('osupp.txt', 'r')
beatmaps = []

for line in glorious_pp_list.readlines():

    line = line.replace('\n', '')
    try:
        pp, index, name = line.split(';')
        beatmaps.append((float(pp), int(index), name))
    except ValueError:
        pass

glorious_pp_list.close()

actual_question = "Do you want to save to file and open it? (Y/N): "
question_file = raw_input(actual_question).lower() == 'y'

if question_file:
    file_write = open('beatmaps_list.txt', 'w+')

for pp, index, name in beatmaps:
    continue_search = (pp >= pp_minimum) and (pp <= pp_maximum)
    result = '['+str(pp)+' PP] '+name+': http://osu.ppy.sh/b/'+str(index)
    # i put it there because pep8 said line was too long

    if continue_search:
        keywords = ('tv', 'hard', 'short')
        continue_search = False

        for word in keywords:
            if word in name.lower():
                continue_search = True

        if continue_search:
            print result

            if question_file:
                file_write.write(result+'\n')

if question_file:
    file_write.close()
    __import__('subprocess').call("beatmaps_list.txt", shell=True)

### Osu PączkoPaczka [PP] by maciej01
### Usage: pp.py <minimum pp> <maximum pp>
### Place osupp.txt in the same directory as script from this pastebin:
### http://pastebin.com/xCeZevW5
### Just remove the first line, and you're good to go.
