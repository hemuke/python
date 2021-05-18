#! /root/anaconda3/bin/python
phonebook = {'张三': '1333333',
             '李四': '1444444',
             '王五': '1555555',
             '赵六': '1666666'}

print('王五的号码：%s，张三的号码：%s' % (phonebook['王五'], phonebook['张三']))
print('王五的号码：%(王五)s，张三的号码：%(张三)s' % phonebook)


phonebook = {'张三': '1333333',
             '李四': '1444444',
             '王五': '1555555',
             '赵六': '1666666'}
print('王五的号码：{}，张三的号码：{}'.format(phonebook['王五'], phonebook['张三']))
print('王五的号码：{王五}，张三的号码：{张三}'.format_map(phonebook))
