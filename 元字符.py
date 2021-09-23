"""
作者：ZYC
时间：2021年09月23日
"""
import re

# []:列表符号，用于一组字符
txt = 'else if(i==2) {} else else else'
x = re.findall('[a-z]', txt)
print(x)

# \d 匹配数字符号
# . 匹配除了换行符之外的任意字符,匹配一个
# ^ 匹配开始，匹配到返回匹配值到列表，否则返回空表
# $ 匹配结束，匹配到返回匹配值到列表，否则返回空表
x1 = re.findall('\d', txt)
print(x1)

x2 = re.findall('if.+2', txt)
print(x2)

x3 = re.findall('^a', txt)
print(x3)

x4 = re.findall('}$', txt)
print(x4)

# * 匹配0次或多次
# + 匹配1次或多次
txt = 'zyc zyc zyc zzz zsx zas'
x5 = re.findall('zyc*', txt)
print(x5)
x6 = re.findall('zyc+', txt)
print(x6)

# {} 集合符号，指定出现次数
txt = 'zz zz'
x7 = re.findall('z{2}', txt)
print(x7)

# | 或符，匹配两者其一
txt = 'zyc Zyc'
x = re.findall('z|d', txt)
print(x)
