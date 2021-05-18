#! /root/anaconda3/bin/python
"""
一、什么是异常
    异常指的是程序在没有语法错误的前提下，在运行期间产生的特定错误。
    每个特定错误都对应一个异常对象。当产生某个特定错误时，其对应的异常类对象的实例对象就会抛出。
    如果在程序中对抛出异常实例对象不进行捕获和处理，程序就会停止运行，并且打印错误的详细信息，包括：
    1.Traceback,它指的是异常调用堆栈的跟踪信息，其中列出了程序中的相关行数。
    2.对应的异常类对象的名称，以及异常的错误信息。
    如果在程序中对抛出的异常实例对象进行捕获和对象，程序就会继续运行。
    那些特定错误会被看做异常呢？首先，Python内置了很多异常类对象，其次，可以自定义异常类对象，所以，内置的异常类对象和自定义的异常类对象，所以，内置的异常类对象和自定的异常类对象对应的错误会被看做异常。
"""
