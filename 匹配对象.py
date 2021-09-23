"""
作者：ZYC
时间：2021年09月23日
"""
import re

# search 返回对象
txt = 'My name Sis worlds w world'
x = re.search('is', txt)
print(x)

# span函数
x1 = re.search(r"\bS\w+", txt)  # 搜索以‘S’开头的单词，并打印其位置
print(x1.span())

# string打印传递给函数字符串
x2 = re.search(r"\bS\w+", txt)
print(x2.string)

# group 打印字符串的匹配部分
x3 = re.search(r"\bw\w+", txt)
print(x3.group())
