#!/usr/bin/env python
# URL to tag HTML
# By: tedezed
# Source: http://stackoverflow.com/questions/33368697/replace-a-url-into-anchor-tag-using-a-python-regex/


import re
p = re.compile(ur'''[^<">]((ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?)[^< ,"'>]''', re.MULTILINE)
test_str = u"I was surfing http://www.google.com, where I found my tweet, check it out <a href=\"http://tinyurl.com/blah\">http://tinyurl.com/blah</a>"

for item in re.finditer(p, test_str):
    result = item.group(0)
    result = result.replace(' ', '')
    print result
    end_result = test_str.replace(result, '<a href="' + result + '">' + result + '</a>')

print end_result
