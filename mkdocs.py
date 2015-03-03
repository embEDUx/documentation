#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
basepath = os.path.abspath(os.getcwd())
basepath = os.path.join(basepath, 'src')
print(basepath)
projecttile = 'embEDUx'
pages = {}

for dirpath, dirnames, filenames in os.walk(basepath):
    to_delete = []
    for d in dirnames:
        if any([
            'site' in d,
            '/.' in d,
            '/img' in d,
            d.startswith('.'),
            ]):
            to_delete.append(d)
    for d in to_delete:
        dirnames.remove(d)
    for f in filenames:
        if f.endswith('.md'):
            title1 = None
            title2 = None
            filename = None
            reldirpath = dirpath.replace(basepath+'/','')
            if reldirpath == basepath:
                filename = f
                title1 = os.path.basename(f).replace('.md','').replace('-', ' ').title()
            else:
                filename = '{}/{}'.format(reldirpath, f)
                title1 = filename.split('/',1)[0].title()
                title2 = filename.split('/',1)[1].replace('.md','').replace('-', ' ').title()
            entry = [filename, title1, title2] 
            if title1 not in pages:
                pages[title1] = []
            if title2 == None:
                del entry[2]
#                entry[2] = 'Overview'
                pages[title1].insert(0, entry)
            elif title1 == title2:
                entry[2] = 'Overview'
                pages[title1].insert(0, entry)
            else:
                pages[title1].append(entry)
            print('Adding {}'.format(entry))

with open('mkdocs.yml', 'w') as target, \
     open('mkdocs_head.yml','r') as head:
    for line in head.readlines():
        target.write(line)

    def write_line(line):
        line = '- {}\n'.format(entry)
        target.write(line)

    write_line(pages['Index'][0])
    del(pages['Index'])

    for category, pagelist in pages.items():
        for entry in pagelist:
            write_line(entry)

import subprocess
output = subprocess.check_output('mkdocs build --clean', shell=True)
print(output.decode())
