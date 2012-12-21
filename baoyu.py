#! /usr/bin/python
# -*- coding: utf-8 -*-

# baoyu, 邮件接收者
__usage__ = "usage: %baoyu.py [--help]"
__version__ = "baoyu by Young 2012-12-21"

from optparse import OptionParser
import quopri
import time
import sys
import poplib
import time
from email.Parser import Parser
from email.header import decode_header

def getheader(header_text, default="ascii"):
    """Decode the specified header"""
    headers = decode_header(header_text)
    header_sections = [unicode(text, charset or default)
                       for text, charset in headers]
    return u"".join(header_sections)

######
# helpers
######

def get_date(which):
    msg = "\n".join(server.retr(which)[1])
    email = parser.parsestr(msg)
    return email.get("Date")

# return subject of message with id 'which'
def get_subject(which):
    msg = "\n".join(server.retr(which)[1])
#    email = parser.parsestr(msg)
#    return email.get("Subject")
    return getheader(parser.parsestr(msg).get("Subject"))



# 命令行解析
p = OptionParser(usage=__usage__, version=__version__, description=__doc__)  
p.add_option("-F", "--file", dest="filename",
                  help="file need to be saved", metavar="FILE", default="test.out")
p.add_option("-P", "--pop", dest="pop",
                  help="pop3 server", metavar="POP3_SERVER", default="pop3.nenu.edu.cn")
p.add_option("-u", "--user", dest="user",
                  help="user name", metavar="USER")
p.add_option("-p", "--password", dest="password",
                  help="password", metavar="PASSWORD")
p.add_option("-L", "--subject", dest="subject_prefix",
                  help="the prefix of mail subject as filter", metavar="subject_prefix", default='zhumao_baoyu_mail')

(opt, args) = p.parse_args()

#  检查, 根据标记过滤
parser = Parser()
server = poplib.POP3_SSL(opt.pop)
server.user(opt.user)
server.pass_(opt.password)
server.set_debuglevel(0)

count = server.stat()[0]
# for i in xrange(count, 1, -1):
#     print get_date(i)
#     print str(i)+' '+ get_subject(i)

retri = 1
print str(retri)+' '+ get_subject(retri)
print str(retri)+' '+ get_date(retri)
#  
#  下载并删除
#  合并文件
#  解码文件
#  接收百分比

