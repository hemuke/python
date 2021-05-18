import threading
import time

print("hello world ----- 2021-04-06 starting")


class LoopThread(threading.Thread):
    n = 0

    def run(self):
        while self.n < 5:
            print(self.n)
            now_thread = threading.current_thread()
            print('[loop]now thread name: {0}'.format(now_thread.name))
            time.sleep(1)
            self.n += 1

#n = 0
#
# class LoopThread(threading.Thread):
#    def run(self):
#        global n
#        while n < 5:
#            print(n)
#            now_thread = threading.current_thread()
#            print('[loop]now thread name: {0}'.format(now_thread.name))
#            time.sleep(1)
#            n += 1
#print("hello world ----- 2021-04-06 ending")


if __name__ == "__main__":
    t = LoopThread(name='Loop_thread_oop')
    t.start()
    t.join()

print("hello world ----- 2021-04-06 ending")
