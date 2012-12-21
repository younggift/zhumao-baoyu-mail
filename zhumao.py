#! /usr/bin/python
# -*- coding: utf-8 -*-

# zhumao，邮件发送者
__usage__ = "usage: %zhumao.py [--help]"
__version__ = "zhumao by Young 2012-12-21"

from optparse import OptionParser
import smtplib
import quopri
import time
import sys

# 命令行解析
p = OptionParser(usage=__usage__, version=__version__, description=__doc__)  
p.add_option("-F", "--file", dest="filename",
                  help="file need to be sent", metavar="FILE", default="test.in")
p.add_option("-S", "--smtp", dest="smtp",
                  help="smtp server", metavar="SMTP_SERVER", default="smtp.nenu.edu.cn")
p.add_option("-f", "--from", dest="fromaddr",
                  help="mail sender", metavar="FROM")
p.add_option("-p", "--password", dest="password",
                  help="password", metavar="PASSWORD")
p.add_option("-t", "--to", dest="to",
                  help="mail receiver", metavar="TO")
p.add_option("-s", "--size", dest="size",
                  help="size of each mail", metavar="SIZE", default=100)
p.add_option("-L", "--subject", dest="subject_prefix",
                  help="the prefix of mail subject", metavar="subject_prefix", default='zhumao_baoyu_mail')

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
# 标记
    sleep = 0.1
    subject = opt.subject_prefix + ' ' +str(i/opt.size)+'/'+str(end/opt.size)
    to = opt.to
    user = opt.fromaddr
    pwd = opt.password
    smtp = opt.smtp
    header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:' + subject +' \n'
    print
    print header
    smtpserver = smtplib.SMTP(smtp)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(user, pwd)
    msg = header + current
    smtpserver.sendmail(user, to, msg)
    print   'sent.'
    smtpserver.close()
    time.sleep(sleep)
#发送



## sys.stdout.write(current)


