"""
作者：ZYC
时间：2021年09月23日
"""
import re

txt = 'The rain in fujian'
x = re.findall('[arn]', txt)  # 匹配[]中任意字母
print(x)

x1 = re.findall('[a-n]', txt)  # 匹配字母a-n之间的任意字母
print(x1)

x3 = re.findall('[^arn]', txt)  # 匹配除了arn的任意字符
print(x3)
