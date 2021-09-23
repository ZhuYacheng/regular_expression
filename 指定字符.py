"""
作者：ZYC
时间：2021年09月23日
"""
import re

# \A 指定开头字符，若指定字符在字符串开头，则返回该字符
# \b 返回指定字符位于开头或结尾的匹配项
# \B 匹配中间字符，返回不在开头或结尾的匹配项
# \d 匹配数字
# \D 匹配非数字
# \s 匹配空格
# \S 匹配非空格
# \w 匹配任意数字和字母（a-z，0-9，_）
# \W 匹配任意非字母和数字
txt = 'ge ZYC is da ge'
x = re.findall('\AZYC', txt)
print(x)

x1 = re.findall(r'\bZYC|ge\b', txt)  # 开头'r'确保字符串被视为原始字符串
print(x1)

txt = '我是菜鸟我是大神'
x2 = re.findall(r'\B我', txt)
print(x2)

txt = 'group ZYC is da ge'
x3 = re.search(r"g\w+\b", txt)
print(x3.group())
