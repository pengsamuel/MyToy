#!/usr/bin/python

# -*- coding:utf-8 -*-  

import shutil
import os

path = "D:\\WeGame\\rail_apps\\饥荒：单机版\\rail_user_data\\2000013\\76561197980970883\\cloud_storage\\user_space\\"
upath = unicode(path, 'utf-8')

sortlist = os.listdir(upath)
sortlist.sort()

print '##################################################################'
print '##################   LOAD Don Starv   ############################'
print '##################################################################'

print "will rm dir:"+sortlist[0]
shutil.rmtree(upath+sortlist[0]) 

print "copy data from:"+sortlist[-1]
shutil.copytree(upath+sortlist[-1], upath+sortlist[0], False)


print '##################################################################'
print '##################   LOAD Don Starv End   ########################'
print '##################################################################'

