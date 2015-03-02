#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
basepath = os.path.abspath(os.getcwd())
projecttitle = u'embEDUx'
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
            title = None
            filename = None
            reldirpath = dirpath.replace(basepath+'/','')
            if reldirpath == basepath:
                filename = f
                title = projecttitle
            else:
                filename = u'{}/{}'.format(reldirpath, f)
                title = reldirpath
            entry = [filename, title]
            pages.append(entry)

with open('mkdocs.yml', 'w') as target, \
     open('mkdocs_head.yml','r') as head:
    for line in head.readlines():
        target.write(line)


#    target.writelines(head.readlines()[0:-1])
    for entry in pages:
        line = u'- {}\n'.format(entry)
        target.write(line)

import subprocess
output = subprocess.check_output('mkdocs build --clean', shell=True)
print(output)
