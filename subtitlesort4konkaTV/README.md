# subtitlesort4konkaTV
家里的康佳电视，播放usb电影的字幕比较傻：
1. 只识别ansi编码格式的中文
2. 字幕小段必须按时间顺序排列，否则出现插入过的小段后，其后的字幕不显示。

用pathon写了个小工具期望解决上述问题，让我好好看一遍“神探夏洛克2015”


to be continue:
1. ansi & utf-8 编码
2. lambda 与python的排序
3. achieve time offset feature
4. regulation expresstion


windows7 默认的编码(ansi,意为使用系统默认编码方式)为GBK编码
BOM-- binary order maker，FFFE在文件头标识大端或小端字节序
utf--unicode transform format ,是unicode编码在传输中使用的表达方式
unicode--universal character set,分两种ucs2,ucs4分别代表2字节和4字节编码格式
