"""
作者：ZYC
时间：2021年09月23日
"""
import re

s1 = 'adkkdk'
s2 = 'abc1efg'

an = re.search('^[a-z]+$', s1)  # 从开始匹配到结束，含有全是字母的字符串则返回列表
print(an)

an1 = re.match('[a-z]+$', s2)  # 从开始匹配到结束，含有全是字母的字符串则返回列表
print(an1)

a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0))  # 123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1))  # 123
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))  # abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3))  # 456

sen = "abc,123,456,789,mnp"
while 1:
    mm = re.search("\d,\d", sen)
    print(mm.group())
    if mm:
        mm = mm.group()

        sen = sen.replace(mm, mm.replace(",", ""))
        print(sen)
    else:
        break
