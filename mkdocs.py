#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
basepath = os.path.abspath(os.getcwd())
projecttitle = 'embEDUx'
pages = []

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
        if '.md' in f:
            title1 = None
            title2 = None
            filename = None
            reldirpath = dirpath.replace(basepath+'/','')
            if reldirpath == basepath:
                filename = f
                title1 = os.path.basename(f).replace('.md','').replace('-', ' ').title()
            else:
                filename = '{}/{}'.format(reldirpath, f)
                title1 = reldirpath.title().title()
                title2 = os.path.basename(f).replace('.md','').replace('-', ' ').title()
            entry = [filename, title1, title2] 
            if entry[0].startswith('home.md'):
                entry[2] = 'Introduction'
                pages.insert(0, entry)
            elif entry[0].startswith('home'):
                pages.insert(1, entry)
            else:
                pages.append(entry)

with open('mkdocs.yml', 'w') as target, \
     open('mkdocs_head.yml','r') as head:
    for line in head.readlines():
        target.write(line)

    for entry in pages:
        line = '- {}\n'.format(entry)
        target.write(line)

import subprocess
output = subprocess.check_output('mkdocs build --clean', shell=True)
print(output.decode())
