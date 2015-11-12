import urllib2

# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()

from urllib2 import *
from cookielib import *


cookie = CookieJar()

handler=HTTPCookieProcessor(cookie)

opener = build_opener(handler)

response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value