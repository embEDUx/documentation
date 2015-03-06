#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
basepath = os.path.abspath(os.getcwd())
basepath = os.path.join(basepath, 'src')
print(basepath)
projecttile = 'embEDUx'
pages = {}

category_order = [
    'Index',
    'Usage',
    'Setup',
    'Background',
    'Troubleshooting',
    'Support',
    ]
key_order = {
    'front': [ 
        'Overview',
        'Repositories',
        'Adminstation',
        'Buildserver',
        'Workstation',
        'Terminilogy',
        'Requirements',
        'Requirements/',
        'Design/',
        'Eval/',
        'Specs/',
        'Uboot',
        'Toolchain',
        'Linux',
        'Root',
        'Misc',
        'Flashtool',
        ], 
    'back': [ 
        'Customization/',
        'Examples/',
        ],
}


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

    def write_line(entry_list):
        entry_line = '- {}\n'.format(entry_list)
        print('Writing "{}"'.format(entry_line.replace('\n','')))
        target.write(entry_line)


    frontcounter = 0
    middlecounter = 0
    backcounter = 0
    def write_category(category):
        pagelist = pages[category]
        front = len(pagelist)
        back = len(pagelist)
        middle = len(pagelist)

        global frontcounter
        global middlecounter
        global backcounter
        frontcounter = 0
        middlecounter = front
        backcounter = front+middle

        keys = key_order['front'] + key_order['back']

        def mysort(entry):
            global frontcounter
            global middlecounter
            global backcounter
            sort_key = entry[1]
            if len(entry) == 3:
                sort_key = entry[2]
#            print('--- Sorting {}'.format(sort_key))

            def get_key(n, k):
                return '{0:05d}{1}'.format(n, k)

            ordered_key_provided = False
            for k in keys:
                if sort_key.startswith(k):
#                    print('ordered key was provided!')
                    ordered_key_provided = True
                    break

            if ordered_key_provided:
                for n, ordered_key in enumerate(keys):
#                    print('checking against {}'.format(ordered_key))
                    if sort_key.startswith(ordered_key):
                        if ordered_key in key_order['front']:
                            sort_key = get_key(n, sort_key)
#                            print('found front key {}'.format(sort_key))
                            break
                        elif ordered_key in key_order['back']:
                            sort_key = get_key(n+backcounter, sort_key)
#                            print('found back key {}'.format(sort_key))
                            break
                        else:
                            assert(false)
            else:
                sort_key = get_key(middle, sort_key)
                middlecounter += 1
#                print('setting middle key {}'.format(sort_key))
            return sort_key

        pagelist.sort(key=mysort)

        for entry in pagelist:
            write_line(entry)
        del pages[category]


    for category in category_order:
        write_category(category)

    for category in pages.copy().keys():
        write_category(category)

import subprocess
output = subprocess.check_output('mkdocs build --clean', shell=True)
print(output.decode())
