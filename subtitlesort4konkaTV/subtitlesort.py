#coding:gbk

import sys
import re

#�������л�ȡҪ�������Ļ�ļ�
def getcommandlineparam():
  if len(sys.argv) < 2:
    print "�÷�:subtitle ��ǰĿ¼�´��������Ļ�ļ�"
  for i in range(1, len(sys.argv)):
    global subtitle
    if i == 1:
      subtitle = sys.argv[i]
    if i == 2:
      #�����Ժ���չ����Ļʱ��ƫ����
      timeoff = sys.argv[i]

  #print "��Ļ�ļ�:", subtitle
  #print "ʱ��ƫ��:", timeoff

#�ҵ�ʱ���������У����е�ǰһ�п�ʼһ����Ļ
def ismatchtimere(linecount, linecontent):
  #print linecontent
  result = re.match(r'\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d', linecontent)
  if result != None :
    #print 'line of:', linecount, 'is:', linecontent
    return True
  else:
    return False
	
#��ʱ���������еĵ�һ��ʱ����ȡ��������Ļ�Ŀ�ʼʱ��
def Extracttimenum(stringcontent):
  num = (int(stringcontent[0:2])*3600 + int(stringcontent[3:5])*60 + int(stringcontent[6:8]))*1000 + int(stringcontent[9:12])
  return num
  
#��ԭ��Ļ��д��Ŀ���ļ���
def Copyline2newfile(lines, pos):
  pos = pos - 1
  #��Ļ�ν�β�ı�־��һ�����У��京�н�һ�����з�������Ϊ1
  while len(lines[pos]) > 1:
    outputfile.write(lines[pos])
    pos = pos + 1
  outputfile.write("\n")
  
getcommandlineparam()
print "����������Ļ�ļ�������:" + subtitle
sourcef = file(subtitle, 'r')
iseof = False
linecount = 0
#�����洢(ʱ��ֵ,�к�),��������������
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
  
#��ԭ��Ļ���뵽�б���
sourcef.seek(0)
sourcelines = sourcef.readlines()
sourcef.close()
#��ʱ��ֵ����
list_linemark.sort(key=lambda x:x[0])
outputfile = open(subtitle+'_sort', 'w')
print "����������Ļ�ļ�:" ,subtitle+'_sort'
for listIndex in range(0, len(list_linemark)):
  startpos = list_linemark[listIndex][1] - 1
  Copyline2newfile(sourcelines, startpos)

outputfile.close()
#print "list line mark as below:"
#for item in list_linemark:
#  print item[1]