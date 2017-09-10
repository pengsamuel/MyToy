#!/usr/bin/python

# -*- coding:utf-8 -*-  

import shutil
import time

#此脚本文件需以UTF-8格式编码
src = "D:\\WeGame\\rail_apps\\饥荒：单机版\\rail_user_data\\2000013\\76561197980970883\\cloud_storage\\user_space\\2199037600743130074"

dst = "D:\\WeGame\\rail_apps\\饥荒：单机版\\rail_user_data\\2000013\\76561197980970883\\cloud_storage\\user_space\\2199037600743130074_save_"

print '##################################################################'
print '##################   SAVE Don Starv   ############################'
print '##################################################################'
#加上时间值作为后缀
strtime = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))

#必须转换成内部编码格式
usrc = unicode(src, 'utf-8')
udst = unicode(dst+strtime, 'utf-8')

#拷贝目录
shutil.copytree(usrc, udst, False)


print '##################################################################'
print '##################   SAVE Don Starv End   ########################'
print '##################################################################'