import threading
import time

print("hello world ----- 2021-04-06 starting")


def loop():
    """ 新线程执行的代码"""
    now_thread = threading.current_thread()
    n = 0
    while n < 5:
        print('[loop]now thread name: {0}'.format(now_thread.name))
        print(n)
        time.sleep(2)
        n += 1


def use_thread():
    """ 使用线程来实现"""
    # 当前正在执行的线程名称
    now_thread = threading.current_thread()
    print('now thread name: {0}'.format(now_thread.name))
    t = threading.Thread(target=loop, name='loop_thread')
    # 启动守护进程
    # t.daemon = True

    # 启动线程
    t.start()

    # 挂起线程
    # t.join()


#print("hello world ----- 2021-04-06 ending")

if __name__ == "__main__":
    use_thread()
    print("hello world ----- 2021-04-06 ending")
