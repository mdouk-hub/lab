# !/usr/bin/python

import os

with open('sortie','w') as sortie:
    for root, dirs, files in os.walk(".", topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))
        for name in files:
            print(name)
            with open(name) as fich:
                lines = fich.readlines()
                for line in lines:
                    if line[:4] == 'URL=':
                        sortie.write(line.split('=')[-1])
