#! /root/anaconda3/bin/python
import time
from multiprocessing import Process
from multiprocessing import current_process

print('父进程启动(%d--%s)' % (current_process().pid, current_process().name))


def do_sth(arg1, arg2):
    print('子进程启动(%d--%s)' % (current_process().pid, current_process().name))
    print('arg1 = %d, arg2 = %d' % (arg1, arg2))
    print('子进程结束(%d--%s)' % (current_process().pid, current_process().name))


process = Process(target=do_sth, args=(5, 8))
process.start()
time.sleep(2)
print('父进程结束(%d--%s)' % (current_process().pid, current_process().name))

"""
class Process(process.BaseProcess):
    _start_method = None
    @staticmethod
    def _Popen(process_obj):
        return _default_context.get_context().Process._Popen(process_obj)


class BaseProcess(object):
    '''
    Process objects represent activity that is run in a separate process

    The class is analogous to `threading.Thread`
    '''
    def _Popen(self):
        raise NotImplementedError

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={},
                 *, daemon=None):
        assert group is None, 'group argument must be None for now'
        count = next(_process_counter)
        self._identity = _current_process._identity + (count,)
        self._config = _current_process._config.copy()
        self._parent_pid = os.getpid()
        self._popen = None
        self._closed = False
        self._target = target
        self._args = tuple(args)
        self._kwargs = dict(kwargs)
        self._name = name or type(self).__name__ + '-' + \
                     ':'.join(str(i) for i in self._identity)
        if daemon is not None:
            self.daemon = daemon
        _dangling.add(self)

    def _check_closed(self):
        if self._closed:
            raise ValueError("process object is closed")

    def run(self):
        '''
        Method to be run in sub-process; can be overridden in sub-class
        '''
        if self._target:
            self._target(*self._args, **self._kwargs)

    def start(self):
        '''
        Start child process
        '''
        self._check_closed()
        assert self._popen is None, 'cannot start a process twice'
        assert self._parent_pid == os.getpid(), \
               'can only start a process object created by current process'
        assert not _current_process._config.get('daemon'), \
               'daemonic processes are not allowed to have children'
        _cleanup()
        self._popen = self._Popen(self)
        self._sentinel = self._popen.sentinel
        # Avoid a refcycle if the target function holds an indirect
        # reference to the process object (see bpo-30775)
        del self._target, self._args, self._kwargs
        _children.add(self)
"""
