#! /usr/bin/python
# -*- coding: utf-8 -*-

# baoyu, 邮件接收者
__usage__ = "usage: %baoyu.py [--help]"
__version__ = "baoyu by Young 2012-12-21"

from optparse import OptionParser
import base64
import time
import sys
import poplib
import time
from email.Parser import Parser
from email.header import decode_header

######
# helpers
######
def getheader(header_text, default="ascii"):
    """Decode the specified header"""
    try:
        headers = decode_header(header_text)
        header_sections = [unicode(text, charset or default)
                           for text, charset in headers]
        return u"".join(header_sections)
    except:
        return u"".join("invalidated encode")

def get_msg(which):
    return "\n".join(server.top(which, 1)[1])

def get_from(msg):
    email = parser.parsestr(msg)
    return email.get("From")

def get_body(which):
    msg = "\n".join(server.retr(which)[1])
    email = parser.parsestr(msg)
    return email.get("BODY_START")

def get_subject(msg):
    return getheader(parser.parsestr(msg).get("Subject"))

# e.g. [base64-2] 1/2 
def get_cur_num(subject, subject_prefix):
    start = subject.find(opt.subject_prefix)+len(opt.subject_prefix)
    slash = subject.find('/', start)
    return int(subject[start:slash])

def get_all_num(subject, subject_prefix):
    start = subject.find(opt.subject_prefix)+len(opt.subject_prefix)
    slash = subject.find('/', start)
    return int(subject[slash+1:])


#--------------------------------------------------------------------
# 命令行解析
p = OptionParser(usage=__usage__, version=__version__, description=__doc__)  
p.add_option("-F", "--file", dest="filename",
             help="file need to be saved", metavar="FILE", 
             default="test.out")
p.add_option("-P", "--pop", dest="pop",
             help="pop3 server", metavar="POP3_SERVER", 
             default="pop3.nenu.edu.cn")
p.add_option("-u", "--user", dest="user",
             help="user name", metavar="USER")
p.add_option("-p", "--password", dest="password",
             help="password", metavar="PASSWORD")
p.add_option("-f", "--from", dest="fromaddr",
             help="from whom to be filtered", metavar="FROM",
             default='gift.young.1@gmail.com' )
p.add_option("-L", "--subject", dest="subject_prefix",
             help="the prefix of mail subject as filter", metavar="subject_prefix",
             default='[zhumao_baoyu_mail]')

(opt, args) = p.parse_args()

#  检查, 根据标记过滤
#  下载并删除
#  接收百分比
parser = Parser()
server = poplib.POP3(opt.pop)
server.user(opt.user)
server.pass_(opt.password)
server.set_debuglevel(0)
sleep = 0.1
count = server.stat()[0]
d = dict()
for i in xrange(1, count, 1):
    current = get_msg(i)
    if (get_from(current).find(opt.fromaddr) != -1 and 
        get_subject(current).find(opt.subject_prefix) != -1):
        b = get_body(i)
        print '+-------------------------'
        print '|' + str(i)+' '+ get_subject(current)
        # print '|' + b
        print '+-------------------------'
        current_seq = get_cur_num(get_subject(current), opt.subject_prefix)
        all_number  = get_all_num(get_subject(current), opt.subject_prefix)
        print (str(current_seq) +'/'+ str(all_number))
        d [current_seq] = b
        if len(d) >= all_number :
            break
        # time.sleep(sleep)
    else:
        print 'filtered out: '+str(i)+'/'+str(count)+' '+get_subject(current)

server.quit()

#  合并文件
s=""
for k in xrange(1, all_number+1, 1):
    print "LEN:"+str(len(d[k]))
    s += d[k]

#  解码文件
s = base64.standard_b64decode(s)

file = open (opt.filename, "w")
file.write(s)
