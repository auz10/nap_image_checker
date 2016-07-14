#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import imghdr

disallowed_chars = ['$', '£', '*', '&', '%', ' ', '[', ']', '@', '€', '^', '+', '(', ')',
                    '`', '/', ':', ';', '|', '}', '{']
skip_files = ['Thumbs.db', '.DS_Store']
allowed_types = ['jpg', 'jpeg', 'png', 'gif']

os.system('cls' if os.name == 'nt' else 'clear')
print "\033[4m\033[1m IMAGE CHECKING TOOL \033[0m\n"
fails = 0
for root, dir, files in os.walk(os.path.dirname('.', topdown=False):
    for name in files:
        if name not in skip_files:
            fail = False
            for each_letter in list(name):
                if each_letter in disallowed_chars:
                    print '\033[1m' + name + "\033[0m |\033[91m INVALID CHARS ("+each_letter+")\033[0m"
                    fail = True
                    fails += 1

            if (os.path.getsize(os.path.join(root, name)) / 1048576) > 2:
                print '\033[1m' + name + "\033[0m |\033[93m LARGE FILE \033[0m"
                fail = True
                fails += 1

            if imghdr.what(os.path.join(root, name)) not in allowed_types:
                print '\033[1m' + name + "\033[0m |\033[91m INVALID FILE TYPE \033[0m"
                fail = True
                fails += 1

            if fail == False: 
                print name  + " |\033[92m PASSED \033[0m"

text_color = "\033[92m" if fails <= 0 else "\033[91m"

print "\n" + text_color + str(fails) + " FILES FAILED! \033[0m"