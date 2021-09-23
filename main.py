"""
作者：ZYC
时间：2021年09月22日
"""
import re

# findall函数返回包含所有匹配值的列表
txt = 'ZYC是帅哥'
x = re.findall('dd', txt)
if x:
    print('Yes')
else:
    print('No')

# search函数在字符串中搜索匹配项，成功返回Match对象，只返回第一个出现的匹配项,未匹配到返回None
txt = 'zyc zyc zyc'
x = re.search("\s", txt)  # \s 匹配空格
print(x.start())
# print(x)

# spilt函数返回列表，在匹配时拆分字符串,可以指定拆分次数
txt = 'else if (i==2) {}'
x = re.split('\s', txt, 2)
print(x)

# sub函数替换指定的字符
x = re.sub('if', 'else', txt, 1)
print(x)
