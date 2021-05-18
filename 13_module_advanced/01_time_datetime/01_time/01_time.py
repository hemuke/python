import time

start_time = time.time() # 时间戳
count = 1 
while True:
    print('抓取百度的信息')
    time.sleep(1)    #爬虫抓了太频繁就要被封因此不建议使用
    count += 1
    if count > 5:
        break
end_time = time.time() # 时间戳
print(end_time - start_time)
