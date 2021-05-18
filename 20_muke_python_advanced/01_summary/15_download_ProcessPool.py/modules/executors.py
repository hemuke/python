# -*- encoding=utf-8 -*-


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


MULTI_NUMS = 8

thread_pool_executor = ThreadPoolExecutor(MULTI_NUMS)
process_pool_executor = ProcessPoolExecutor(MULTI_NUMS)
