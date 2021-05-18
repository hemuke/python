import logging

# 如果想要把日志记录在不同的文件中

# 创建一个操作日志的对象logger（依赖FileHandler）
file_handler = logging.FileHandler('l1.log', 'a', encoding='utf-8')  # f = open()
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s"))

logger1 = logging.Logger('财务系统', level=40)  # 创建日志对象
logger1.addHandler(file_handler)  # 给日志对象设置文件信息


# 再创建一个操作日志的对象logger（依赖FileHandler）
file_handler2 = logging.FileHandler('l2.log', 'a', encoding='utf-8')
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s"))

logger2 = logging.Logger('会计系统', level=40)
logger2.addHandler(file_handler2)



# 项目1: 财务系统出错了
logger1.error('财务系统炸了. 程序员出来工作了')
# 项目2: 会计系统出错了
logger2.error("会计系统出错了. 领导出来溜达溜达")

logger1.log(9999, '没事儿 ')

"""
(base) [root@k8s-ansible 08_logging]# cat l1.log 
2021-03-22 17:18:38,534 - 财务系统 - ERROR -02_logging:  财务系统炸了. 程序员出来工作了
2021-03-22 17:18:38,534 - 财务系统 - Level 9999 -02_logging:  没事儿 
2021-03-22 17:26:45,991 - 财务系统 - ERROR -02_logging:  财务系统炸了. 程序员出来工作了
2021-03-22 17:26:45,991 - 财务系统 - Level 9999 -02_logging:  没事儿 
2021-03-22 17:29:14,314 - 财务系统 - ERROR -<stdin>:  财务系统炸了. 程序员出来工作了
2021-03-22 17:29:14,344 - 财务系统 - Level 9999 -<stdin>:  没事儿 
"""
