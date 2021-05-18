threading模块的对象

对象
Thread			表示一个执行线程的对象
Lock			锁原语对象 （和thread模块中的锁一样）
RLock			可重入锁对象，使单一线程可以（再次）获得已持有的锁（递归锁）
Condition		条件变量对象，使得一个线程等待另一个线程满足特定的"条件"，比如改变状态或某个数据值
Event			条件变量的通用版本，任意数量的线程等待某个时间的发生，在该事件发生后所有线程将被激活
Semaphore		为线程间共享的有限资源提供了一个"计数器"，如果没有可用资源时会被阻塞
BoundedSemaphore	与Semaphore相似，不过它不允许超过初始值
Barrier			创建一个"障碍"，必须达到指定的数量的线程后才可以继续

属性
name			线程名
ident			线程的标识符
daemon			布尔标志，表示这个线程是否是守护线程

方法
__init__()		实例化一个线程对象，需要有一个可调用的target，以及其参数args或kwargs
start()			开始执行该线程
run()			定义线程功能的方法（通常在子类重被应用开发者重写）
join(timeout=None)	timeout(秒)，否者会一直阻塞
getName()		返回线程名
setName(name)		设定线程名
isAlivel/is_alive()	布尔标志，表示这个线程是否还存活
isDaemon()		如果是守护线程，则返货True; 否者，返回False
setDaemon()		把线程的守护标志设定为布尔值daemonic(必须在线程start()之前调用)
