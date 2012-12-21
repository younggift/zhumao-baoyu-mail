#! /usr/bin/python
# -*- coding: utf-8 -*-

# zhumao，邮件发送者
__usage__ = "usage: %zhumao.py [--help] | -file <filename> -from <user@library.nenu.edu.cn> -to <user@jlu.ciac.cn>"
__version__ = "zhumao by Young 2012-12-21"

from optparse import OptionParser
import smtplib
import quopri
import sys

# 命令行解析
p = OptionParser(usage=__usage__, version=__version__, description=__doc__)  
p.add_option("-F", "--file", dest="filename",
                  help="file need to be sent", metavar="FILE", default="test.in")
p.add_option("-f", "--from", dest="from",
                  help="mail sender", metavar="FROM")
p.add_option("-t", "--to", dest="to",
                  help="mail receiver", metavar="TO")
p.add_option("-s", "--size", dest="size",
                  help="size of each mail", metavar="SIZE", default=20)

(opt, args) = p.parse_args()

# 输入文件
file = open (opt.filename, "r")
s = file.read()

# 编码文件
s = quopri.encodestring(s, 1)
## sys.stdout.write(s)

# 折分文件
end = len(s)
for i in xrange(0, end, opt.size):
    current = s[i:i+opt.size]
    sys.stdout.write(current)

# 标记，发送

