from threading import Thread, local, current_thread

thread_local = local()


def do_sth(arg1, arg2, arg3):
    thread_local.local_var1 = arg1
    thread_local.local_var2 = arg2
    thread_local.local_var3 = arg3

    fun1()
    fun2()
    fun3()


def fun1():
    print(
        '%s: %s -- %s -- %s' %
        (current_thread().name,
         thread_local.local_var1,
         thread_local.local_var2,
         thread_local.local_var3))


def fun2():
    print(
        '%s: %s -- %s -- %s' %
        (current_thread().name,
         thread_local.local_var1,
         thread_local.local_var2,
         thread_local.local_var3))


def fun3():
    print(
        '%s: %s -- %s -- %s' %
        (current_thread().name,
         thread_local.local_var1,
         thread_local.local_var2,
         thread_local.local_var3))


t1 = Thread(target=do_sth, args=('a', 'b', 'c'))
t2 = Thread(target=do_sth, args=('d', 'e', 'f'))

t1.start()
t2.start()
