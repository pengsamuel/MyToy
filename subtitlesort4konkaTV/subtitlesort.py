#coding:gbk

import sys
import re

#从命令行获取要排序的字幕文件
def getcommandlineparam():
  if len(sys.argv) < 2:
    print "用法:subtitle 当前目录下待排序的字幕文件"
  for i in range(1, len(sys.argv)):
    global subtitle
    if i == 1:
      subtitle = sys.argv[i]
    if i == 2:
      #留着以后扩展做字幕时间偏移用
      timeoff = sys.argv[i]

  #print "字幕文件:", subtitle
  #print "时间偏移:", timeoff

#找到时间轴描述行，这行的前一行开始一段字幕
def ismatchtimere(linecount, linecontent):
  #print linecontent
  result = re.match(r'\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d', linecontent)
  if result != None :
    #print 'line of:', linecount, 'is:', linecontent
    return True
  else:
    return False
	
#从时间轴描述行的第一个时间里取出本段字幕的开始时间
def Extracttimenum(stringcontent):
  num = (int(stringcontent[0:2])*3600 + int(stringcontent[3:5])*60 + int(stringcontent[6:8]))*1000 + int(stringcontent[9:12])
  return num
  
#将原字幕段写到目标文件中
def Copyline2newfile(lines, pos):
  pos = pos - 1
  #字幕段结尾的标志是一个空行，其含有仅一个换行符，长度为1
  while len(lines[pos]) > 1:
    outputfile.write(lines[pos])
    pos = pos + 1
  outputfile.write("\n")
  
getcommandlineparam()
print "将对以下字幕文件重排序:" + subtitle
sourcef = file(subtitle, 'r')
iseof = False
linecount = 0
#用来存储(时间值,行号),并用作排序容器
list_linemark = []
while not iseof:
  content = sourcef.readline()
  linecount = linecount+1
  if len(content) == 0:
    iseof = True
  else:
    istimeline = ismatchtimere(linecount, content)
    if istimeline:
      timetick = Extracttimenum(content)
      list_linemark.append((timetick, linecount))
  
#将原字幕读入到列表中
sourcef.seek(0)
sourcelines = sourcef.readlines()
sourcef.close()
#对时间值排序
list_linemark.sort(key=lambda x:x[0])
outputfile = open(subtitle+'_sort', 'w')
print "完成排序的字幕文件:" ,subtitle+'_sort'
for listIndex in range(0, len(list_linemark)):
  startpos = list_linemark[listIndex][1] - 1
  Copyline2newfile(sourcelines, startpos)

outputfile.close()
#print "list line mark as below:"
#for item in list_linemark:
#  print item[1]