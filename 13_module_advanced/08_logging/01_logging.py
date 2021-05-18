import logging

# filename: 文件名
# format: 数据的格式化输出. 最终在日志文件中的样子
#     时间-名称-级别-模块: 错误信息
# datefmt: 时间的格式
# level: 错误的级别权重, 当错误的级别权重大于等于leval的时候才会写入文件
logging.basicConfig(filename='x1.txt',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=40)  # 记录文件中的日志的最低等级


# logging.log(100, "你好，我是20")
logging.critical("今天系统奔溃") # 最高级别的日志信息 50分
logging.error("bug")  # 40分
logging.warning("warning") # 30分
logging.info("info")    # 20分
logging.debug("debug")  # 10分

"""
2021-03-22 17:04:44 - root - Level 100 -01_logging:  你好，我是20
2021-03-22 17:08:50 - root - CRITICAL -01_logging:  今天系统奔溃
2021-03-22 17:08:50 - root - ERROR -01_logging:  bug
2021-04-12 17:47:25 - root - CRITICAL -01_logging:  今天系统奔溃
2021-04-12 17:47:25 - root - ERROR -01_logging:  bug
"""
